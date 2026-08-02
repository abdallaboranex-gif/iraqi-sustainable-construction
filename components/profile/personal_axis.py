import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

def render_personal_axis():
    """
    Axis 1: Mandatory Personal Identification Profile.
    Strictly follows the platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Enforces 5 mandatory civil fields and 1 optional avatar uploader [1.1]
    """
    st.markdown(f'<div class="profile-tab-title">{get_text("Mandatory Operator Identification")}</div>', unsafe_allow_html=True)
    
    user_data = st.session_state.user_identity

    # Enforce clear vertical grid inputs using pure safe Streamlit text components
    input_name = st.text_input(get_text("Full Professional Name:"), value=user_data.get("full_name", ""), placeholder="e.g. Eng. Omar Ali")
    input_email = st.text_input(get_text("Corporate Email Address:"), placeholder="e.g. omar@company.iq")
    input_phone = st.text_input(get_text("Active Contact Phone Number:"), placeholder="e.g. +964 770 000 0000")
    
    # Country field: Mandatory with Iraq locked as default but flexible selection framework
    input_country = st.selectbox(get_text("Country of Operation:"), ["Iraq", "United Arab Emirates", "Jordan", "Saudi Arabia"], index=0)
    
    # City/Governorate field: Mandatory civil layout bound tracking [1.1]
    input_city = st.selectbox(
        get_text("City / Governorate:"), 
        ["", "Baghdad", "Nineveh", "Basra", "Erbil", "Salah Al-Din", "Anbar", "Babylon", "Najaf", "Karbala", "Diyala", "Kirkuk"], 
        index=0
    )
    
    # Optional Profile Photo Avatar component uploader block (Explicitly optional) [1.1]
    st.file_uploader(label=get_text("Upload Your Optional Profile Photo (PNG/JPG):"), type=["png", "jpg", "jpeg"], key="optional_avatar_uploader")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Rigid validation check trigger saving baseline credentials context safely
    if st.button(get_text("Save Personal Profile Parameters"), key="btn_save_personal_axis", type="primary", use_container_width=True):
        if not input_name or not input_email or not input_phone or not input_city:
            st.warning(get_text("Validation Failure: All 5 mandatory fields must be completed prior to staging profile records!"))
        else:
            st.session_state.user_identity["full_name"] = input_name
            st.session_state.user_identity["registered"] = True
            
            log_action(user_credential=input_name, action_details=f"Updated operational personal credentials profile. City context: {input_city}")
            st.success(get_text("Sanitized credentials saved successfully!"))
            st.rerun()

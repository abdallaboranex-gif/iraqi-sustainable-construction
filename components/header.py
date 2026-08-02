import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

def handle_language_switch():
    """
    Sovereign Language Callback Subroutine.
    Executes safely in the backend thread context BEFORE the UI redraws.
    Completely eliminates double-triggering lag and interface freezing loops [1.1].
    """
    # Capture the freshly selected token from the temporary bridge widget
    new_lang = st.session_state.get("temp_lang_selector")
    if new_lang:
        # Commit the choice securely to the sovereign central source of truth
        st.session_state.language = new_lang

def render_header():
    """
    Component: Sovereign Top Header & Secure Digital Identity Navigation Bar.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Streamlined to support pure English (EN) and Arabic (العربية) only [1.1]
    - Decouples state changes via handle_language_switch callback to resolve lag permanently [1.1]
    """
    user_data = st.session_state.user_identity
    
    display_name = user_data["full_name"] if user_data["registered"] else get_text("Unregistered Account")
    display_rank = user_data["rank_title"] if user_data["registered"] else get_text("Click to Verify Identity")

    col_brand, col_context, col_user = st.columns([2.6, 1.8, 1.6], gap="small")
    
    # Left Column: Brand Identity
    with col_brand:
        st.markdown(
            f"""
            <div style='text-align: left; padding-top: 5px;'>
                <h2 style='color: #1D4ED8; margin: 0; font-weight: 800; font-size: 24px; letter-spacing: 0.5px;'>
                    Iraqi Green Construction Data Platform
                </h2>
                <h4 style='color: #0F172A; margin: 2px 0 0 0; font-weight: 800; font-size: 16px;'>
                    {get_text('Iraqi Green Construction Data Platform')}
                </h4>
                <p style='color: #475569; margin: 4px 0 0 0; font-size: 12px; font-weight: 700; word-spacing: 2px;'>
                    DATA • COMPLIANCE • SUSTAINABILITY • EFFICIENCY
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    # Middle Column: Geolocation & Optimized Dual-Language Control Pipeline
    with col_context:
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            current_gov = st.session_state.property_data.get("governorate", "Baghdad")
            st.markdown(
                f"""
                <div style='background-color: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 10px; padding: 6px 12px; text-align: center; margin-top: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);'>
                    <span style='color: #475569 !important; font-size: 11px !important; font-weight: 700 !important; display: block;'>{get_text('Current Location')}</span>
                    <strong style='color: #1D4ED8 !important; font-size: 15px !important; font-weight: 800 !important; display: block; margin-top: 2px;'>📍 {current_gov}</strong>
                </div>
                """, 
                unsafe_allow_html=True
            )
        with sub_col2:
            st.markdown(f"<span style='color: #0F172A; font-size: 12px !important; font-weight: 700; display: block; margin-top: 2px; text-align: center;'>{get_text('Language')}</span>", unsafe_allow_html=True)
            
            lang_options = ["العربية", "EN"]
            current_lang = st.session_state.get("language", "العربية")
            default_idx = 1 if current_lang == "EN" else 0
            
            # SAFE ISOLATED WIDGET: Intercepts input and updates state via Callback before page reruns
            st.segmented_control(
                label="Language Selector", 
                options=lang_options, 
                default=lang_options[default_idx], 
                label_visibility="collapsed", 
                key="temp_lang_selector",
                on_change=handle_language_switch
            )

    # Right Column: User Profile Details
    with col_user:
        st.markdown(
            f"""
            <div style='display: flex; align-items: center; justify-content: flex-end; gap: 14px; padding-top: 5px; margin-bottom: 2px;'>
                <div style='text-align: right;'>
                    <span style='color: #0F172A; font-weight: 800; font-size: 15px; display: block;'>{display_name}</span>
                    <span style='color: #475569; font-weight: 700; font-size: 12px; display: block;'>{display_rank}</span>
                </div>
                <img src='{user_data["avatar_url"] if user_data["avatar_url"] else "https://unsplash.com"}' 
                     style='width: 44px; height: 44px; border-radius: 50%; border: 2.5px solid #1D4ED8; object-fit: cover; box-shadow: 0 2px 4px rgba(0,0,0,0.1);' />
            </div>
            """, 
            unsafe_allow_html=True
        )
        if st.button(get_text("Click to Verify Identity"), key="open_profile_drawer", use_container_width=True):
            st.session_state.show_profile_drawer = True
            
    # Legal Accountability Sidebar
    if st.session_state.get("show_profile_drawer", False):
        with st.sidebar:
            if st.button(get_text("Close & Return"), use_container_width=True):
                st.session_state.show_profile_drawer = False
                st.rerun()
                
            st.markdown(f"## {get_text('Documentation & Legal Accountability Portal')}")
            st.markdown(f"<p style='color: #475569; font-size: 12px;'>{get_text('Official IDs must be uploaded to bear full legal accountability for the data and engineering blueprints.')}</p>", unsafe_allow_html=True)
            
            if not user_data["registered"]:
                st.markdown(f"<h4 style='color: #1D4ED8; font-size: 15px; margin-top: 10px;'>{get_text('Create Register:')}</h4>", unsafe_allow_html=True)
                input_name = st.text_input(get_text("User's Full Quadruple Name:"), placeholder="Eng. Abdulla Omar")
                user_role = st.selectbox(get_text("Technical Role in the Project:"), ["Consultant Engineer", "Property Owner", "Certified Contractor"])
                input_nid = st.text_input(get_text("National Unified ID Number (12 Digits):"), max_chars=12, placeholder="199204358112")
                
                input_sid = ""
                if user_role == "Consultant Engineer":
                    input_sid = st.text_input(get_text("Valid Iraqi Engineers Syndicate ID Number:"), placeholder="40512")
                    
                uploaded_avatar = st.file_uploader(get_text("Upload Your Official Profile Photo (PNG/JPG):"), type=["png", "jpg", "jpeg"], key="user_avatar_uploader")
                
                if st.button(get_text("Approve, Verify Identity & Launch Sovereign Permissions"), use_container_width=True):
                    if input_name and input_nid:
                        st.session_state.user_identity["registered"] = True
                        st.session_state.user_identity["full_name"] = input_name
                        st.session_state.user_identity["rank_title"] = get_text("Licensed Consultant Engineer") if user_role == "Consultant Engineer" else get_text(user_role)
                        st.session_state.user_identity["national_id"] = input_nid
                        st.session_state.user_identity["syndicate_id"] = input_sid if input_sid else "N/A"
                        st.session_state.user_identity["projects_list"] = [{"id": 1, "name": "Initial Unregistered Property File", "status": "compliant"}]
                        
                        log_action(user_credential=input_name, action_details="Registered official digital ID profile under legal accountability guidelines.")
                        st.success(get_text("Verified Successfully!"))
                        st.rerun()
                    else:
                        st.warning(get_text("Required Fields!"))
            else:
                st.markdown(f"<h4 style='color: #10B981; font-size: 15px; margin-top: 10px;'>✔️ {get_text('Identity Verified Status')}</h4>", unsafe_allow_html=True)
                st.text_input(get_text("Registered Operator Nominee"), value=user_data["full_name"], disabled=True)
                st.text_input(get_text("Sovereign Technical Rank"), value=user_data["rank_title"], disabled=True)
                st.text_input(get_text("Masked National ID Tracking Number"), value=f"XXXXXXXX{user_data['national_id'][-4:] if len(user_data['national_id']) >= 4 else '0000'}", disabled=True)
                
                if st.button(get_text("Revoke Profile Authorization Logs"), use_container_width=True, type="primary"):
                    st.session_state.user_identity["registered"] = False
                    log_action(user_credential=user_data["full_name"], action_details="Revoked operator security authorization profile context manually.")
                    st.rerun()

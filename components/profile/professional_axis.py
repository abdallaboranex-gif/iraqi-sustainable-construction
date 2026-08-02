import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

def render_professional_axis():
    """
    Axis 2: Mandatory Professional Credentials Profile.
    Strictly follows the platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Incorporates an optional Freelance selection within the workplace grid
    - Pre-staged infrastructure for future mandatory syndicate locks
    """
    st.markdown(f'<div class="profile-tab-title">{get_text("Mandatory Engineering Credentials")}</div>', unsafe_allow_html=True)
    
    # 1. Mandatory Technical Profession & Specialty Fields
    input_profession = st.text_input(get_text("Profession / Title:"), placeholder="e.g. Civil Engineer, Project Manager")
    input_specialty = st.text_input(get_text("Technical Specialty Area:"), placeholder="e.g. Structural Engineering, Green Architecture")
    
    # 2. Mandatory Experience Counter using numeric input bounds
    input_experience = st.number_input(get_text("Years of Experience:"), min_value=0, max_value=60, value=0, step=1)
    
    # 3. Dynamic Workplace Input: Allows Freelance or Custom Company registration
    workplace_mode = st.selectbox(
        get_text("Workplace Framework Entity:"), 
        ["", "Corporate Company / Consulting Bureau", "Independent Work / Freelance"],
        index=0
    )
    
    input_company = ""
    if workplace_mode == "Corporate Company / Consulting Bureau":
        input_company = st.text_input(get_text("Company or Bureau Name:"), placeholder="e.g. Al-Rafidain Construction Co.")
    elif workplace_mode == "Independent Work / Freelance":
        input_company = "Independent Work / Freelance"
        st.caption(get_text("Account context registered under individual consultant framework guidelines."))

    # 4. Sovereign Syndicate Vault: Currently explicitly optional until federal mapping matrix goes active
    st.markdown("<hr style='border-color: #E2E8F0; margin: 15px 0;'>", unsafe_allow_html=True)
    st.write(f"**{get_text('National Union Authorization')}**")
    
    input_syndicate_id = st.text_input(
        get_text("Iraqi Engineers Syndicate ID Number (Optional for Corporate Phase):"), 
        placeholder="e.g. 40512",
        value=""
    )
    st.caption(get_text("Note: National syndicate validation vectors remain locked until official ministry integration link goes live."))

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 5. Rigid submission safeguard checking values against blank entities prior to staging
    if st.button(get_text("Save Professional Profile Parameters"), key="btn_save_professional_axis", type="primary", use_container_width=True):
        if not input_profession or not input_specialty or not workplace_mode or (workplace_mode == "Corporate Company / Consulting Bureau" and not input_company):
            st.warning(get_text("Validation Failure: Please fill out all mandatory professional and workplace fields first!"))
        else:
            # Sync verified configurations back to the global state tracker
            st.session_state.user_identity["rank_title"] = get_text(input_profession)
            st.session_state.user_identity["syndicate_id"] = input_syndicate_id if input_syndicate_id else "N/A"
            
            log_action(
                user_credential=st.session_state.user_identity.get("full_name", "Anonymous Operative"), 
                action_details=f"Updated technical profile parameters. Specialty: {input_specialty}, Entity: {input_company}"
            )
            st.success(get_text("Sanitized credentials saved successfully!"))
            st.rerun()

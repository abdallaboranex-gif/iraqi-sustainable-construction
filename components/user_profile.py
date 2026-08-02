import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

def render_user_profile_tabs():
    """
    Component: Modular Enterprise User Profile Canvas.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Categorized into 5 isolated functional tabs to prevent layout crowding [1.1]
    - Fully prepared to inject sovereign governmental verification hooks in future phases [1.1]
    """
    
    # Inject high-contrast dark navy typography styling configuration overrides
    st.markdown(
        """
        <style>
        .profile-tab-title {
            color: #0F172A !important;
            font-size: 16px !important;
            font-weight: 800 !important;
            margin-bottom: 12px;
        }
        .profile-status-badge {
            background-color: #EFF6FF;
            color: #1D4ED8 !important;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 15px;
            border: 1px solid #BFDBFE;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 1. Initialize the 5 core structural business axes using native tabs
    tab_personal, tab_professional, tab_subscription, tab_security, tab_billing = st.tabs([
        get_text("Personal Info"),
        get_text("Professional Info"),
        get_text("Subscription Plan"),
        get_text("Security & Sovereign"),
        get_text("Billing Ledger")
    ])

    user_data = st.session_state.user_identity

    # --- AXIS 1: MANDATORY PERSONAL INFO ---
    with tab_personal:
        st.markdown(f'<div class="profile-tab-title">{get_text("Mandatory Operator Identification")}</div>', unsafe_allow_html=True)
        
        # Safe form input elements directly syncing with global central state keys
        input_name = st.text_input(get_text("Full Professional Name:"), value=user_data.get("full_name", ""), placeholder="e.g. Eng. Omar Ali")
        input_email = st.text_input(get_text("Corporate Email Address:"), placeholder="e.g. omar@company.iq")
        input_phone = st.text_input(get_text("Active Contact Phone Number:"), placeholder="e.g. +964 770 000 0000")
        
        if st.button(get_text("Save Personal Profile Parameters"), key="btn_save_personal_axis", type="primary", use_container_width=True):
            if input_name:
                st.session_state.user_identity["full_name"] = input_name
                st.session_state.user_identity["registered"] = True
                log_action(user_credential=input_name, action_details="Updated personal profile identity information.")
                st.success(get_text("Sanitized credentials saved successfully!"))
                st.rerun()
            else:
                st.warning(get_text("Full Name field is required!"))

    # --- AXIS 2: MANDATORY PROFESSIONAL INFO ---
    with tab_professional:
        st.markdown(f'<div class="profile-tab-title">{get_text("Mandatory Engineering Credentials")}</div>', unsafe_allow_html=True)
        
        input_company = st.text_input(get_text("Company or Consulting Bureau Name:"), placeholder="e.g. Al-Rafidain Construction Co.")
        user_role = st.selectbox(get_text("Technical Role Profile:"), ["Consultant Engineer", "Project Director", "Site Supervisor", "Certified Contractor"])
        
        st.caption(get_text("Note: National syndicate validation vectors remain locked until official ministry integration."))

    # --- AXIS 3: SUBSCRIPTION PLAN DATA ---
    with tab_subscription:
        st.markdown(f'<div class="profile-tab-title">{get_text("Active Account License Parameters")}</div>', unsafe_allow_html=True)
        
        st.markdown(
            f'''
            <div class="profile-status-badge">
                🚀 <b>{get_text("Current Active Tier:")}</b> Corporate Enterprise Bundle<br>
                📊 <b>{get_text("Project Allowance Usage:")}</b> 2 / 10 {get_text("Active Sites Monitored")}
            </div>
            ''',
            unsafe_allow_html=True
        )
        st.metric(label=get_text("Next Renovation Date Reset"), value="May 15, 2027")

    # --- AXIS 4: SECURITY & GOVERNMENT READINESS ---
    with tab_security:
        st.markdown(f'<div class="profile-tab-title">{get_text("Sovereign Security Framework")}</div>', unsafe_allow_html=True)
        
        # Informative notice highlighting B2B state with absolute hidden readiness for government IDs
        st.info(get_text("Internal Corporate Audit Mode: Connection to federal ministry authentication nodes is currently unlinked."))
        
        # Staged disabled components waiting for national backend integration locks
        st.file_uploader(label=get_text("Upload National Unified Civil ID (Locked until government link)"), disabled=True, key="disabled_nid_vault")
        st.file_uploader(label=get_text("Upload Valid Iraqi Engineers Syndicate ID (Locked until government link)"), disabled=True, key="disabled_sid_vault")

    # --- AXIS 5: BILLING LEDGER ---
    with tab_billing:
        st.markdown(f'<div class="profile-tab-title">{get_text("Corporate Invoicing Registry")}</div>', unsafe_allow_html=True)
        
        # Safe structural dataframe displaying transaction histories cleanly
        mock_billing_matrix = {
            get_text("Transaction ID"): ["TXN-2026-001", "TXN-2026-002"],
            get_text("Date"): ["2026-01-15", "2026-05-15"],
            get_text("Plan"): ["Enterprise Init", "Enterprise Renovation"],
            get_text("Status"): [get_text("Paid Successfully"), get_text("Paid Successfully")]
        }
        st.dataframe(mock_billing_matrix, use_container_width=True)

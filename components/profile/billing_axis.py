import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

def render_billing_axis():
    """
    Axis 5: Corporate Invoicing Registry & Commercial Plan Tier Upgrades.
    Strictly follows the platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Direct PDF download mock setups and Master/Visa methods [1.1]
    """
    st.markdown(f'<div class="profile-tab-title">{get_text("Corporate Invoicing Registry")}</div>', unsafe_allow_html=True)
    
    # 1. Payment Methods Secure Matrix Card
    st.write(f"**{get_text('Linked Corporate Payment Methods')}**")
    st.markdown(
        f'''
        <div class="profile-status-badge" style="background-color: #F8FAFC; border-color: #E2E8F0; color: #475569 !important;">
            💳 <b>MasterCard Personal Credit Wallet</b><br>
            Card Identity: **** **** **** 4012 • Expiration Boundary: 12/29
        </div>
        ''',
        unsafe_allow_html=True
    )
    if st.button(get_text("Update / Bind New Bank Card Method"), key="btn_trigger_card_rewrite", use_container_width=True):
        st.toast(get_text("Secure billing authorization gateway initiated."))

    st.markdown("<hr style='border-color: #E2E8F0; margin: 15px 0;'>", unsafe_allow_html=True)

    # 2. Plan Tier Matrix Upgrades: Shift between the 4 verified commercial tier buckets [1.1]
    st.write(f"**{get_text('License Scale Optimization Workspace')}**")
    current_tier = st.session_state.subscription.get("tier", "Enterprise")
    
    new_tier_selection = st.radio(
        get_text("Modify Active Project Allowance Capacity Package Tier:"),
        ["Free", "Pro", "Team", "Enterprise"],
        index=["Free", "Pro", "Team", "Enterprise"].index(current_tier),
        help=get_text("Modifying allowance profiles dynamically adjusts invoice matrices and scales project site audit data allowances.")
    )
    
    if new_tier_selection != current_tier:
        if st.button(get_text("Confirm License Scale Adjustment Order"), type="primary", use_container_width=True):
            st.session_state.subscription["tier"] = new_tier_selection
            # Scaled projects allowances drive logic parameters instantly
            if new_tier_selection == "Free": st.session_state.subscription["max_projects"] = 1
            elif new_tier_selection == "Pro": st.session_state.subscription["max_projects"] = 5
            elif new_tier_selection == "Team": st.session_state.subscription["max_projects"] = 15
            elif new_tier_selection == "Enterprise": st.session_state.subscription["max_projects"] = 50
            
            log_action(user_credential=st.session_state.user_identity.get("full_name", "Anonymous Partner"), action_details=f"Scaled active license subscription tier mapping to: {new_tier_selection}")
            st.success(get_text("Subscription scale updated successfully!"))
            st.rerun()

    st.markdown("<hr style='border-color: #E2E8F0; margin: 15px 0;'>", unsafe_allow_html=True)

    # 3. Billing Ledger History & Invoice PDF Download triggers [1.1]
    st.write(f"**{get_text('Historical Billing Records')}**")
    
    # Render native grid containing invoice trace with mock file download anchors
    b_col1, b_col2, b_col3, b_col4 = st.columns([1.5, 1.2, 1.2, 1.1])
    with b_col1: st.markdown(f"<b>{get_text('Invoice ID')}</b>", unsafe_allow_html=True)
    with b_col2: st.markdown(f"<b>{get_text('Date')}</b>", unsafe_allow_html=True)
    with b_col3: st.markdown(f"<b>{get_text('Amount')}</b>", unsafe_allow_html=True)
    with b_col4: st.markdown(f"<b>{get_text('Action')}</b>", unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: #F1F5F9; margin: 6px 0;'>", unsafe_allow_html=True)
    
    r1_c1, r1_c2, r1_c3, r1_c4 = st.columns([1.5, 1.2, 1.2, 1.1])
    with r1_c1: st.write("INV-2026-004")
    with r1_c2: st.write("2026-05-15")
    with r1_c3: st.write("$1,200.00")
    with r1_c4: 
        # Clean native vector stream file downloader to download invoice records safely [1.1]
        st.download_button(label=get_text("PDF"), data=b"Mock Invoice Content Trace", file_name="INV-2026-004.pdf", key="btn_dl_inv_004", size="small")

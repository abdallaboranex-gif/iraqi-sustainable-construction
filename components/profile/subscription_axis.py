import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

def render_subscription_axis():
    """
    Axis 3: Active Subscription Plan & License Parameter Ledger.
    Strictly follows the platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Renders the 4 verified commercial tier buckets: Free / Pro / Team / Enterprise [1.1]
    - Incorporates colored active statuses and native dynamic progress trackers [1.1]
    """
    st.markdown(f'<div class="profile-tab-title">{get_text("Active Account License Parameters")}</div>', unsafe_allow_html=True)
    
    # 1. Read or initialize subscription state elements safely to prevent runtime failures
    if "subscription" not in st.session_state:
        st.session_state.subscription = {
            "tier": "Enterprise",  # Verified defaults matching enterprise staging blueprints
            "active": True,
            "auto_renew": False,
            "used_projects": 3,
            "max_projects": 12
        }
        
    sub = st.session_state.subscription

    # 2. Render High-Contrast Visual Metric Blocks for current tier and liveness status
    c1, c2 = st.columns(2)
    with c1:
        # Displays the assigned commercial tier license out of the 4 defined buckets [1.1]
        st.selectbox(
            get_text("Current Assigned Subscription Tier:"),
            ["Free", "Pro", "Team", "Enterprise"],
            index=["Free", "Pro", "Team", "Enterprise"].index(sub["tier"]),
            disabled=True,
            key="sub_tier_display_selectbox"
        )
    with c2:
        # Render a crisp, vivid text status badge indicating activation posture [1.1]
        st.write(f"**{get_text('License Integrity Posture')}**")
        if sub["active"]:
            st.markdown(f'<div class="profile-status-badge" style="background-color: #DCFCE7; color: #15803D !important; border-color: #BBF7D0;">✔️ {get_text("Active Authorization License")}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="profile-status-badge" style="background-color: #FEE2E2; color: #991B1B !important; border-color: #FCA5A5;">❌ {get_text("Expired / Suspended")}</div>', unsafe_allow_html=True)

    # 3. Temporal Bounds: Explicit Subscription Start and Expiration limits
    c3, c4 = st.columns(2)
    with c3:
        st.text_input(get_text("Subscription Activation Date:"), value="2026-01-15", disabled=True)
    with c4:
        st.text_input(get_text("License Expiration Reset Date:"), value="2027-01-15", disabled=True)

    st.markdown("<hr style='border-color: #E2E8F0; margin: 15px 0;'>", unsafe_allow_html=True)

    # 4. Project Allowance Usage Tracker: Native visual progress bar indicator [1.1]
    st.write(f"**{get_text('Project Volume Allowance Logs')}**")
    progress_ratio = float(sub["used_projects"]) / float(sub["max_projects"])
    st.progress(progress_ratio, text=f"{sub['used_projects']} / {sub['max_projects']} {get_text('Active Sites Monitored')}")
    st.caption(get_text("Audit capability threshold tracking enforced across corporate subscription bounds."))

    st.markdown("<br>", unsafe_allow_html=True)

    # 5. Interactive Auto-Renewal Toggle: Secure banking synchronization framework [1.1]
    st.write(f"**{get_text('Banking Synchronization & Renewal')}**")
    renew_toggle = st.toggle(
        get_text("Enable Automated Subscriptions Renewal Process"),
        value=sub["auto_renew"],
        help=get_text("Enforces automated secure credit pull matching contract totals upon reset dates if a valid banking method contains required balances.")
    )
    
    # Update central memory configurations immediately upon client toggle adjustments
    if renew_toggle != sub["auto_renew"]:
        st.session_state.subscription["auto_renew"] = renew_toggle
        log_action(
            user_credential=st.session_state.user_identity.get("full_name", "Anonymous Partner"),
            action_details=f"Modified subscription auto-renewal toggle configuration state to: {renew_toggle}"
        )
        st.rerun()

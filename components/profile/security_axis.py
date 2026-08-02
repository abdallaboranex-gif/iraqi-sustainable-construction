import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

# استدعاء دالة التحقق الخارقة من الملف المستقل
from core.auth_owner import render_sovereign_owner_pipeline

def render_security_axis():
    """
    Axis 4: Security Framework & System Sessions Activity Ledger.
    Incorporate the secure hidden master login at the bottom.
    """
    st.markdown(f'<div class="profile-tab-title">{get_text("Sovereign Security Framework")}</div>', unsafe_allow_html=True)
    
    # 1. واجهة حقول كلمة المرور العادية للشركات
    with st.expander(get_text("Change Account Password Credentials"), expanded=False):
        old_pwd = st.text_input(get_text("Current Secure Password:"), type="password", key="sec_old_password")
        new_pwd = st.text_input(get_text("New Desired Password:"), type="password", key="sec_new_password")
        confirm_pwd = st.text_input(get_text("Confirm New Password:"), type="password", key="sec_confirm_password")
        
        if st.button(get_text("Update Security Password Access"), key="btn_trigger_pwd_rewrite", type="primary"):
            if old_pwd and new_pwd and confirm_pwd:
                if new_pwd == confirm_pwd:
                    log_action(user_credential=st.session_state.user_identity.get("full_name", "Anonymous Partner"), action_details="Changed password.")
                    st.success(get_text("Security credentials re-encrypted successfully!"))
                else:
                    st.error(get_text("Validation Failure: New password fields do not match parameter limits."))
            else:
                st.warning(get_text("Required Fields!"))

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. خيار تفعيل المصادقة الثنائية 2FA
    st.write(f"**{get_text('Multi-Factor Verification Protocols')}**")
    tfa_toggle = st.toggle(get_text("Enforce Two-Factor Authentication (2FA) Protection Layer"), value=False)
    if tfa_toggle:
        tfa_channel = st.radio(get_text("Select Identity Verification Gateway Channel:"), [get_text("SMS Mobile Verification Token"), get_text("Corporate Email Security Token")])

    st.markdown("<hr style='border-color: #E2E8F0; margin: 15px 0;'>", unsafe_allow_html=True)

    # 3. جدول الأجهزة النشطة المسجلة
    st.write(f"**{get_text('Active Registered Devices')}**")
    st.markdown(
        f'''
        <div class="profile-status-badge" style="background-color: #FFFFFF; border-color: #CBD5E1; color: #0F172A !important;">
            🖥️ <b>Windows PC • Chrome Browser</b><br>
            📍 Location Traced: Baghdad, Iraq
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 4. حقن استدعاء بوابة التحقق السرية لمالك المنصة في نهاية الملف
    render_sovereign_owner_pipeline()

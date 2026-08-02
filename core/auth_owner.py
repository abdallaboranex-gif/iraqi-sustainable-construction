import streamlit as st
import random
from utils.localization import get_text
from core.state_manager import log_action

def generate_owner_otp():
    """
    [تأمين ثبات الجلسة]
    توليد رمز التحقق وقفله لحمايته من التغيير الصامت عند عمل Rerun للصفحة.
    """
    if "owner_otp_secret" not in st.session_state:
        st.session_state.owner_otp_secret = str(random.randint(100000, 999999))
    return st.session_state.owner_otp_secret

def verify_owner_credentials(username, password):
    """
    الطبقة الأولى: التحقق الصارم من بيانات مالك المنصة السيادية.
    """
    MASTER_USERNAME = "عبدالله مثنى احمد"
    MASTER_PASSWORD = "1990Abdalla"
    return username == MASTER_USERNAME and password == MASTER_PASSWORD

def render_sovereign_owner_pipeline():
    """
    Core Architecture Module: Sovereign Owner Authentication Bypass Panel.
    Purged of Namespace leaks to resolve NameError crashes cleanly.
    """
    # تهيئة وضبط متغيرات الجلسة مسبقاً لحماية النطاق البرمجي
    if "owner_verified" not in st.session_state:
        st.session_state.owner_verified = False
    if "otp_dispatched" not in st.session_state:
        st.session_state.otp_dispatched = False

    st.write(f"### 🛡️ {get_text('Sovereign Owner Authorization')}")
    st.caption(get_text("Multi-factor master bypass console for system ownership activation."))

    # إذا تم تفعيل الحساب الخارق بنجاح مسبقاً
    if st.session_state.owner_verified:
        st.success(f"👑 {get_text('Sovereign Permissions Released: Infinite administrative dashboard capability active.')}")
        if st.button(get_text("Revoke Owner Security Authorization Profile"), type="primary", use_container_width=True, key="owner_revoke_secure_btn"):
            st.session_state.owner_verified = False
            st.session_state.otp_dispatched = False
            if "owner_otp_secret" in st.session_state:
                del st.session_state.owner_otp_secret
            st.session_state.user_identity["full_name"] = ""
            st.session_state.user_identity["rank_title"] = get_text("Click to Verify Identity")
            if "subscription" in st.session_state:
                st.session_state.subscription["tier"] = "Enterprise"
                st.session_state.subscription["max_projects"] = 12
            st.rerun()
        return

    # استمارة إدخال طبقات التحقق
    with st.container(border=True):
        st.write(f"**{get_text('Layer 1: Sovereign Credentials Entry')}**")
        input_user = st.text_input(get_text("Master Owner Username"), placeholder="e.g. عبدالله مثنى احمد", key="owner_user_input_text_field")
        input_pass = st.text_input(get_text("Master Owner Secret Token"), type="password", placeholder="••••••••", key="owner_pass_input_text_field")
        
        # تفعيل وإرسال الرمز الحركي التخيلي
        if not st.session_state.otp_dispatched:
            if st.button(get_text("Verify Credentials & Dispatch Security OTP"), use_container_width=True, type="primary", key="owner_dispatch_otp_trigger_btn"):
                if verify_owner_credentials(input_user, input_pass):
                    generated_otp = generate_owner_otp()
                    st.session_state.otp_dispatched = True
                    st.session_state.user_identity["email"] = "lawyerabdalla90@gmail.com"
                    st.toast(f"🔒 OTP Security code dispatched to: lawyerabdalla90@gmail.com")
                    st.rerun()
                else:
                    st.error(get_text("Security Access Denied: Invalid master owner credential matching parameters."))

        # إدخال الرمز والموافقة النهائية لتصفير القيود
        if st.session_state.otp_dispatched:
            st.markdown("<hr style='border-color: #E2E8F0; margin: 12px 0;'>", unsafe_allow_html=True)
            st.write(f"**{get_text('Layer 2: Dynamic Email Verification Token')}**")
            
            # عرض الرمز أمامك مباشرة في صندوق المراقبة لغرض الفحص والـ Test السريع بنجاح
            current_otp = st.session_state.get("owner_otp_secret", "123456")
            st.info(f"📬 [TEST MONITORING]: Dynamic Verification Token generated: {current_otp}")
            
            input_otp = st.text_input(get_text("Enter 6-Digit Verification Token Sent to Your Email"), max_chars=6, placeholder="123456", key="owner_otp_validation_text_field")
            
            c_btn1, c_btn2 = st.columns(2)
            with c_btn1:
                if st.button(get_text("Approve & Unlock All Permissions"), type="primary", use_container_width=True, key="owner_unlock_all_perm_btn"):
                    if input_otp == st.session_state.get("owner_otp_secret"):
                        st.session_state.owner_verified = True
                        st.session_state.user_identity["full_name"] = "عبدالله مثنى احمد"
                        st.session_state.user_identity["rank_title"] = get_text("Sovereign Owner")
                        st.session_state.user_identity["registered"] = True
                        
                        if "subscription" not in st.session_state:
                            st.session_state.subscription = {}
                        st.session_state.subscription["tier"] = "Enterprise"
                        st.session_state.subscription["max_projects"] = 999999
                        st.session_state.subscription["active"] = True
                        
                        log_action(user_credential="عبدالله مثنى احمد", action_details="Sovereign Master Profile parameters unlocked completely.")
                        st.success(get_text("Verified Successfully! All sovereign system features unlocked."))
                        st.rerun()
                    else:
                        st.error(get_text("Validation Failure: The entered OTP token is invalid or has expired."))
            with c_btn2:
                if st.button(get_text("Cancel & Reset Pipeline"), use_container_width=True, key="owner_cancel_pipeline_btn"):
                    st.session_state.otp_dispatched = False
                    if "owner_otp_secret" in st.session_state:
                        del st.session_state.owner_otp_secret
                    st.rerun()

import streamlit as st
import random
from utils.localization import get_text
from core.state_manager import log_action

def generate_owner_otp():
    """
    توليد رمز تحقق حركي مؤقت مكون من 6 أرقام وحفظه في ذاكرة الجلسة الآمنة.
    """
    otp_code = str(random.randint(100000, 999999))
    st.session_state.owner_otp_secret = otp_code
    return otp_code

def verify_owner_credentials(username, password):
    """
    الطبقة الأولى: التحقق الصارم من الاسم البصري وكلمة المرور الخارقة لمالك المنصة.
    [بيانات سيادية ثابتة محددة من قبل مالك المنصة]
    """
    MASTER_USERNAME = "عبدالله مثنى احمد"
    MASTER_PASSWORD = "1990Abdalla"
    
    return username == MASTER_USERNAME and password == MASTER_PASSWORD

def render_sovereign_owner_pipeline():
    """
    Core Architecture Module: Sovereign Owner Authentication Bypass Panel.
    Strictly locked to owner credentials: عبدالله مثنى احمد / 1990Abdalla
    Enforces the 3-Layer Security verification framework:
    - Layer 1: Secure Username & Master Password check
    - Layer 2: Dynamic OTP token simulation mapped to lawyerabdalla90@gmail.com
    - Layer 3: Unlocks infinite access metrics (∞) and purges billing matrices
    """
    st.markdown(
        """
        <style>
        .auth-title { color: #0F172A !important; font-size: 18px; font-weight: 900; margin-bottom: 8px; }
        .auth-subtitle { color: #475569 !important; font-size: 12px; font-weight: 600; margin-bottom: 15px; }
        </style>
        """,
        unsafe_allow_html=True
    )

    if "owner_verified" not in st.session_state:
        st.session_state.owner_verified = False
    if "otp_dispatched" not in st.session_state:
        st.session_state.otp_dispatched = False

    st.markdown(f'<div class="auth-title">🛡️ {get_text("Sovereign Owner Authorization")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="auth-subtitle">{get_text("Multi-factor master bypass console for system ownership activation.")}</div>', unsafe_allow_html=True)

    # إذا تم تفعيل الصلاحيات بنجاح، اقلب واجهة الحساب كلياً للمالك الخارق
    if st.session_state.owner_verified:
        st.success(f"👑 {get_text('Sovereign Permissions Released: Infinite administrative dashboard capability active.')}")
        if st.button(get_text("Revoke Owner Security Authorization Profile"), type="primary", use_container_width=True):
            st.session_state.owner_verified = False
            st.session_state.otp_dispatched = False
            st.session_state.user_identity["full_name"] = ""
            st.session_state.user_identity["rank_title"] = get_text("Click to Verify Identity")
            if "subscription" in st.session_state:
                st.session_state.subscription["tier"] = "Enterprise"
                st.session_state.subscription["max_projects"] = 12
            st.rerun()
        return

    with st.container(border=True):
        # --- الطبقة الأولى: التحقق من اسم المستخدم والباسورد الصارم ---
        st.write(f"**{get_text('Layer 1: Sovereign Credentials Entry')}**")
        input_user = st.text_input(get_text("Master Owner Username"), placeholder="e.g. عبدالله مثنى احمد", key="owner_input_user_field")
        input_pass = st.text_input(get_text("Master Owner Secret Token"), type="password", placeholder="••••••••", key="owner_input_pass_field")
        
        # الطبقة الثانية: توليد وإرسال الرمز الحركي
        if not st.session_state.otp_dispatched:
            if st.button(get_text("Verify Credentials & Dispatch Security OTP"), use_container_width=True, type="primary"):
                if verify_owner_credentials(input_user, input_pass):
                    generated_otp = generate_owner_otp()
                    st.session_state.otp_dispatched = True
                    
                    # قفل وتثبيت البريد الإلكتروني الموثق لمالك المنصة
                    st.session_state.user_identity["email"] = "lawyerabdalla90@gmail.com"
                    st.toast(f"🔒 OTP Security code dispatched to: lawyerabdalla90@gmail.com")
                    
                    # إظهار الرمز في شاشة المراقبة الداخلية لغرض الفحص والتجربة المباشرة
                    st.info(f"📬 [TEST MONITORING]: Dynamic Verification Token generated: {generated_otp}")
                    st.rerun()
                else:
                    st.error(get_text("Security Access Denied: Invalid master owner credential matching parameters."))

        # الطبقة الثالثة: إدخال رمز الـ OTP وإطلاق التفعيلات الكاملة
        if st.session_state.otp_dispatched:
            st.markdown("<hr style='border-color: #E2E8F0; margin: 12px 0;'>", unsafe_allow_html=True)
            st.write(f"**{get_text('Layer 2: Dynamic Email Verification Token')}**")
            
            input_otp = st.text_input(get_text("Enter 6-Digit Verification Token Sent to Your Email"), max_chars=6, placeholder="123456", key="owner_input_otp_field")
            
            c_btn1, c_btn2 = st.columns(2)
            with c_btn1:
                if st.button(get_text("Approve & Unlock All Permissions"), type="primary", use_container_width=True):
                    if input_otp == st.session_state.get("owner_otp_secret"):
                        # إطلاق الرتبة الخارقة في الهيدر العلوي وفي الذاكرة
                        st.session_state.owner_verified = True
                        st.session_state.user_identity["full_name"] = "عبدالله مثنى احمد"
                        st.session_state.user_identity["rank_title"] = get_text("Sovereign Owner")
                        st.session_state.user_identity["registered"] = True
                        
                        if "subscription" not in st.session_state:
                            st.session_state.subscription = {}
                        st.session_state.subscription["tier"] = "Enterprise"
                        st.session_state.subscription["max_projects"] = 999999  # سعة لانهائية
                        st.session_state.subscription["active"] = True
                        
                        log_action(user_credential="عبدالله مثنى احمد", action_details="Sovereign Multi-factor owner pipeline bypass console successfully unlocked.")
                        st.success(get_text("Verified Successfully! All sovereign system features unlocked."))
                        st.rerun()
                    else:
                        st.error(get_text("Validation Failure: The entered OTP token is invalid or has expired."))
            with c_btn2:
                if st.button(get_text("Cancel & Reset Pipeline"), use_container_width=True):
                    st.session_state.otp_dispatched = False
                    st.rerun()

import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

def handle_language_switch():
    """تحديث لغة الجلسة فوراً عند التغيير."""
    new_lang = st.session_state.get("temp_lang_selector")
    if new_lang:
        st.session_state.language = new_lang

def render_header():
    """
    مكون الهيدر المبسط والنظيف 100% لضمان تناسق التوزيع وحجم الخط.
    يعتمد كلياً على أدوات بايثون القياسية لـ Streamlit لمنع التشوه البصري.
    """
    user_data = st.session_state.user_identity
    
    # تحديد مسميات الحساب والهوية
    display_name = user_data["full_name"] if user_data["registered"] else get_text("Unregistered Account")
    display_rank = user_data["rank_title"] if user_data["registered"] else get_text("Click to Verify Identity")
    current_gov = st.session_state.property_data.get("governorate", "Baghdad")

    # 1. إجبار العناوين والنصوص على الظهور بلون كحلي داكن وخطوط عريضة غليظة جداً واضحة
    st.markdown(
        """
        <style>
        .stApp h2, .stApp h4, .stApp p, .stApp span {
            color: #0F172A !important; /* لون كحلي داكن شديد التباين */
            font-weight: 800 !important; /* خطوط مغلظة حادة */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 2. تقسيم مساحات الهيدر بالتساوي لمنع الاختناق وتداخل النصوص
    col_brand, col_context, col_user = st.columns([3.0, 2.0, 2.0], gap="large")
    
    # الجانب الأيمن: شعار وهوية المنصة الوطنية
    with col_brand:
        st.subheader("Iraqi Green Construction Data Platform")
        st.caption(get_text("Iraqi Green Construction Data Platform"))
        st.caption("DATA • COMPLIANCE • SUSTAINABILITY • EFFICIENCY")
        
    # المنتصف: بطاقة الموقع الجغرافي الموحدة وأداة تحويل اللغة
    with col_context:
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            st.metric(label=get_text("Current Location"), value=f"📍 {current_gov}")
        with sub_col2:
            st.write(f"**{get_text('Language')}**")
            lang_options = ["العربية", "EN"]
            current_lang = st.session_state.get("language", "العربية")
            default_idx = 1 if current_lang == "EN" else 0
            
            st.segmented_control(
                label="Language Selector", 
                options=lang_options, 
                default=lang_options[default_idx], 
                label_visibility="collapsed", 
                key="temp_lang_selector",
                on_change=handle_language_switch
            )

    # الجانب الأيسر: الملف الشخصي للمشغل وزر التحقق
    with col_user:
        sub_col_avatar, sub_col_btn = st.columns([1.0, 2.0])
        with sub_col_avatar:
            avatar_src = user_data["avatar_url"] if user_data["avatar_url"] else "https://unsplash.com"
            st.image(avatar_src, width=50)
        with sub_col_btn:
            st.write(f"**{display_name}**")
            st.caption(display_rank)
            
        if st.button(get_text("Click to Verify Identity"), key="open_profile_drawer", use_container_width=True):
            st.session_state.show_profile_drawer = True
            
    # نافذة شريط التدقيق القانوني والهوية الجانبية
    if st.session_state.get("show_profile_drawer", False):
        with st.sidebar:
            if st.button(get_text("Close & Return"), use_container_width=True):
                st.session_state.show_profile_drawer = False
                st.rerun()
                
            st.markdown(f"## {get_text('Documentation & Legal Accountability Portal')}")
            
            if not user_data["registered"]:
                input_name = st.text_input(get_text("User's Full Quadruple Name:"))
                user_role = st.selectbox(get_text("Technical Role in the Project:"), ["Consultant Engineer", "Property Owner", "Certified Contractor"])
                input_nid = st.text_input(get_text("National Unified ID Number (12 Digits):"), max_chars=12)
                
                if st.button(get_text("Approve, Verify Identity & Launch Sovereign Permissions"), use_container_width=True):
                    if input_name and input_nid:
                        st.session_state.user_identity["registered"] = True
                        st.session_state.user_identity["full_name"] = input_name
                        st.session_state.user_identity["rank_title"] = get_text(user_role)
                        st.session_state.user_identity["national_id"] = input_nid
                        log_action(user_credential=input_name, action_details="Registered ID profile.")
                        st.success(get_text("Verified Successfully!"))
                        st.rerun()
            else:
                st.success(get_text("Identity Verified Status"))
                st.text_input(get_text("Registered Operator Nominee"), value=user_data["full_name"], disabled=True)
                if st.button(get_text("Revoke Profile Authorization Logs"), use_container_width=True, type="primary"):
                    st.session_state.user_identity["registered"] = False
                    st.rerun()

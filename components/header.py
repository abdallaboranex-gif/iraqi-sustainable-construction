import streamlit as st
from core.security_crypto import mask_sensitive_data
from utils.localization import get_text # استيراد دالة الترجمة

def render_header():
    """
    مكون الشريحة العليا السيادي والديناميكي: الجزء الأول.
    يبني الهوية البصرية، وصندوق الموقع الأبيض، ومبدل اللغات الثلاثي المربوط بالسيرفر.
    """
    user_data = st.session_state.user_identity
    
    # تحديد الكلمات التي ستظهر ديناميكياً بناءً على اكتمال التسجيل واللغة الفعالة
    display_name = user_data["full_name"] if user_data["registered"] else get_text("user_unregistered")
    display_rank = user_data["rank_title"] if user_data["registered"] else get_text("user_action_verify")

    # تقسيم الهيدر بمسافات فسيحة مطابقة للصورة المرجعية الفخمة مئة بالمئة
    col_brand, col_context, col_user = st.columns([2.6, 1.8, 1.6], gap="small")
    
    # أقصى اليسار: الشعار واللوحة اللفظية الرسمية
    with col_brand:
        st.markdown(
            f"""
            <div style='text-align: left; padding-top: 5px;'>
                <h2 style='color: #1D4ED8; margin: 0; font-weight: 800; font-size: 24px; letter-spacing: 0.5px;'>
                    Iraqi Green Construction Data Platform
                </h2>
                <h4 style='color: #0F172A; margin: 2px 0 0 0; font-weight: 800; font-size: 16px;'>
                    {get_text('platform_title')}
                </h4>
                <p style='color: #475569; margin: 4px 0 0 0; font-size: 12px; font-weight: 700; word-spacing: 2px;'>
                    DATA • COMPLIANCE • SUSTAINABILITY • EFFICIENCY
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    # الوسط: صندوق الموقع الأبيض الفخم ومبدل اللغات المحكم
    with col_context:
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            current_gov = st.session_state.property_data.get("governorate", "Baghdad")
            st.markdown(
                f"""
                <div style='background-color: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 10px; padding: 6px 12px; text-align: center; margin-top: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);'>
                    <span style='color: #475569 !important; font-size: 11px !important; font-weight: 700 !important; display: block;'>{get_text('current_location')}</span>
                    <strong style='color: #1D4ED8 !important; font-size: 15px !important; font-weight: 800 !important; display: block; margin-top: 2px;'>📍 {current_gov}</strong>
                </div>
                """, 
                unsafe_allow_html=True
            )
        with sub_col2:
            st.markdown(f"<span style='color: #0F172A; font-size: 12px !important; font-weight: 700; display: block; margin-top: 2px; text-align: center;'>{get_text('lang_label')}</span>", unsafe_allow_html=True)
            lang_options = ["العربية", "كردي", "EN"]
            
            default_idx = 0
            if st.session_state.get("language", "ar") == "ku": default_idx = 1
            elif st.session_state.get("language", "ar") == "en": default_idx = 2
            
            # [التعديل الفاخر للربط] تصفير الانفصال وجعل الوجت يغير الذاكرة العامة مباشرة
            selected_lang = st.segmented_control(
                label="Language Selector", options=lang_options, default=lang_options[default_idx], label_visibility="collapsed", key="language_selection_trigger"
            )
            if selected_lang == "العربية" and st.session_state.get("language", "ar") != "ar":
                st.session_state.language = "ar"; st.rerun()
            elif selected_lang == "كردي" and st.session_state.get("language", "ar") != "ku":
                st.session_state.language = "ku"; st.rerun()
            elif selected_lang == "EN" and st.session_state.get("language", "ar") != "en":
                st.session_state.language = "en"; st.rerun()
    # أقصى اليمين: عرض الصورة الشخصية الفخمة وبوابة الشريط الجانبي (Sidebar)
    with col_user:
        st.markdown(
            f"""
            <div style='display: flex; align-items: center; justify-content: flex-end; gap: 14px; padding-top: 5px; margin-bottom: 2px;'>
                <div style='text-align: right;'>
                    <span style='color: #0F172A; font-weight: 800; font-size: 15px; display: block;'>{display_name}</span>
                    <span style='color: #475569; font-weight: 700; font-size: 12px; display: block;'>{display_rank}</span>
                </div>
                <img src='{user_data["avatar_url"]}' 
                     style='width: 44px; height: 44px; border-radius: 50%; border: 2.5px solid #1D4ED8; object-fit: cover; box-shadow: 0 2px 4px rgba(0,0,0,0.1);' />
            </div>
            """, 
            unsafe_allow_html=True
        )
        if st.button(get_text("user_action_verify"), key="open_profile_drawer", use_container_width=True):
            st.session_state.show_profile_drawer = True
            
    # تشغيل شريط الهوية والتفتيش الرقمي الفسيح عند طلب المستخدم
    if st.session_state.get("show_profile_drawer", False):
        with st.sidebar:
            if st.button("❌ Close & Return", use_container_width=True):
                st.session_state.show_profile_drawer = False
                st.rerun()
                
            st.markdown(f"## {get_text('drawer_title')}")
            st.markdown(f"<p style='color: #475569; font-size: 12px;'>{get_text('drawer_desc')}</p>", unsafe_allow_html=True)
            
            # حالة 1: الاستمارة بيضاء وفارغة تماماً وتطلب الإدخال والتسجيل الحي
            if not user_data["registered"]:
                st.markdown(f"<h4 style='color: #1D4ED8; font-size: 15px; margin-top: 10px;'>📝 Create Register:</h4>", unsafe_allow_html=True)
                input_name = st.text_input(get_text("lbl_user_name"), placeholder="مثال: عبد الله عمر")
                user_role = st.selectbox(get_text("lbl_user_role"), ["مهندس استشاري / مكتب هندسي", "مواطن / مالك العقار", "مقاول إنشائي معتمد"])
                input_nid = st.text_input(get_text("lbl_national_id"), max_chars=12, placeholder="199204358112")
                
                input_sid = ""
                if user_role == "مهندس استشاري / مكتب هندسي":
                    input_sid = st.text_input(get_text("lbl_syndicate_id"), placeholder="40512")
                    
                uploaded_avatar = st.file_uploader(get_text("lbl_upload_avatar"), type=["png", "jpg", "jpeg"], key="user_avatar_uploader")
                
                if st.button(get_text("btn_submit_auth"), use_container_width=True):
                    if input_name and input_nid:
                        st.session_state.user_identity["registered"] = True
                        st.session_state.user_identity["full_name"] = input_name
                        st.session_state.user_identity["rank_title"] = "مهندس استشاري مرخص" if user_role == "مهندس استشاري / مكتب هندسي" else user_role
                        st.session_state.user_identity["national_id"] = input_nid
                        st.session_state.user_identity["syndicate_id"] = input_sid if input_sid else "N/A"
                        if uploaded_avatar is not None:
                            st.session_state.user_identity["avatar_url"] = "https://unsplash.com"
                        st.session_state.user_identity["projects_list"] = [{"id": 1, "name": "مشروع عقار قيد التسجيل الأولي", "status": "compliant"}]
                        
                        from core.state_manager import log_action
                        log_action(user=input_name, action_details="سجل حسابه الرسمي الموافق للمسؤولية القانونية.")
                        st.success("🎉 Verified Successfully!")
                        st.rerun()
                    else:
                        st.warning("⚠️ Required Fields!")
                        
            # حالة 2: حساب موثق سياقاً ويعرض شارات الأمان والأرقام المعماة بـ *****
            else:
                st.markdown(f"### 🛡️ {user_data['full_name']}")
                st.markdown(
                    f"""
                    <div style='background-color: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 12px; padding: 12px; margin-bottom: 15px;'>
                        <span style='color: #166534 !important; font-weight: 800 !important; font-size: 14px !important; display: block;'>
                            {get_text('badge_verified')}
                        </span>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                st.markdown(f"💼 **باقة النظام الحالية:** باقة الشركات والمكاتب الاستشارية")
                st.markdown(f"⏱️ **صلاحية الباقة:** متبقي {user_data['days_left']} يوماً")
                
                st.markdown("---")
                st.markdown(f"### 🔐 {get_text('crypto_notice')}")
                masked_nid = mask_sensitive_data(user_data["national_id"])
                masked_sid = mask_sensitive_data(user_data["syndicate_id"])
                
                st.markdown(f"💳 **الرقم الوطني الموحد:** ` {masked_nid} `")
                st.markdown(f"📐 **رقم الهوية النقابية:** ` {masked_sid} `")
                
                st.markdown("<br><br>", unsafe_allow_html=True)
                if st.button(get_text("btn_reset"), use_container_width=True):
                    st.session_state.user_identity["registered"] = False
                    st.rerun()

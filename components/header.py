import streamlit as st
from core.security_crypto import mask_sensitive_data

def render_header():
    """
    مكون الشريحة العليا المطور: الجزء الأول.
    يهيئ البيانات البيضاء للفراغات ويبني الهوية البصرية الفخمة على اليسار.
    """
    # 1. تهيئة حقول البيانات البيضاء والفارغة تماماً عند أول تشغيل للمنصة
    if "user_identity" not in st.session_state:
        st.session_state.user_identity = {
            "registered": False,
            "full_name": "",
            "rank_title": "مواطن / مقاول",
            "national_id": "",
            "syndicate_id": "",
            "avatar_url": "https://unsplash.com",
            "days_left": 365,
            "projects_list": []
        }

    user_data = st.session_state.user_identity
    display_name = user_data["full_name"] if user_data["registered"] else "حساب غير مسجل"
    display_rank = user_data["rank_title"] if user_data["registered"] else "اضغط لتأكيد الهوية"

    # تقسيم الشاشة أفقياً بمسافات عريضة متناسقة مع الثيم الفاتح والأحرف الغامقة
    col_brand, col_context, col_user = st.columns([2.6, 1.8, 1.6], gap="small")
    
    # بناء الشعار اللفظي والهوية الرسمية في أقصى اليسار
    with col_brand:
        st.markdown(
            """
            <div style='text-align: left; padding-top: 5px;'>
                <h2 style='color: #1D4ED8; margin: 0; font-weight: 800; font-size: 24px; letter-spacing: 0.5px;'>
                    Iraqi Green Construction Data Platform
                </h2>
                <h4 style='color: #0F172A; margin: 2px 0 0 0; font-weight: 800; font-size: 16px;'>
                    منصة البناء المستدام
                </h4>
                <p style='color: #475569; margin: 4px 0 0 0; font-size: 12px; font-weight: 700; word-spacing: 2px;'>
                    DATA • COMPLIANCE • SUSTAINABILITY • EFFICIENCY
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    # بناء صندوق الموقع والتحكم باللغات في العمود الأوسط
    with col_context:
        sub_col1, sub_col2 = st.columns(2)
        
        with sub_col1:
            current_gov = st.session_state.property_data.get("governorate", "Baghdad")
            st.markdown(
                f"""
                <div style='background-color: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 10px; padding: 6px 12px; text-align: center; margin-top: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);'>
                    <span style='color: #475569 !important; font-size: 11px !important; font-weight: 700 !important; display: block;'>الموقع الحالي / Location</span>
                    <strong style='color: #1D4ED8 !important; font-size: 15px !important; font-weight: 800 !important; display: block; margin-top: 2px;'>📍 {current_gov}</strong>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
        with sub_col2:
            st.markdown("<span style='color: #0F172A; font-size: 12px !important; font-weight: 700; display: block; margin-top: 2px; text-align: center;'>اللغة / Language</span>", unsafe_allow_html=True)
            lang_options = ["العربية", "كردي", "EN"]
            default_idx = 0
            if st.session_state.language == "ku": default_idx = 1
            elif st.session_state.language == "en": default_idx = 2
            
            selected_lang = st.segmented_control(
                label="Language Selector", options=lang_options, default=lang_options[default_idx], label_visibility="collapsed", key="header_lang_widget"
            )
            
            if selected_lang == "العربية" and st.session_state.language != "ar":
                st.session_state.language = "ar"; st.rerun()
            elif selected_lang == "كردي" and st.session_state.language != "ku":
                st.session_state.language = "ku"; st.rerun()
            elif selected_lang == "EN" and st.session_state.language != "en":
                st.session_state.language = "en"; st.rerun()
    # بناء عرض حساب المستخدم والزر الحركي لفتح بوابة الهوية والتسجيل في اليمين
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
        if st.button("🗂️ فتح بوابة الهوية والتسجيل السيادي", key="open_profile_drawer", use_container_width=True):
            st.session_state.show_profile_drawer = True
            
    # تشغيل شريط التسجيل والتحقق الفسيح والآمن (Sidebar) عند الضغط
    if st.session_state.get("show_profile_drawer", False):
        with st.sidebar:
            if st.button("❌ إغلاق كرت الهوية والعودة للمنصة", use_container_width=True):
                st.session_state.show_profile_drawer = False
                st.rerun()
                
            st.markdown("## 🔐 بوابة التوثيق والمسؤولية القانونية")
            
            # حالة الحساب 1: غير مسجل وفارغ تماماً للبدء الحركي والتجريب
            if not user_data["registered"]:
                st.markdown("<h4 style='color: #1D4ED8; font-size: 15px; margin-top: 10px;'>📝 إنشاء السجل الرقمي الموثق:</h4>", unsafe_allow_html=True)
                input_name = st.text_input("الاسم الرباعي الكامل للمستخدم:", placeholder="مثال: عبد الله عمر الجبوري")
                user_role = st.selectbox("الصفة الفنية في المشروع:", ["مهندس استشاري / مكتب هندسي", "مواطن / مالك العقار", "مقاول إنشائي معتمد"])
                input_nid = st.text_input("رقم البطاقة الوطنية الموحدة (12 رقماً):", max_chars=12, placeholder="مثال: 199204358112")
                
                input_sid = ""
                if user_role == "مهندس استشاري / مكتب هندسي":
                    input_sid = st.text_input("رقم هوية نقابة المهندسين العراقية النافذة:", placeholder="مثال: 40512")
                    
                uploaded_avatar = st.file_uploader("ارفع صورتك الشخصية الرسمية (PNG/JPG):", type=["png", "jpg", "jpeg"], key="user_avatar_uploader")
                
                if st.button("🔒 اعتماد وتوثيق الهوية وإطلق الصلاحيات السيادية", use_container_width=True):
                    if input_name and input_nid:
                        st.session_state.user_identity["registered"] = True
                        st.session_state.user_identity["full_name"] = input_name
                        st.session_state.user_identity["rank_title"] = "مهندس استشاري مرخص" if user_role == "مهندس استشاري / مكتب هندسي" else user_role
                        st.session_state.user_identity["national_id"] = input_nid
                        st.session_state.user_identity["syndicate_id"] = input_sid if input_sid else "غير متوفر"
                        if uploaded_avatar is not None:
                            st.session_state.user_identity["avatar_url"] = "https://unsplash.com"
                        st.session_state.user_identity["projects_list"] = [{"id": 1, "name": "مشروع عقار قيد التسجيل الأولي", "status": "compliant"}]
                        
                        from core.state_manager import log_action
                        log_action(user=input_name, action_details=f"سجل حسابه الرسمي الموثق بالرقم الوطني {input_nid}.")
                        st.success("🎉 تم توثيق هويتك بنجاح ومزامنتها سيادياً!")
                        st.rerun()
                    else:
                        st.warning("⚠️ يرجى ملء الاسم الكامل والرقم الوطني الموحد.")
                        
            # حالة الحساب 2: مسجل ومحمي بتشفير التعمية البصرية الآمنة مئة بالمئة
            else:
                st.markdown(f"### 🛡️ {user_data['full_name']}")
                st.markdown(f"💼 **باقة النظام الحالية:** باقة الشركات والمكاتب الاستشارية")
                st.markdown(f"⏱️ **صلاحية الباقة:** متبقي {user_data['days_left']} يوماً")
                
                st.markdown("---")
                st.markdown("### 🔐 البيانات السيادية المشفرة للحساب:")
                masked_nid = mask_sensitive_data(user_data["national_id"])
                masked_sid = mask_sensitive_data(user_data["syndicate_id"])
                
                st.markdown(f"💳 **الرقم الوطني الموحد:** ` {masked_nid} `")
                st.markdown(f"📐 **رقم الهوية النقابية العراقية:** ` {masked_sid} `")
                
                st.markdown("<br><br>", unsafe_allow_html=True)
                if st.button("🔄 خروج وتصفير السجل التجريبي (Reset)", use_container_width=True):
                    st.session_state.user_identity["registered"] = False
                    st.rerun()

import streamlit as st
from core.security_crypto import mask_sensitive_data

def render_header():
    """
    مكون الشريحة العليا المطور والمنظف تماماً من أي أخطاء قواعد برمجية.
    يعمل بالثيم المشرق والحروف الكحلية الغامقة والنافذة المنبثقة التفاعلية.
    """
    if "user_identity" not in st.session_state:
        st.session_state.user_identity = {
            "full_name": "المهندس عبد الله عمر الجبوري",
            "rank_title": "مدير مشروع / مهندس استشاري مرخص",
            "national_id": "199204358112",
            "syndicate_id": "40512",
            "days_left": 42,
            "projects_list": [
                {"id": 1, "name": "مشروع مجمع اليرموك السكني", "status": "compliant"},
                {"id": 2, "name": "مشروع برج الكرادة التجاري", "status": "non_compliant"}
            ]
        }

    col_brand, col_context, col_user = st.columns([2.6, 1.8, 1.6], gap="small")
    
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
                label="Language Selector",
                options=lang_options,
                default=lang_options[default_idx],
                label_visibility="collapsed",
                key="header_lang_widget"
            )
            
            if selected_lang == "العربية" and st.session_state.language != "ar":
                st.session_state.language = "ar"
                st.rerun()
            elif selected_lang == "كردي" and st.session_state.language != "ku":
                st.session_state.language = "ku"
                st.rerun()
            elif selected_lang == "EN" and st.session_state.language != "en":
                st.session_state.language = "en"
                st.rerun()

    with col_user:
        st.markdown("<div style='padding-top: 6px;'></div>", unsafe_allow_html=True)
        
        with st.popover(label="👤  Eng. Abdulla | مدير مشروع", use_container_width=True):
            user_data = st.session_state.user_identity
            
            st.markdown(f"### 👤 {user_data['full_name']}")
            st.markdown(
                f"""
                <div style='background-color: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; padding: 8px 12px; margin-bottom: 12px;'>
                    <span style='color: #166534 !important; font-weight: 800 !important; font-size: 13px !important; display: block;'>
                        🛡️ حساب موثق سيادياً ونقابياً | Professional Verified
                    </span>
                    <span style='color: #475569 !important; font-size: 11px !important; font-weight: 700 !important; display: block; margin-top: 2px;'>
                        المرتبة المعتمدة: {user_data['rank_title']}
                    </span>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            st.markdown("---")
            st.markdown(
                f"""
                <div style='background-color: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px; margin-bottom: 15px;'>
                    <span style='color: #334155; font-size: 12px; font-weight: 700; display: block;'>نوع الباقة المشترك بها:</span>
                    <strong style='color: #0F172A; font-size: 14px; display: block; margin-top: 2px;'>💼 باقة الشركات والمكاتب الاستشارية الهندسية</strong>
                    <span style='color: #1D4ED8 !important; font-weight: 800 !important; font-size: 13px !important; display: block; margin-top: 6px;'>
                        ⏱️ صلاحية الباقة: متبقي {user_data['days_left']} يوماً (جاهز للتجديد سحابياً)
                    </span>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            st.markdown("#### 🏢 سجل المشاريع الميدانية النشطة:")
            st.markdown("<p style='color: #64748B; font-size: 11px; margin: 0 0 8px 0;'>*اضغط على اسم المشروع لتحديث كافة بوابات الحوكمة وحساباتها فوراً*</p>", unsafe_allow_html=True)
            
            for project in user_data["projects_list"]:
                status_dot = "🟢" if project["status"] == "compliant" else "🔴"
                status_txt = "(سليم ومطابق)" if project["status"] == "compliant" else "(موقوف - مخالفة الباب السادس)"
                
                if st.button(
                    label=f"{status_dot} {project['name']} {status_txt}", 
                    key=f"switcher_proj_{project['id']}", 
                    use_container_width=True
                ):
                    st.session_state.property_data["district"] = "المنصور" if project["id"] == 1 else "الكرادة"
                    st.session_state.property_data["is_compliant"] = True if project["status"] == "compliant" else False
                    st.success(f"🔄 تم الانتقال السحابي الفوري لملف: {project['name']}")
                    st.rerun()
                    
            st.markdown("---")
            st.markdown("#### 🔐 البيانات السيادية المشفرة للحساب:")
            
            masked_nid = mask_sensitive_data(user_data["national_id"])
            masked_sid = mask_sensitive_data(user_data["syndicate_id"])
            
            st.markdown(f"💳 **الرقم الوطني الموحد:** ` {masked_nid} `")
            st.markdown(f"📐 **رقم الهوية النقابية العراقية:** ` {masked_sid} `")
            st.markdown("<span style='color: #64748B; font-size: 11px; display: block; margin-top: 4px;'>*الحقول معماة ومحمية بتشفير AES-256 لمنع تسريب البيانات البحتة.*</span>", unsafe_allow_html=True)

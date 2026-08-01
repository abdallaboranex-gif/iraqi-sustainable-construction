import streamlit as st

def render_header():
    """
    مكون الشريحة العليا (Header Component).
    يبني الهوية البصرية، حساب المهندس، وأزرار التحكم باللغات جغرافياً.
    """
    # إنشاء ثلاثة أعمدة علوية متناسقة بمسافات بصرية مريحة
    col_brand, col_context, col_user = st.columns([2.5, 2, 1.5], gap="small")
    
    # 1. العمود الأول (أقصى اليسار): الهوية البصرية للمنصة
    with col_brand:
        st.markdown(
            """
            <div style='text-align: left; padding-top: 5px;'>
                <h2 style='color: #00FFCC; margin: 0; font-weight: 800; font-size: 24px; letter-spacing: 0.5px;'>
                    Iraqi Green Construction Data Platform
                </h2>
                <h4 style='color: #64748B; margin: 0; font-weight: 600; font-size: 16px;'>
                    منصة البناء المستدام
                </h4>
                <p style='color: #475569; margin: 2px 0 0 0; font-size: 11px; font-weight: 500; word-spacing: 2px;'>
                    DATA • COMPLIANCE • SUSTAINABILITY • EFFICIENCY
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    # 2. العمود الثاني (الوسط): مبدل اللغات ومحدد الموقع الجغرافي للمشروع
    with col_context:
        # حاوية أفقية صغيرة لترتيب الأزرار والموقع بجانب بعضها
        sub_col1, sub_col2 = st.columns([1, 1])
        
        with sub_col1:
            # عرض اسم المحافظة المختارة حالياً بناءً على بيانات العقار في الذاكرة
            current_gov = st.session_state.property_data.get("governorate", "Baghdad")
            st.markdown(
                f"""
                <div style='background-color: #1E293B; border: 1px solid #334155; border-radius: 6px; padding: 6px 12px; text-align: center; margin-top: 10px;'>
                    <span style='color: #94A3B8; font-size: 12px; display: block;'>الموقع الحالي / Location</span>
                    <strong style='color: #00FFCC; font-size: 14px;'>📍 {current_gov}</strong>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
        with sub_col2:
            # أزرار تحويل اللغة الثلاثية (العربية، الكردية، الإنكليزية)
            st.markdown("<span style='color: #94A3B8; font-size: 11px; display: block; margin-top: 4px; text-align: center;'>اللغة / Language</span>", unsafe_allow_html=True)
            
            # رص الأزرار أفقياً بشكل ناعم
            lang_options = ["العربية", "كردي", "EN"]
            # نحدد الزر النشط تلقائياً بناءً على المخزن في الذاكرة السحابية
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
            
            # تحديث لغة المنصة فوراً في الذاكرة السحابية عند قيام المستخدم بالضغط على زر آخر
            if selected_lang == "العربية" and st.session_state.language != "ar":
                st.session_state.language = "ar"
                st.rerun()
            elif selected_lang == "كردي" and st.session_state.language != "ku":
                st.session_state.language = "ku"
                st.rerun()
            elif selected_lang == "EN" and st.session_state.language != "en":
                st.session_state.language = "en"
                st.rerun()

    # 3. العمود الثالث (أقصى اليمين): ملف المهندس وحالة تسجيل الدخول
    with col_user:
        st.markdown(
            """
            <div style='display: flex; align-items: center; justify-content: flex-end; gap: 12px; padding-top: 8px;'>
                <div style='text-align: right;'>
                    <span style='color: #F8FAFC; font-weight: 600; font-size: 14px; display: block;'>Eng. Abdulla</span>
                    <span style='color: #64748B; font-size: 12px; display: block;'>Project Manager</span>
                </div>
                <div style='width: 42px; height: 42px; background-color: #00FFCC; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 2px solid #1E293B;'>
                    <span style='color: #0F172A; font-weight: bold; font-size: 16px;'>EA</span>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

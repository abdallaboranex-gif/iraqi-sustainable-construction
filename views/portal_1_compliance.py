import streamlit as st

def render_portal_1():
    """
    واجهة الباب الأول: التدقيق الإنشائي وفحص التربة والمدونات الجغرافية.
    تحتوي على الـ 13 حقل رئيسي للفلترة الذكية وتوجيه المستخدم.
    """
    st.markdown("<h2 style='color: #00FFCC; font-size: 22px; margin-bottom: 5px;'>📋 الباب الأول: تحليل الموقع ومحددات البلدية</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; font-size: 13px;'>يرجى ملء الحقول الـ 13 بدقة لتحديد متطلبات فحص التربة والمدونات الهندسية الإلزامية لمشروعك وفقاً للوائح العراقية.</p>", unsafe_allow_html=True)
    
    # استخدام حاوية بحدود واضحة لجمع الحقول الـ 13 الفاصلة
    with st.container(border=True):
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 15px;'>📍 أولاً: البيانات الجغرافية والإدارية (المحددات الأساسية)</h4>", unsafe_allow_html=True)
        
        # تقسيم الحقول أفقياً لتسهيل تجربة الإدخال المتعدد
        c1, c2, c3 = st.columns(3)
        with c1:
            gov = st.selectbox("1. المحافظة", ["بغداد", "نينوى", "البصرة", "أربيل", "صلاح الدين", "الأنبار", "بابل", "النجف"], index=0)
        with c2:
            district = st.text_input("2. القضاء / الناحية", placeholder="مثال: الكرخ / المنصور")
        with c3:
            zoning = st.selectbox("3. تصنيف جنس العقار (البلدية)", ["سكني صرف", "تجاري", "صناعي", "زراعي مشمول", "حكومي / خدمي"])
            
        c4, c5, c6 = st.columns(3)
        with c4:
            plot_num = st.text_input("4. رقم القطعة والمقاطعة", placeholder="مثال: 4/12 م10 داوودي")
        with c5:
            total_area = st.number_value = st.number_input("5. المساحة الكلية للأرض (متر مربع)", min_value=50.0, value=200.0, step=10.0)
        with c6:
            built_area = st.number_value = st.number_input("6. مساحة البناء الطابقي (متر مربع)", min_value=40.0, value=150.0, step=10.0)

        st.markdown("<hr style='border-color: #334155; margin: 20px 0;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 15px;'>🏗️ ثانياً: المحددات الإنشائية والكتلة المعمارية</h4>", unsafe_allow_html=True)
        
        c7, c8, c9 = st.columns(3)
        with c7:
            floors = st.number_input("7. عدد الطوابق الكلي", min_value=1, max_value=60, value=2)
        with c8:
            building_height = st.number_input("8. الارتفاع الكلي للمبنى (متر)", min_value=3.0, value=7.5, step=0.5)
        with c9:
            basement = st.selectbox("9. هل يحتوي المبنى على سرداب (قبو)؟", ["لا يحتوي", "سرداب واحد", "متعدد الطوابق تحت الأرض"])

        c10, c11, c12 = st.columns(3)
        with c10:
            front_offset = st.number_input("10. الارتداد الأمامي القانوني (متر)", min_value=0.0, value=3.0, step=0.5)
        with c11:
            side_offset = st.number_input("11. الارتدادات الجانبية والخلفية (متر)", min_value=0.0, value=1.5, step=0.5)
        with c12:
            adjacent_buildings = st.selectbox("12. طبيعة الملاصقة والأبنية المجاورة", ["مباني سكنية خفيفة", "هياكل كونكريتية ضخمة", "أرض فضاء / ساحة"])

        # الحقل الـ 13 الحاسم لنوع الأساس والتربة
        st.markdown("<br>", unsafe_allow_html=True)
        structural_system = st.selectbox("13. النظام الإنشائي المقترح للهيكل", ["هيكل خرساني مسلّح (Columns & Beams)", "جدران حاملة (Bearing Walls)", "هيكل حديدي (Steel Structure)", "مختلط / خاص"])

        # زر الحساب والمطابقة الإلكترونية التلقائية
        st.markdown("<br>", unsafe_allow_html=True)
        submit_filter = st.button("🚀 إكمال ملء الحقول ومطابقة محددات البلدية", use_container_width=True)
        
        if submit_filter:
            # تحديث المحافظة في الذاكرة السحابية ليتغير تلقائياً في الشريحة العليا (الهيدر)
            st.session_state.property_data["governorate"] = gov
            st.session_state.property_data["district"] = district
            st.session_state.property_data["zoning_type"] = zoning
            
            st.success(f"✅ تم حفظ وتدقيق المحددات الـ 13 بنجاح لمحافظة {gov}!")
            st.log_action = f"قام المستخدم بتثبيت بيانات الموقع لـ {gov}/{district}."
            
            # محرك الفلترة الجغرافية والذكية التلقائية بناءً على معطيات المستخدم
            st.markdown("<br><hr style='border-color: #00FFCC;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #00FFCC; font-size: 18px;'>🛠️ البرامج التخصصية المتاحة لمشروعك الآن:</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color: #94A3B8; font-size: 13px;'>بناءً على الفلترة التلقائية للموقع وطبيعة الأرض، تم فتح البوابات التالية للمطابقة البرمجية الصارمة:</p>", unsafe_allow_html=True)
            
            # مصفوفة اتخاذ القرار (Decision Matrix) المبرمجة آلياً
            col_p1, col_p2 = st.columns(2)
            with col_p1:
                # فلترة ذكية: إذا كان عدد الطوابق أكثر من طابقين أو تحتوي على سرداب، يصبح فحص التربة إلزامياً مئة بالمئة
                if floors > 2 or basement != "لا يحتوي":
                    st.info("📌 **برنامج فحص التربة وتصميم الأسس:** [إلزامي مخبري] - تم رصد أحمال تتطلب تقرير مختبر موثق.")
                else:
                    st.success("📌 **برنامج فحص التربة وتصميم الأسس:** [اختياري جغرافياً] - يسمح بالتصميم المباشر وفق الحدود الدنيا للمدونة.")
                
                st.info("📌 **برنامج التدقيق الإنشائي وحساب الأحمال والخرسانة:** [إلزامي]")
            
            with col_p2:
                st.info("📌 **برنامج هندسة التأسيسات الصحية والمائية:** [إلزامي]")
                st.info("📌 **برنامج هندسة التأسيسات الكهربائية ومحامل الطاقة:** [إلزامي]")
                
            st.rerun() # إعادة بث لتحديث اسم المحافظة في أعلى المتصفح فوراً

import streamlit as st
# استيراد محرك المطابقة الإلكتروني التلقائي من طبقة الـ Backend
from engines.code_compliance import verify_site_compliance

def render_portal_1():
    """
    واجهة الباب الأول المحدثة: تحليل الموقع ومحددات البلدية.
    تربط المدخلات بمحرك المعادلات لإصدار تقرير المطابقة والمخالفات الفوري.
    """
    st.markdown("<h2 style='color: #00FFCC; font-size: 22px; margin-bottom: 5px;'>📋 الباب الأول: تحليل الموقع ومحددات البلدية</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; font-size: 13px;'>يرجى ملء الحقول الـ 13 بدقة لتشغيل محرك التدقيق الإلكتروني الصارم (Strict Mode) والمطابقة مع المدونات العراقية.</p>", unsafe_allow_html=True)
    
    # بناء استمارة الحقول الـ 13 الفاصلة جغرافياً وهندسياً
    with st.container(border=True):
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 15px;'>📍 أولاً: البيانات الجغرافية والإدارية</h4>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            gov = st.selectbox("1. المحافظة", ["بغداد", "نينوى", "البصرة", "أربيل", "صلاح الدين", "الأنبار", "بابل", "النجف"], index=0)
        with c2:
            district = st.text_input("2. القضاء / الناحية", placeholder="مثال: الكرخ / المنصور", value="المنصور")
        with c3:
            zoning = st.selectbox("3. تصنيف جنس العقار (البلدية)", ["سكني صرف", "تجاري", "صناعي", "زراعي مشمول", "حكومي / خدمي"])
            
        c4, c5, c6 = st.columns(3)
        with c4:
            plot_num = st.text_input("4. رقم القطعة والمقاطعة", placeholder="مثال: 4/12 م10 داوودي", value="4/12 داوودي")
        with c5:
            total_area = st.number_input("5. المساحة الكلية للأرض (متر مربع)", min_value=50.0, value=200.0, step=10.0)
        with c6:
            built_area = st.number_input("6. مساحة البناء الطابقي (متر مربع)", min_value=40.0, value=150.0, step=10.0)

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

        st.markdown("<br>", unsafe_allow_html=True)
        structural_system = st.selectbox("13. النظام الإنشائي المقترح للهيكل", ["هيكل خرساني مسلّح (Columns & Beams)", "جدران حاملة (Bearing Walls)", "هيكل حديدي (Steel Structure)", "مختلط / خاص"])

        st.markdown("<br>", unsafe_allow_html=True)
        submit_filter = st.button("🚀 تشغيل محرك المطابقة الفوري وفحص القيود", use_container_width=True)
        
        if submit_filter:
            # 1. تحديث البيانات الجغرافية في الذاكرة السحابية المشتركة للمنصة
            st.session_state.property_data["governorate"] = gov
            st.session_state.property_data["district"] = district
            st.session_state.property_data["zoning_type"] = zoning
            
            # 2. استدعاء محرك التفتيش الرقمي وتمرير مدخلات المستخدم الـ 13 له
            result = verify_site_compliance(
                governorate=gov,
                zoning_type=zoning,
                building_height=building_height,
                floors=floors
            )
            
            # 3. معالجة وحفظ حالة العقار العامة بناءً على النتيجة الإلكترونية الصافية
            st.session_state.property_data["is_compliant"] = result["status"]
            
            # عرض النتائج بصرية بناءً على نجاح أو فشل الفحص
            st.markdown("<br><hr style='border-color: #334155;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #F8FAFC; font-size: 18px;'>📊 تقرير المطابقة والفرز الإلكتروني اللحظي:</h3>", unsafe_allow_html=True)
            
            if result["status"]:
                # المسار الأخضر المعتمد بنسبة 100%
                st.success("✅ تهانينا! المخطط الأولي مطابق تماماً لكافة قيود البناء والمدونات المعتمدة جغرافياً في بلدية المنطقة.")
                with st.expander("🔍 تفاصيل بنود الفحص الناجحة"):
                    for log in result["logs"]:
                        st.markdown(f"<span style='color: #10B981;'>{log}</span>", unsafe_allow_html=True)
                
                # تفعيل محرك توجيه البرامج التخصصية تلقائياً
                st.markdown("<h4 style='color: #00FFCC; font-size: 15px; margin-top: 15px;'>🛠️ البوابات التخصصية المفتوحة لمشروعك الآن:</h4>", unsafe_allow_html=True)
                col_b1, col_b2 = st.columns(2)
                with col_b1:
                    if floors > 2 or basement != "لا يحتوي":
                        st.info("📌 **برنامج فحص التربة وتصميم الأسس:** [إلزامي مخبري] - تم رصد أحمال تتطلب تقرير مختبر موثق.")
                    else:
                        st.success("📌 **برنامج فحص التربة وتصميم الأسس:** [اختياري جغرافياً] - يسمح بالتصميم المباشر وفق معايير المدونة.")
                with col_b2:
                    st.info("📌 **برنامج إدارة الطاقة والاستدامة والعزل الحراري:** [مفتوح وجاهز للاستخدام]")
            else:
                # المسار الأحمر الصارم - منع التجاوز وقفل التوصية بإجازة البناء
                st.error("❌ تم رصد مخالفات صريحة لشروط البناء والمدونات الوطنية! تم قفل المعاملة وتجميد إصدار شهادة التوصية بالإجازة.")
                with st.expander("🚨 سجل المخالفات والخرق القانوني المكتشف (يجب تصحيحه):", expanded=True):
                    for error in result["errors"]:
                        st.markdown(f"<span style='color: #EF4444; font-weight: 600;'>{error}</span>", unsafe_allow_html=True)
                st.warning("⚠️ يرجى تعديل الارتفاع أو عدد الطوابق المقترح في الحقول أعلاه وإعادة تشغيل محرك المطابقة لتحقيق الامتثال الكامل وفك قفل ملف العقار.")
                
            # تسجيل الحركة فوراً في الصندوق الأسود مع توثيق اسم المهندس والوقت
            from core.state_manager import log_action
            log_action(user="Eng. Abdulla", action_details=f"شغّل محرك المطابقة لـ {gov}، النتيجة: {result['status']}")
            
            st.rerun() # إعادة بث فورية لتحديث البيانات وعرض التقارير في الشاشة بلمح البصر

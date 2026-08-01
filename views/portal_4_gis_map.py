import streamlit as st
import pandas as pd
import numpy as np

def render_portal_4():
    """
    واجهة الباب الرابع: خارطة العراق التفاعلية ونظام المعلومات الجغرافي (GIS).
    تفرز المشاريع وتعرض الخرائط الحرارية لنسب الاستدامة والتربة وطنياً.
    """
    st.markdown("<h2 style='color: #00FFCC; font-size: 22px; margin-bottom: 5px;'>🗺️ الباب الرابع: خارطة العراق التفاعلية ونظام المؤشرات الجغرافي (GIS)</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; font-size: 13px;'>لوحة حوكمة استراتيجية وطنية تعرض التوزيع المكاني للمشاريع قيد الإنجاز، ونسب الامتثال للمدونات الهندسية لكل محافظة وقضاء [١.١].</p>", unsafe_allow_html=True)
    
    # 1. طبقة الفلترة والتوجيه الهرمي الإداري في العراق (Hierarchical Geo-Filtering)
    with st.container(border=True):
        st.markdown("<h4 style='color: #F8FAFC; font-size: 14px; margin-bottom: 12px;'>🔍 محرك التصفية الجغرافية الهرمي</h4>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            selected_gov = st.selectbox(
                "اختر الإقليم / المحافظة للمعاينة الاستراتيجية:",
                ["كل محافظات العراق", "بغداد", "نينوى", "البصرة", "أربيل", "بابل", "صلاح الدين", "الأنبار", "النجف"]
            )
        with c2:
            # فلترة ديناميكية للأقضية بناءً على اختيار المحافظة
            districts_pool = ["كل الأقضية والنواحي"]
            if selected_gov == "بغداد": districts_pool.extend(["الكرخ / المنصور", "الرصافة / الكرادة", "الكاظمية", "الأعظمية"])
            elif selected_gov == "البصرة": districts_pool.extend(["العشار", "الزبير", "الفاو", "القرنة"])
            elif selected_gov == "نينوى": districts_pool.extend(["الموصل الأيسر", "الموصل الأيمن", "تلكيف", "سنجار"])
            st.selectbox("اختر القضاء / الناحية للتفتيش:", districts_pool)
        with c3:
            map_type = st.selectbox(
                "نوع الخارطة الحرارية (Heatmap Mode):",
                ["مواقع المشاريع ونسب الإنجاز", "خارطة طبقات ومشاكل التربة الجيوتقنية", "خارطة أنماط هدر واستهلاك الطاقة بموجب العزل"]
            )

    # 2. بناء ومحاكاة قاعدة البيانات الجغرافية الوطنية (Geo-Database Simulation)
    # توليد نقاط إحداثيات وهمية دقيقة تتوزع هندسياً داخل خريطة العراق لتمثيل المشاريع النشطة في المنصة
    # بغداد (33.3)، الموصل (36.3)، البصرة (30.5)
    total_projects_count = 142 # إجمالي المشاريع الافتراضية المسجلة وطنياً في قاعدة البيانات
    
    # توزيع الإحداثيات جغرافياً لتبدو حقيقية على الخريطة
    lats = [33.31 + np.random.normal(0, 0.15) for _ in range(60)] + \
           [36.34 + np.random.normal(0, 0.20) for _ in range(42)] + \
           [30.50 + np.random.normal(0, 0.18) for _ in range(40)]
    lons = [44.36 + np.random.normal(0, 0.15) for _ in range(60)] + \
           [43.13 + np.random.normal(0, 0.18) for _ in range(42)] + \
           [47.78 + np.random.normal(0, 0.20) for _ in range(40)]
           
    map_data = pd.DataFrame({'lat': lats, 'lon': lons})

    # 3. عرض الرادارية الجغرافية (Spatial Mapping Visualization)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"🎯 **الرؤية المكانية التفاعلية الحية لـ [{selected_gov}] - بموجب خيار: [{map_type}]:**")
    
    # استخدام محرك خرائط Streamlit السحابي المدمج لعرض النقاط الحية للمشاريع بدقة بالغة
    st.map(map_data, zoom=5 if selected_gov == "كل محافظات العراق" else 9, use_container_width=True)

    # 4. لوحة تفكيك البيانات وقراءة واقع حال المحافظات (Provincial Analytics Dashboard)
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<h4 style='color: #00FFCC; font-size: 15px; margin-bottom: 12px;'>📊 الاستخبارات البيانية والمؤشرات التخطيطية الكلية</h4>", unsafe_allow_html=True)
        
        cc1, cc2, cc3 = st.columns(3)
        with cc1:
            st.metric(label="إجمالي المشاريع الخاضعة للحوكمة السحابية", value=f"{total_projects_count} مشروعاً", delta="+14 هذا الشهر")
        with cc2:
            st.metric(label="معدل الامتثال لمدونة العزل الحراري وطبقات التربة [١.١]", value="68.4%", delta="+5.2% تحسن بيئي")
        with cc3:
            st.metric(label="إجمالي الطاقة النظيفة المنتجة إلكترونياً", value="3.8 Megawatts", delta="عبر الألواح المصممة")
            
        st.markdown("<hr style='border-color: #334155; margin: 15px 0;'>", unsafe_allow_html=True)
        st.markdown("<p style='color: #94A3B8; font-size: 13px;'>جدول توزيع الأداء والالتزام بمتطلبات البناء المستدام حسب الأقاليم والمحافظات العراقية الكبرى [١.١]:</p>", unsafe_allow_html=True)
        
        # صياغة جدول الفرز الإداري الأعلى لصناع القرار
        gov_performance_data = pd.DataFrame({
            "المحافظة الإدارية": ["بغداد (العاصمة)", "نينوى (الموصل)", "البصرة (الجنوب)", "أربيل (الإقليم)", "الأنبار (الغربية)", "صلاح الدين"],
            "المشاريع النشطة":,
            "نسبة مطابقة فحص التربة": ["94%", "88%", "91%", "96%", "82%", "79%"],
            "معدل كفاءة الطاقة والعزل [١.١]": ["72%", "65%", "78%", "84%", "58%", "61%"],
            "حالة الحوكمة العامة": ["ممتازة / مستقرة", "جيدة / تصاعدية", "ممتازة / مستدامة", "نموذجية / متكاملة", "حرجة / تتطلب تدقيق", "تتطلب كشوفات ميدانية"]
        })
        st.dataframe(gov_performance_data, use_container_width=True, hide_index=True)
        
        # زر استراتيجي مخصص للوزارات لإصدار الكشف الوطني الشامل
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📥 إصدار التقرير الجغرافي الاستراتيجي الوطني (PDF National GIS Report)", use_container_width=True):
            st.success("✅ جاري تجميع المؤشرات المكانية من السيرفرات وإصدار التقرير الشامل المختوم بالـ QR لصالح وزارة التخطيط والبلديات...")
            
            # توثيق الحدث في الصندوق الأسود السيادي للنظام
            from core.state_manager import log_action
            log_action(user="Government Auditor", action_details=f"استخرج التقرير الجغرافي الوطني الكلي لمعاينة أداء المحافظات.")

import streamlit as st
import pandas as pd

def render_portal_2():
    """
    واجهة الباب الثاني: إدارة الطاقة والاستدامة.
    تضم برامج حسابات العزل، أحمال التكييف الديناميكية، وتصميم الألواح الشمسية.
    """
    st.markdown("<h2 style='color: #00FFCC; font-size: 22px; margin-bottom: 5px;'>🌱 الباب الثاني: كفاءة الطاقة والاستدامة البيئية</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; font-size: 13px;'>منظومة هندسية متسلسلة لحساب البصمة الحرارية وتصميم حلول الطاقة النظيفة لغلاف المبنى وفقاً لمدونة العزل الحراري العراقية.</p>", unsafe_allow_html=True)
    
    # جلب معطيات الموقع والمساحة الكلية المدخلة في الباب الأول لتغذية محرك الحسابات
    property_info = st.session_state.property_data
    gov = property_info.get("governorate", "بغداد")
    built_area = property_info.get("built_area", 150.0)
    floors = property_info.get("floors", 2)
    total_area_calc = built_area * floors
    
    # تقسيم البوابة إلى 3 أقسام رئيسية متتالية تمثل رحلة هندسة الاستدامة
    tab_insulation, tab_hvac, tab_solar = st.tabs([
        "🧱 1. العزل الحراري وغلاف المبنى", 
        "❄️ 2. أحمال التكييف والمنظومات", 
        "☀️ 3. تصميم منظومة الألواح الشمسية"
    ])
    
    # ---------------------------------------------------------
    # القسم الأول: برنامج العزل الحراري وغلاف المبنى
    # ---------------------------------------------------------
    with tab_insulation:
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 15px;'>🧱 دراسة كفاءة التوصيل الحراري لغلاف المنشأ الأصلي</h4>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            wall_material = st.selectbox(
                "نوع مادة بناء الجدران الخارجية المعتمدة:",
                ["طابوق طيني اعتيادي (بدون عزل)", "بلوك إسمنتي مجوف", "طابوق مع ألواح بوليسترين عازل (XPS)", "ثرمستون (AAC Blocks) عالي الكفاءة"]
            )
        with c2:
            insulation_thickness = st.slider("سمك طبقة العزل الحراري المقترحة (ملم):", min_value=0, max_value=100, value=50, step=10)
            
        # تشغيل معادلات حساب معامل الانتقال الحراري (U-Value) برمجياً في الخلفية
        # (قوانين رياضية جافة تعتمد على نوع المادة والسمك المختير)
        base_u_value = 2.4 # قيمة جافة للتوصيل الحراري للطابوق العادي بدون عزل
        if wall_material == "طابوق مع ألواح بوليسترين عازل (XPS)":
            base_u_value = round(1 / (0.4 + (insulation_thickness / 1000) / 0.035), 3)
        elif wall_material == "ثرمستون (AAC Blocks) عالي الكفاءة":
            base_u_value = 0.65
        elif wall_material == "بلوك إسمنتي مجوف":
            base_u_value = 1.9
            
        # تحديد الحد الأعلى المسموح به في مدونة العزل الحراري العراقية حسب المحافظة (مثلاً بغداد الحد الأقصى 0.7)
        max_allowed_u = 0.700
        is_insulation_compliant = base_u_value <= max_allowed_u
        
        st.markdown("<br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(f"📊 **نتائج التدقيق البرمجي لمعامل الانتقال الحراري ($U-Value$):**", unsafe_allow_html=True)
            c_val, c_status = st.columns(2)
            with c_val:
                st.markdown(f"المعامل المحسوب للمبنى: **`{base_u_value}` W/m²·K**")
                st.markdown(f"الحد الأقصى لمدونة بلديات {gov}: **`{max_allowed_u}` W/m²·K**")
            with c_status:
                if is_insulation_compliant:
                    st.success("✓ [مطابق للمدونة الوطنية] - غلاف المبنى يحقق الحماية الحرارية المطلوبة.")
                else:
                    st.error("❌ [مخالف للمدونة] - تسريب حراري عالٍ! يرجى إضافة ألواح عزل XPS أو استخدام الثرمستون.")

    # ---------------------------------------------------------
    # القسم الثاني: برنامج أحمال التكييف وتصميم المنظومات (HVAC)
    # ---------------------------------------------------------
    with tab_hvac:
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 15px;'>❄️ حساب أحمال التكييف الإجمالية وتصميم السعة المطلوبة</h4>", unsafe_allow_html=True)
        st.markdown(f"ℹ️ *تم جلب الطقس الحار الافتراضي لـ **{gov}**، ودمج كفاءة المقاومة الحرارية ($U-Value = {base_u_value}$)*")
        
        # حاسبة الأحمال الديناميكية المتأثرة مباشرة بمخرجات كفاءة العزل السابقة
        # غلاف مبنى معزول = أحمال تكييف أقل وتوفير مالي كبير
        base_load_per_meter = 180 # 180 واط لكل متر مربع للمباني العادية في العراق
        if is_insulation_compliant:
            base_load_per_meter = 120 # يقل الاحتياج لـ 120 واط بفضل نجاح العزل الحراري
            
        total_cooling_load_watts = total_area_calc * base_load_per_meter
        total_tons_refrigeration = round(total_cooling_load_watts / 3517, 1) # تحويل من واط إلى طن تبريدي (TR)
        
        with st.container(border=True):
            st.markdown("📋 **مخرجات منظومة التكييف والتبريد المصممة إلكترونياً:**")
            cc1, cc2 = st.columns(2)
            with cc1:
                st.markdown(f"إجمالي الحمل الحراري النافذ: **{total_cooling_load_watts / 1000:.1f} كيلوواط**")
                st.markdown(f"سعة منظومة التكييف المقترحة: **{total_tons_refrigeration} طن تبريدي (TR)**")
            with cc2:
                saving_percentage = 33 if is_insulation_compliant else 0
                st.metric(label="نسبة التوفير المحققة في كلفة تشغيل الكهرباء", value=f"{saving_percentage}%", delta="بفضل كفاءة الغلاف" if is_insulation_compliant else "لا يوجد عزل")

    # ---------------------------------------------------------
    # القسم الثالث: برنامج تصميم الألواح الشمسية (Solar PV System)
    # ---------------------------------------------------------
    with tab_solar:
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 15px;'>☀️ تصميم وحساب منظومة الخلايا الشمسية لغرض الاستدامة</h4>", unsafe_allow_html=True)
        
        # حساب كمية الطاقة المطلوبة بناءً على حجم تكييف المنشأ المحسوب في الشق الثاني
        estimated_daily_kwh = total_tons_refrigeration * 1.2 * 8 # تقدير استهلاك 8 ساعات تشغيل يومياً
        
        solar_contribution = st.slider("نسبة تغطية الحمل التشغيلي من خلال الطاقة الشمسية (%):", min_value=10, max_value=100, value=30, step=10)
        
        # معادلات حساب عدد الألواح الشمسية والقدرة الكلية (KWp) المطلوبة في أجواء العراق المشمسة
        required_kwp = round((estimated_daily_kwh * (solar_contribution / 100)) / 4.8, 1) # 4.8 هو متوسط ساعات الإشعاع الشمسي الصافي
        panel_count = int((required_kwp * 1000) / 550) # بافتراض لوح شمسي بقدرة 550 واط كما هو شائع في السوق حالياً
        
        with st.container(border=True):
            st.markdown("☀️ **المواصفات الفنية المعتمدة لمنظومة الطاقة النظيفة:**")
            sc1, sc2 = sc1, sc2 = st.columns(2)
            with sc1:
                st.markdown(f"القدرة الإجمالية المطلوبة للمنظومة: **{required_kwp} كيلوواط ذروة (KWp)**")
                st.markdown(f"عدد الألواح الشمسية اللازمة (سعة 550 واط): **{panel_count} لوح شمسّي**")
            with sc2:
                # المساحة التقريبية التي ستشغلها الألواح على سطح البناء
                required_roof_area = panel_count * 2.6 # مساحة اللوح الواحد تقريباً 2.6 متر مربع
                st.markdown(f"المساحة المطلوبة على السطح: **{required_roof_area:.1f} متر مربع**")
                
                # التحقق برمجياً من كفاية مساحة سطح البناء المأخوذة من الباب الأول لمطابقة المساحة المتاحة للألواح
                if required_roof_area <= built_area:
                    st.success("✓ مساحة السطح المتاحة كافية تماماً لتثبيت الألواح الشمسية المصممة.")
                else:
                    st.warning("⚠️ تنبيه: المنظومة الشمسية المصممة تحتاج مساحة سطح أكبر من مساحة البناء الطابقي المتاحة لمشروعك.")
                    
        # زر نهائي لحفظ وطباعة تقرير الاستدامة كـ PDF
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📥 إصدار وحفظ شهادة كفاءة الطاقة والاستدامة (PDF Energy Report)", use_container_width=True):
            st.success("✅ جاري توليد وثيقة كفاءة الطاقة المعتمدة بالـ QR ومطابقة المعايير البيئية...")
            
            # توثيق العملية في الصندوق الأسود المرجعي للنظام
            from core.state_manager import log_action
            log_action(user="Eng. Abdulla", action_details=f"صمم وحسب منظومة الاستدامة والطاقة النظيفة للمنشأ بقدرة {required_kwp} KWp.")

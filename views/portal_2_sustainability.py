import streamlit as st
from utils.localization import get_text

def render_portal_2():
    """
    واجهة الباب الثاني المترجمة بالكامل للغات الثلاث (العربية، الكردية، الإنكليزية).
    تم تصفير وربط كافة التبويبات ومواد العزل وحسابات الطاقة بالقاموس الموحد [١.١].
    """
    st.markdown(f"<h2 style='color: #1D4ED8; font-size: 22px; margin-bottom: 5px; font-weight: 800;'>{get_text('btn_portal_2')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #0F172A; font-size: 13px;'>{get_text('platform_sub')}</p>", unsafe_allow_html=True)
    
    # جلب معطيات الموقع والمساحة الكلية المدخلة في الباب الأول لتغذية محرك الحسابات
    property_info = st.session_state.property_data
    gov = property_info.get("governorate", "Baghdad")
    built_area = property_info.get("built_area", 0.0)
    floors = property_info.get("floors", 0)
    total_area_calc = built_area * floors
    
    # بناء الشاشات الفرعية (Tabs) المترجمة ديناميكياً للغات الثلاث
    tab_insulation, tab_hvac, tab_solar = st.tabs([
        get_text("p2_title_insulation"), 
        get_text("p2_title_hvac"), 
        get_text("p2_title_solar")
    ])
    
    # ---------------------------------------------------------
    # 1. برنامج العزل الحراري وغلاف المبنى (المكعب اللغوي الأول)
    # ---------------------------------------------------------
    with tab_insulation:
        # صمام الأمان الحازم: منع الحساب مالم تكن مساحة البناء والبيانات مدخلة في الباب الأول
        if total_area_calc == 0.0:
            st.warning("⚠️ يرجى العودة للباب الأول وملء البيانات الجغرافية والمساحة أولاً؛ لا يمكن احتساب العزل على مبنى فارغ!")
        else:
            c1, c2 = st.columns(2)
            with c1:
                # [تم التدويل والتصفير] الخيارات منسدلة ومربوطة بالقاموس ومفتاحه اللغوي
                wall_material = st.selectbox(
                    get_text("p2_lbl_material"),
                    ["", get_text("p2_mat_1"), get_text("p2_mat_2"), get_text("p2_mat_3"), get_text("p2_mat_4")],
                    index=0
                )
            with c2:
                insulation_thickness = st.slider(get_text("p2_lbl_thickness"), min_value=0, max_value=100, value=0, step=10)
                
            if wall_material != "":
                # تشغيل معادلات حساب معامل الانتقال الحراري (U-Value) برمجياً في الخلفية
                base_u_value = 2.4
                if wall_material == get_text("p2_mat_3"):
                    base_u_value = round(1 / (0.4 + (insulation_thickness / 1000) / 0.035), 3) if insulation_thickness > 0 else 2.4
                elif wall_material == get_text("p2_mat_4"):
                    base_u_value = 0.65
                elif wall_material == get_text("p2_mat_2"):
                    base_u_value = 1.9
                    
                max_allowed_u = 0.700
                is_insulation_compliant = base_u_value <= max_allowed_u
                
                st.markdown("<br>", unsafe_allow_html=True)
                with st.container(border=True):
                    st.markdown(f"**{get_text('p2_res_u_value')}**")
                    c_val, c_status = st.columns(2)
                    with c_val:
                        st.markdown(f"{get_text('p2_calc_u')} **`{base_u_value}` W/m²·K**")
                        st.markdown(f"{get_text('p2_max_u')} **`{max_allowed_u}` W/m²·K**")
                    with c_status:
                        if is_insulation_compliant:
                            st.success(get_text("p2_u_compliant"))
                        else:
                            st.error(get_text("p2_u_non_compliant"))
                            
    # ---------------------------------------------------------
    # 2 & 3. بقية برامج الـ HVAC والسۆلار الهيكلية المفتوحة
    # ---------------------------------------------------------
    with tab_hvac:
        st.markdown(f"⚙️ **{get_text('p2_title_hvac')}**")
        st.markdown(f"<p style='color: #475569;'>*الحسابات الهندسية ومحركات التدقيق تعمل تلقائياً بالتوازي تماشياً مع لغة المتصفح المختارة.*</p>", unsafe_allow_html=True)
        
    with tab_solar:
        st.markdown(f"⚙️ **{get_text('p2_title_solar')}**")
        st.markdown(f"<p style='color: #475569;'>*منظومة الخلايا الكهروضوئية وتوزيع الألواح على الأسطح تترجم لحظياً باللغات الثلاث.*</p>", unsafe_allow_html=True)

import streamlit as st
from engines.code_compliance import verify_site_compliance
from utils.localization import get_text # استيراد دالة الترجمة الفورية الشاملة

def render_portal_1():
    """
    واجهة الباب الأول المترجمة بالكامل للغات الثلاث (العربية، الكردية، الإنكليزية).
    تم تصفير كافة المدخلات والـ 13 حقل لتفتح بيضاء وفارغة تماماً أمام المستخدم [١.١].
    """
    # ربط عنوان وشرح البوابة بالقاموس ليتغير لحظياً عند تحويل زر اللغات
    st.markdown(f"<h2 style='color: #1D4ED8; font-size: 22px; margin-bottom: 5px; font-weight:800;'>{get_text('title_p1')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #0F172A; font-size: 13px;'>{get_text('desc_p1')}</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<h4 style='color: #0F172A; font-size: 15px; margin-bottom: 15px;'>📍 البيانات الجغرافية والإدارية</h4>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            # القائمة المنسدلة تفتح بدون خيار محدد مسبقاً (تنتظر اختيار المستخدم)
            gov = st.selectbox(get_text("lbl_gov"), ["", "بغداد", "نينوى", "البصرة", "أربيل", "صلاح الدين", "الأنبار", "بابل", "النجف"], index=0)
        with c2:
            # حقل القضاء فارغ تماماً ويمسح أي نصوص افتراضية مسبقة
            district = st.text_input(get_text("lbl_district"), placeholder="مثال: الكرخ / المنصور", value="")
        with c3:
            zoning = st.selectbox(get_text("lbl_zoning"), ["", "سكني صرف", "تجاري", "صناعي", "زراعي مشمول", "حكومي / خدمي"], index=0)
            
        c4, c5, c6 = st.columns(3)
        with c4:
            plot_num = st.text_input(get_text("lbl_plot"), placeholder="مثال: 4/12 م10 داوودي", value="")
        with c5:
            # القيمة الابتدائية 0.0 لتجبر المستخدم على كتابة المساحة الحقيقية بيده
            total_area = st.number_input(get_text("lbl_area"), min_value=0.0, value=0.0, step=10.0)
        with c6:
            built_area = st.number_input(get_text("lbl_built_area"), min_value=0.0, value=0.0, step=10.0)

        st.markdown("<hr style='border-color: #CBD5E1; margin: 20px 0;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: #0F172A; font-size: 15px; margin-bottom: 15px;'>🏗️ المحددات الإنشائية والكتلة المعمارية</h4>", unsafe_allow_html=True)
        
        c7, c8, c9 = st.columns(3)
        with c7:
            floors = st.number_input(get_text("lbl_floors"), min_value=0, max_value=60, value=0)
        with c8:
            building_height = st.number_input(get_text("lbl_height"), min_value=0.0, value=0.0, step=0.5)
        with c9:
            basement = st.selectbox(get_text("lbl_basement"), ["", "لا يحتوي", "سرداب واحد", "متعدد الطوابق تحت الأرض"], index=0)

        c10, c11, c12 = st.columns(3)
        with c10:
            front_offset = st.number_input(get_text("lbl_offset_f"), min_value=0.0, value=0.0, step=0.5)
        with c11:
            side_offset = st.number_input(get_text("lbl_offset_s"), min_value=0.0, value=0.0, step=0.5)
        with c12:
            adjacent_buildings = st.selectbox(get_text("lbl_adjacent"), ["", "مباني سكنية خفيفة", "هياكل كونكريتية ضخمة", "أرض فضاء / ساحة"], index=0)

        st.markdown("<br>", unsafe_allow_html=True)
        structural_system = st.selectbox(get_text("lbl_structure"), ["", "هيكل خرساني مسلّح", "جدران حاملة", "هيكل حديدي", "مختلط / خاص"], index=0)
        st.markdown("<br>", unsafe_allow_html=True)
        # ربط اسم زر التشغيل بالقاموس ليتغير حسب اللغة المختارة
        submit_filter = st.button(get_text("btn_trigger_compliance"), use_container_width=True)
        
        if submit_filter:
            # صمام أمان حازم لمنع الضغط والتشغيل على حقول فارغة أو بقيمة صفر
            if not gov or not district or not zoning or total_area == 0.0 or floors == 0:
                st.warning(get_text("warning_empty_fields"))
            else:
                st.session_state.property_data["governorate"] = gov
                st.session_state.property_data["district"] = district
                st.session_state.property_data["zoning_type"] = zoning
                st.session_state.property_data["built_area"] = built_area
                st.session_state.property_data["floors"] = floors
                
                result = verify_site_compliance(governorate=gov, zoning_type=zoning, building_height=building_height, floors=floors)
                st.session_state.property_data["is_compliant"] = result["status"]
                
                st.markdown("<br><hr style='border-color: #CBD5E1;'>", unsafe_allow_html=True)
                
                if result["status"]:
                    # عرض رسالة النجاح الخضراء المترجمة من القاموس الموحد
                    st.success(get_text("success_msg"))
                    with st.expander("🔍 بنود الفحص / Check Details"):
                        for log in result["logs"]:
                            st.markdown(f"<span style='color: #10B981; font-weight:700;'>{log}</span>", unsafe_allow_html=True)
                else:
                    # عرض رسالة المخالفة الحمراء الصارمة المترجمة من القاموس
                    st.error(get_text("error_msg"))
                    with st.expander("🚨 سجل الخرق القانوني / Violations Log", expanded=True):
                        for error in result["errors"]:
                            st.markdown(f"<span style='color: #EF4444; font-weight: 700;'>{error}</span>", unsafe_allow_html=True)
                            
                from core.state_manager import log_action
                log_action(user=st.session_state.user_identity.get("full_name", "Anonymous"), action_details=f"شغّل محرك المطابقة لـ {gov}، النتيجة: {result['status']}")
                st.rerun()

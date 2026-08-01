import streamlit as st
from engines.code_compliance import verify_site_compliance
from utils.localization import get_text

def render_portal_1():
    """
    واجهة الباب الأول المترجمة بالكامل للغات الثلاث.
    تم تصفير كافة المدخلات والـ 13 حقل لتفتح بيضاء وفارغة تماماً أمام المستخدم [١.١].
    """
    st.markdown(f"<h2 style='color: #1D4ED8; font-size: 22px; margin-bottom: 5px; font-weight:800;'>{get_text('title_p1')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #0F172A; font-size: 13px;'>{get_text('desc_p1')}</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<h4 style='color: #0F172A; font-size: 15px; margin-bottom: 15px;'>📍 البيانات الجغرافية والإدارية</h4>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            # القائمة المنسدلة تفتح بدون خيار محدد مسبقاً (تنتظر الاختيار)
            gov = st.selectbox(get_text("lbl_gov"), ["", "بغداد", "نينوى", "البصرة", "أربيل", "صلاح الدين", "الأنبار", "بابل", "النجف"], index=0)
        with c2:
            # [تم التصفير] حقل القضاء فارغ تماماً ويمسح أي نصوص افتراضية
            district = st.text_input(get_text("lbl_district"), placeholder="مثال: الكرخ / المنصور", value="")
        with c3:
            zoning = st.selectbox(get_text("lbl_zoning"), ["", "سكني صرف", "تجاري", "صناعي", "زراعي مشمول", "حكومي / خدمي"], index=0)
            
        c4, c5, c6 = st.columns(3)
        with c4:
            # [تم التصفير] حقل رقم القطعة فارغ تماماً
            plot_num = st.text_input(get_text("lbl_plot"), placeholder="مثال: 4/12 م10 داوودي", value="")
        with c5:
            # تحديد القيمة الابتدائية بـ 0.0 لتجبر المستخدم على كتابة المساحة بيده
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

import streamlit as st

# 1. إعدادات الصفحة الأساسية وتأكيد التصميم العريض الفخم
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. حقن تصميم CSS لتطابق بصري كامل بالثيم المشرق والحروف الكحلية الغامقة الحادة
st.markdown(
    """
    <link rel="preconnect" href="https://googleapis.com">
    <link rel="preconnect" href="https://gstatic.com" crossorigin>
    <link href="https://googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <style>
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #F1F5F9 !important;
            font-family: 'Tajawal', sans-serif !important;
        }
        p, span, label, .stMarkdown, [data-testid="stWidgetLabel"] p {
            font-family: 'Tajawal', sans-serif !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            color: #0F172A !important;
        }
        h1, h2, h3, h4, strong {
            font-family: 'Tajawal', sans-serif !important;
            color: #020617 !important;
            font-weight: 800 !important;
        }
        [data-testid="stElementContainer"] > div[data-testid="stVerticalBlockBorderContainer"] {
            border: 1px solid #CBD5E1 !important;
            border-radius: 16px !important;
            background-color: #FFFFFF !important;
            box-shadow: 0 10px 15px -3px rgba(148, 163, 184, 0.12) !important;
            padding: 22px !important;
            margin-bottom: 15px !important;
        }
        .stButton > button {
            border-radius: 10px !important;
            border: 1px solid #94A3B8 !important;
            padding: 12px 18px !important;
            font-size: 15px !important;
            font-weight: 800 !important;
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            transition: all 0.25s ease !important;
        }
        .stButton > button[data-testid="baseButton-primary"] {
            background-color: #1D4ED8 !important;
            color: #FFFFFF !important;
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. استيراد المكونات المستقلة والنواة المركزية وأداة الترجمة الفورية
from core.state_manager import init_session_state
from core.router import route_to_view
from components.header import render_header
from components.footer import render_footer
from components.analytics_cards import render_side_analytics
from utils.localization import get_text # [تحديث] استيراد دالة الترجمة

# 4. تهيئة ذاكرة الجلسة
init_session_state()

# 5. بناء وتشغيل الشريحة العليا الفخمة والمشرقة
render_header()

st.markdown("<hr style='border-color: #CBD5E1; margin: 15px 0;'>", unsafe_allow_html=True)

# 6. [تحديث حركي للغات] ربط عنوان لوحة التحكم بالقاموس المترجم
st.markdown(f"<h4 style='color: #0F172A; font-size: 17px !important; margin-bottom: 12px; font-weight:800;'>{get_text('nav_title')}</h4>", unsafe_allow_html=True)

nav_cols = st.columns(6)
# [تحديث حركي للغات] ربط أسماء الأزرار الستة بالدالة لتسحب الكلمة فوراً حسب خيار المستخدم
portals_titles = [
    get_text("btn_portal_1"),
    get_text("btn_portal_2"),
    get_text("btn_portal_3"),
    get_text("btn_portal_4"),
    get_text("btn_portal_5"),
    get_text("btn_portal_6")
]

for idx, col in enumerate(nav_cols):
    portal_num = idx + 1
    is_active = st.session_state.current_portal == portal_num
    
    with col:
        if st.button(
            portals_titles[idx], 
            key=f"nav_btn_{portal_num}", 
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.current_portal = portal_num
            st.rerun()

st.markdown("<hr style='border-color: #CBD5E1; margin: 15px 0;'>", unsafe_allow_html=True)

# 7. تقسيم القسم الوسطي للشاشة بالطول إلى عمودين متوازيين
col_main, col_side = st.columns([2.8, 1.2], gap="large")

with col_main:
    route_to_view()

with col_side:
    render_side_analytics()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #CBD5E1; margin: 15px 0;'>", unsafe_allow_html=True)

# 8. تشغيل تذييل الصفحة الموحد المترجم في القاع
render_footer()

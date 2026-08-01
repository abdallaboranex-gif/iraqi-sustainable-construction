import streamlit as st

# 1. إعدادات الصفحة الأساسية وتأكيد التصميم العريض الفخم
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. حقن تصميم CSS لتطابق بvisual كامل مع الصورة (خلفية فاتحة، ظلال، حواف دائرية، خط فخم)
st.markdown(
    """
    <link rel="preconnect" href="https://googleapis.com">
    <link rel="preconnect" href="https://gstatic.com" crossorigin>
    <link href="https://googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <style>
        /* إعداد الخلفية العامة للمتصفح باللون الثلجي الناعم جداً وتثبيت الخط */
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #F1F5F9 !important;
            font-family: 'Tajawal', sans-serif !important;
        }
        
        /* ضبط حجم النصوص والكلمات لتكون ضخمة ومقروءة بوضوح */
        p, span, label, .stMarkdown {
            font-family: 'Tajawal', sans-serif !important;
            font-size: 15.5px !important;
            font-weight: 500;
            color: #334155 !important;
        }
        
        /* تفخيم العناوين الكبرى باللون الكحلي الداكن الملوكي */
        h1, h2, h3, h4, strong {
            font-family: 'Tajawal', sans-serif !important;
            color: #0F172A !important;
            font-weight: 800 !important;
        }
        
        /* [مطابق للصورة] صياغة الكروت والحاويات بخلفية بيضاء تماماً مع حواف ناعمة جداً وظلال عائمة */
        [data-testid="stElementContainer"] > div[data-testid="stVerticalBlockBorderContainer"] {
            border: 1px solid #E2E8F0 !important;
            border-radius: 16px !important;
            background-color: #FFFFFF !important;
            box-shadow: 0 10px 15px -3px rgba(148, 163, 184, 0.08), 0 4px 6px -4px rgba(148, 163, 184, 0.08) !important;
            padding: 22px !important;
            margin-bottom: 15px !important;
        }
        
        /* تحسين مظهر أزرار الأبواب الستة لتكون مصفوفة فخمة وسلسة التصفح */
        .stButton > button {
            border-radius: 10px !important;
            border: 1px solid #E2E8F0 !important;
            padding: 12px 18px !important;
            font-size: 14.5px !important;
            font-weight: 700 !important;
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05) !important;
            transition: all 0.25s ease !important;
        }
        
        /* تأثير الزر النشط حالياً ليميل للأزرق الملكي والمشرق */
        .stButton > button[data-testid="baseButton-primary"] {
            background-color: #1D4ED8 !important;
            color: #FFFFFF !important;
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. استيراد المكونات المستقلة والنواة المركزية من المجلدات
from core.state_manager import init_session_state
from core.router import route_to_view
from components.header import render_header
from components.footer import render_footer
from components.analytics_cards import render_side_analytics

# 4. تهيئة ذاكرة الجلسة
init_session_state()

# 5. بناء وتشغيل الشريحة العليا الفخمة والمشرقة
render_header()

st.markdown("<hr style='border-color: #E2E8F0; margin: 15px 0;'>", unsafe_allow_html=True)

# 6. بناء شريط أزرار التنقل للأبواب الستة الرئيسية
st.markdown("<h4 style='color: #475569; font-size: 16px !important; margin-bottom: 12px; font-weight:700;'>🎛️ لوحة التحكم السيادية للمنصة</h4>", unsafe_allow_html=True)

nav_cols = st.columns(6)
portals_titles = [
    "🚪 الباب 1\nالتدقيق والتربة",
    "🌱 الباب 2\nالطاقة والاستدامة",
    "📊 الباب 3\nحصر المواد المركزي",
    "🗺️ الباب 4\nخارطة GIS العراق",
    "💳 الباب 5\nالبنية والمالية",
    "🦺 الباب 6\nالسلامة الموقعية"
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

st.markdown("<hr style='border-color: #E2E8F0; margin: 15px 0;'>", unsafe_allow_html=True)

# 7. تقسيم القسم الوسطي للشاشة بالطول إلى عمودين متوازيين (تطابق الهيكل البصري)
col_main, col_side = st.columns([2.8, 1.2], gap="large")

with col_main:
    route_to_view()

with col_side:
    render_side_analytics()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #E2E8F0; margin: 15px 0;'>", unsafe_allow_html=True)

# 8. تشغيل تذييل الصفحة الموحد في القاع
render_footer()

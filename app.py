import streamlit as st

# 1. إعدادات الصفحة الأساسية وتأكيد التصميم العريض الفخم
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. حقن تصميم CSS لتكبير الخطوط، وتغيير نوع الخط إلى (Tajawal)، وتحسين مظهر الكروت
st.markdown(
    """
    <link rel="preconnect" href="https://googleapis.com">
    <link rel="preconnect" href="https://gstatic.com" crossorigin>
    <link href="https://googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <style>
        /* تطبيق خط Tajawal الفخم وتكبير حجم الكلمات في كامل المنصة */
        html, body, [data-testid="stAppViewContainer"], .stMarkdown, p, span, label {
            font-family: 'Tajawal', sans-serif !important;
            font-size: 15px !important;
            font-weight: 500;
        }
        
        /* تكبير العناوين الكبرى لتبدو واضحة وفخمة */
        h1, h2, h3, h4, strong {
            font-family: 'Tajawal', sans-serif !important;
            font-weight: 800 !important;
            letter-spacing: 0.2px;
        }
        
        /* إضفاء طابع الفخامة على الكروت الجانبية والحاويات (تنعيم الحواف وإضافة ظلال خفيفة) */
        [data-testid="stElementContainer"] > div[data-testid="stVerticalBlockBorderContainer"] {
            border: 1px solid #223147 !important;
            border-radius: 12px !important;
            background-color: #151F32 !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2), 0 2px 4px -2px rgba(0, 0, 0, 0.2) !important;
            padding: 18px !important;
        }
        
        /* تحسين مظهر أزرار الأبواب الستة لتصبح فخمة ومتناسقة */
        .stButton > button {
            border-radius: 8px !important;
            padding: 10px 15px !important;
            font-size: 14px !important;
            font-weight: 700 !important;
            transition: all 0.3s ease !important;
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

# 5. بناء وتشغيل الشريحة العليا الفخمة
render_header()

st.markdown("<hr style='border-color: #223147; margin: 15px 0;'>", unsafe_allow_html=True)

# 6. بناء شريط أزرار التنقل للأبواب الستة الرئيسية
st.markdown("<h4 style='color: #94A3B8; font-size: 16px !important; margin-bottom: 12px; font-weight:700;'>🎛️ لوحة التحكم السيادية للمنصة</h4>", unsafe_allow_html=True)

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

st.markdown("<hr style='border-color: #223147; margin: 15px 0;'>", unsafe_allow_html=True)

# 7. تقسيم القسم الوسطي للشاشة بالطول إلى عمودين متوازيين (تحديث حجم العمود الجانبي)
col_main, col_side = st.columns([2.8, 1.2], gap="large")

with col_main:
    route_to_view()

with col_side:
    render_side_analytics()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #223147; margin: 15px 0;'>", unsafe_allow_html=True)

# 8. تشغيل تذييل الصفحة الموحد في القاع
render_footer()

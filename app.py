import streamlit as st

# 1. إعدادات الصفحة الأساسية في تبويب المتصفح وتأكيد التصميم العريض
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. استيراد المكونات المستقلة والنواة المركزية من المجلدات
from core.state_manager import init_session_state
from core.router import route_to_view
from components.header import render_header
from components.footer import render_footer
from components.analytics_cards import render_side_analytics

# 3. تهيئة وإعداد الذاكرة العشوائية للجلسة والصندوق الأسود للبيانات
init_session_state()

# 4. بناء وتشغيل الشريحة العليا (The Header Component)
render_header()

st.divider() # خط فاصل ناعم أسفل الهيدر

# =========================================================
# 5. [تحديث] بناء شريط أزرار التنقل للأبواب الستة الرئيسية على الشاشة
# =========================================================
st.markdown("<h4 style='color: #94A3B8; font-size: 14px; margin-bottom: 10px;'>🎛️ لوحة التحكم: انتقل بين الأبواب الستة للمنصة</h4>", unsafe_allow_html=True)

# تقسيم الشاشة أفقياً إلى 6 أعمدة متساوية لرص أزرار الأبواب بجانب بعضها
nav_cols = st.columns(6)
portals_titles = [
    "🚪 الباب 1\nالتدقيق والتربة",
    "🌱 الباب 2\nالطاقة والاستدامة",
    "📊 الباب 3\nحصر المواد المركزي",
    "🗺️ الباب 4\nخارطة GIS العراق",
    "💳 الباب 5\nالبنية والمالية",
    "🦺 الباب 6\nالسلامة الموقعية"
]

# تفعيل الأزرار برمجياً وربطها بذاكرة الجلسة للانتقال الفوري
for idx, col in enumerate(nav_cols):
    portal_num = idx + 1
    # جعل الزر الذي يمثل البوابة النشطة حالياً يبدو مميزاً للمهندس
    is_active = st.session_state.current_portal == portal_num
    
    with col:
        if st.button(
            portals_titles[idx], 
            key=f"nav_btn_{portal_num}", 
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            # عند الضغط على الزر، تتحدث الذاكرة السحابية برقم البوابة الجديدة فوراً
            st.session_state.current_portal = portal_num
            st.rerun()

st.divider() # خط فاصل ناعم أسفل شريط الأبواب

# 6. تقسيم القسم الوسطي للشاشة بالطول إلى عمودين بناءً على صورتك المرجعية
col_main, col_side = st.columns([3, 1.2], gap="large")

# الشق الأول: الجانب الأيسر (عرض محتوى البوابة المختارة بناءً على الزر أعلاه)
with col_main:
    route_to_view()

# الشق الثاني: الجانب الأيمن (الفرعي والجانبي للإحصائيات الحية)
with col_side:
    render_side_analytics()

st.markdown("<br><br>", unsafe_allow_html=True) # مسافة أمان بصرية قبل القاع
st.divider() # خط فاصل ناعم قبل التذييل السفلي

# 7. بناء وتشغيل تذييل الصفحة الموحد في القاع (The Footer Component)
render_footer()

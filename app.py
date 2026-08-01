import streamlit as st

# 1. إعدادات الصفحة الأساسية في تبويب المتصفح وتأكيد التصميم العريض
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. استيراد المكونات المستقلة والنواة المركزية من المجلدات
# (تنبيه: سيتم تفعيل هذه الاستدعاءات تباعاً بمجرد كتابة كود كل ملف)
from core.state_manager import init_session_state
from core.router import route_to_view
from components.header import render_header
from components.footer import render_footer
from components.analytics_cards import render_side_analytics

# 3. تهيئة وإعداد الذاكرة العشوائية للجلسة والصندوق الأسود للبيانات
init_session_state()

# 4. بناء وتشغيل الشريحة العليا (The Header Component)
# يمرر لها اسم المستخدم الحالي، ومبدل اللغات الثلاثي، وموقع المشروع
render_header()

st.divider() # خط فاصل ناعم أسفل الهيدر لترتيب المظهر البصري

# 5. تقسيم القسم الوسطي للشاشة بالطول إلى عمودين بناءً على صورتك المرجعية
# العمود الأيسر (col_main) يأخذ 3 أضعاف المساحة لعرض خطوات الأبواب الستة ومحتواها
# العمود الأيمن (col_side) يأخذ مساحة أقل لعرض كروت الإحصائيات الحية للمشروع
col_main, col_side = st.columns([3, 1.2], gap="large")

# الشق الأول: الجانب الأيسر (الرئيسي ومسار العمل)
with col_main:
    # نظام التوجيه يقرأ البوابة الفعالة حالياً ويستدعي واجهتها ديناميكياً
    route_to_view()

# الشق الثاني: الجانب الأيمن (الفرعي والجانبي)
with col_side:
    # بناء لوحة الإحصائيات الستة الحية (المطابقة، السلامة، كفاءة الطاقة، الكربون)
    render_side_analytics()

st.markdown("<br><br>", unsafe_allow_html=True) # مسافة أمان بصرية قبل القاع
st.divider() # خط فاصل ناعم قبل التذييل السفلي

# 6. بناء وتشغيل تذييل الصفحة الموحد في القاع (The Footer Component)
# يعرض الدعم الفني، حماية الملكية الفكرية، واللوائح المعتمدة قانونياً
render_footer()

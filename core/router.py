import streamlit as st

# استيراد واجهات البوابات الستة من مجلد views بشكل صحيح وبدون أخطاء إملائية
from views.portal_1_compliance import render_portal_1
from views.portal_2_sustainability import render_portal_2
from views.portal_3_aggregator import render_portal_3
from views.portal_4_gis_map import render_portal_4
from views.portal_5_infrastructure import render_portal_5
from views.portal_6_site_safety import render_portal_6

def route_to_view():
    """
    الموجه المركزي السيادي.
    يقرأ رقم البوابة النشطة من ذاكرة السحاب ويستدعي ملفها المخصص فوراً.
    """
    # قراءة رقم البوابة الحالية الفعالة من الذاكرة السحابية للمنصة
    current_portal = st.session_state.get("current_portal", 1)
    
    # تحويل حركة السيرفر ديناميكياً بناءً على الزر الذي ضغط عليه المهندس
    if current_portal == 1:
        render_portal_1()
    elif current_portal == 2:
        render_portal_2()
    elif current_portal == 3:
        render_portal_3()
    elif current_portal == 4:
        render_portal_4()
    elif current_portal == 5:
        render_portal_5()
    elif current_portal == 6:
        render_portal_6()
    else:
        st.error("⚠️ خطأ في التوجيه السحابي: البوابة المطلوبة غير مدرجة في نظام المنصة.")

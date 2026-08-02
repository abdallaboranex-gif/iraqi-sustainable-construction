import streamlit as st
from utils.localization import get_text

# استدعاء الدوال الحاكمة للمحاور الخمسة المعزولة والمنظفة من نفس المجلد الفرعي
from components.profile.personal_axis import render_personal_axis
from components.profile.professional_axis import render_professional_axis
from components.profile.subscription_axis import render_subscription_axis
from components.profile.security_axis import render_security_axis
from components.profile.billing_axis import render_billing_axis

def render_user_profile_tabs():
    """
    Component: Modular Enterprise User Profile Canvas (Main Internal Orchestrator Solution).
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Maps and loads the 5 independent axes concurrently inside clean tabs frames [1.1]
    """
    
    # بناء شريط التبويبات الخمسة العصرية عالية التباين لنسخة الشركات والمستقلين
    tab_personal, tab_professional, tab_subscription, tab_security, tab_billing = st.tabs([
        get_text("Personal Info"),
        get_text("Professional Info"),
        get_text("Subscription Plan"),
        get_text("Security & Sovereign"),
        get_text("Billing Ledger")
    ])

    # 1. التبويب الأول: المعلومات الشخصية الإلزامية
    with tab_personal:
        render_personal_axis()

    # 2. التبويب الثاني: المعلومات المهنية وجهة العمل
    with tab_professional:
        render_professional_axis()
        
    # 3. التبويب الثالث: بيانات الاشتراك والمشاريع المسموحة
    with tab_subscription:
        render_subscription_axis()
        
    # 4. التبويب الرابع: تغيير كلمة المرور والـ 2FA وسجل الأجهزة
    with tab_security:
        render_security_axis()
        
    # 5. التبويب الخامس: فواتير الـ PDF، الماستر كارد، وترقية الباقات
    with tab_billing:
        render_billing_axis()

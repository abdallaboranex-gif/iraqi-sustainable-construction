import streamlit as st
from utils.localization import get_text

# استدعاء الدوال الحاكمة للمحاور من المجلد الفرعي الجديد بالتتابع البرمجي
from components.profile.personal_axis import render_personal_axis
# [المحاور القادمة سيتم فك قفل استدعائها فور صياغتها برمجياً معاً]
# from components.profile.professional_axis import render_professional_axis
# from components.profile.subscription_axis import render_subscription_axis
# from components.profile.security_axis import render_security_axis
# from components.profile.billing_axis import render_billing_axis

def render_user_profile_tabs():
    """
    Component: Modular Enterprise User Profile Canvas (Main Orchestrator).
    Strictly follows the platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Acts as a silent container that embeds decentralized sub-axes [1.1]
    """
    
    # بناء شريط التبويبات الخمسة المتفق عليها داخل نافذة حساب الشركة
    tab_personal, tab_professional, tab_subscription, tab_security, tab_billing = st.tabs([
        get_text("Personal Info"),
        get_text("Professional Info"),
        get_text("Subscription Plan"),
        get_text("Security & Sovereign"),
        get_text("Billing Ledger")
    ])

    # حقن المحور الأول المنسق بداخل التبويب المخصص له
    with tab_personal:
        render_personal_axis()

    # التبويبات المتبقية مجهزة ومحمية برسائل نصية مبسطة بانتظام لحين صياغة ملفاتها
    with tab_professional:
        st.info(get_text("Staging Context: Awaiting professional axis pipeline deployment."))
        
    with tab_subscription:
        st.info(get_text("Staging Context: Awaiting subscription axis pipeline deployment."))
        
    with tab_security:
        st.info(get_text("Staging Context: Awaiting security axis pipeline deployment."))
        
    with tab_billing:
        st.info(get_text("Staging Context: Awaiting billing axis pipeline deployment."))

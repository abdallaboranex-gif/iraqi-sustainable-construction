import streamlit as st
from utils.localization import get_text

# [تعديل المسار السيادي] استدعاء دوال المحاور من نفس المجلد الحالي المخزن محلياً
from components.profile.personal_axis import render_personal_axis
from components.profile.professional_axis import render_professional_axis

# المحاور المتبقية مجهزة وسيتم رفع الهاش عنها بالتتابع البرمجي فور صياغة ملفاتها
# from components.profile.subscription_axis import render_subscription_axis
# from components.profile.security_axis import render_security_axis
# from components.profile.billing_axis import render_billing_axis

def render_user_profile_tabs():
    """
    Component: Modular Enterprise User Profile Canvas (Main Internal Orchestrator).
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Consolidated inside components/profile/ directory for strict modular bundling [1.1]
    - Maps 5 clean business tabs instantly backed by the dual-language framework [1.1]
    """
    
    # بناء شريط التبويبات الخمسة العصرية عالية التباين لنسخة الشركات والأفراد
    tab_personal, tab_professional, tab_subscription, tab_security, tab_billing = st.tabs([
        get_text("Personal Info"),
        get_text("Professional Info"),
        get_text("Subscription Plan"),
        get_text("Security & Sovereign"),
        get_text("Billing Ledger")
    ])

    # 1. حقن المحور الشخصي الأول (الاسم، الإيميل، الهاتف، الدولة، المدينة، والصورة الاختيارية)
    with tab_personal:
        render_personal_axis()

    # 2. حقن المحور المهني الثاني (المهنة، جهة العمل مع خيار Freelance، الخبرة، والنقابة الاختياري)
    with tab_professional:
        render_professional_axis()
        
    # 3. التبويبات المتبقية مجهزة برمجياً ومحمية برسائل صامتة لحين الانتهاء من نقاش شروطها
    with tab_subscription:
        st.info(get_text("Staging Context: Awaiting subscription axis pipeline deployment."))
        
    with tab_security:
        st.info(get_text("Staging Context: Awaiting security axis pipeline deployment."))
        
    with tab_billing:
        st.info(get_text("Staging Context: Awaiting billing axis pipeline deployment."))

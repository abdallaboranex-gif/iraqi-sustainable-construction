import streamlit as st
import pandas as pd

def render_portal_5():
    """
    واجهة الباب الخامس: البنية التحتية والخدمات المساعدة.
    تدير الاشتراكات الموثقة، بوابة الدفع، وحاسبات الجدوى المالية وفترة الاسترداد.
    """
    st.markdown("<h2 style='color: #00FFCC; font-size: 22px; margin-bottom: 5px;'>💳 الباب الخامس: البنية التحتية المالية والاستشارية للمشروع</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; font-size: 13px;'>بوابة مركزية لإدارة أمان البيانات، وباقات الاشتراك الموثقة نقابياً وحكومياً، مع محرك التحليل المالي والجدوى الاقتصادية [١.١].</p>", unsafe_allow_html=True)
    
    # جلب مساحة البناء الإجمالية المحسوبة لتغذية محرك التكلفة التقديرية
    property_info = st.session_state.property_data
    gov = property_info.get("governorate", "بغداد")
    built_area = property_info.get("built_area", 150.0)
    floors = property_info.get("floors", 2)
    total_area_calc = built_area * floors
    is_compliant = property_info.get("is_compliant", True)
    
    # تقسيم الواجهة إلى شقين: البنية المالية والأمان، والحاسبات الهندسية الاقتصادية
    tab_billing, tab_financial_engine = st.tabs([
        "🔐 البنية التحتية وباقات الاشتراك والدفع", 
        "💰 محرك الجدوى المالية وفترة استرداد رأس المال"
    ])
    
    # ---------------------------------------------------------
    # الشق الأول: البنية التحتية الرقمية والدفع الإلكتروني
    # ---------------------------------------------------------
    with tab_billing:
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 12px;'>🛡️ إدارة التوثيق الرقمي والاشتراك الفعال</h4>", unsafe_allow_html=True)
        
        col_pkg, col_pay = st.columns([2, 1.5], gap="large")
        with col_pkg:
            st.markdown(
                """
                <div style='background-color: #1E293B; border: 1px solid #00FFCC; border-radius: 8px; padding: 15px;'>
                    <span style='color: #00FFCC; font-size: 11px; text-transform: uppercase; font-weight: bold;'>الباقة الحالية النشطة / Active Plan</span>
                    <h3 style='color: #F8FAFC; margin: 5px 0 0 0; font-size: 18px;'>باقة المكاتب الاستشارية والشركات الهندسية</h3>
                    <p style='color: #94A3B8; font-size: 12px; margin: 4px 0 0 0;'>تتيح معالجة ملفات الـ CAD/BIM، قراءة تقارير المختبرات بالـ OCR، وإصدار تقارير PDF حصرية ومحمية بالـ QR Code.</p>
                    <hr style='border-color: #334155; margin: 10px 0;'>
                    <span style='color: #64748B; font-size: 11px;'>حالة الحساب السيادي: <b>موثّق نقابياً ومربوط ببلديات العراق</b></span> [١.١]
                </div>
                """, 
                unsafe_allow_html=True
            )
        with col_pay:
            st.markdown("<span style='color: #94A3B8; font-size: 12px; display: block; margin-bottom: 5px;'>محفظة الدفع الإلكتروني المعتمدة للتجديد:</span>", unsafe_allow_html=True)
            pay_method = st.selectbox("اختر بوابة الدفع المحلية:", ["Zain Cash (زين كاش)", "AsiaHawala (آسيا حوالة)", "Qi Card / Visa / Mastercard"])
            st.button(f"💳 تجديد الاشتراك السنوي عبر {pay_method.split(' ')[0]}", use_container_width=True)

    # ---------------------------------------------------------
    # الشق الثاني: محرك الجدوى المالية وفترة استرداد رأس المال
    # ---------------------------------------------------------
    with tab_financial_engine:
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 15px;'>💰 الهندسة المالية وتحليل العائد الاستثماري للاستدامة</h4>", unsafe_allow_html=True)
        
        # 1. حاسبة الكلفة الإنشائية التقديرية (CapEx Calculator)
        # ضرب المساحة الكلية في متوسط سعر المتر المربع الإنشائي في السوق المحلية
        cost_per_meter = st.number_input("متوسط كلفة بناء المتر المربع الهيكلي والمشطب في السوق (ر.س):", min_value=100, value=600, step=50)
        total_capex = total_area_calc * cost_per_meter
        
        # كلفة إضافية اختيارية تفرض عند تطبيق معايير العزل والاستدامة والطاقة الشمسية
        sustainability_premium = 0
        if is_compliant:
            # افتراض كلفة إضافية لشراء مواد العزل والمنظومة الشمسية بمتوسط 80 ر.س للمتر
            sustainability_premium = total_area_calc * 80 
            
        final_capex_with_green = total_capex + sustainability_premium
        
        # 2. حاسبة كلفة التشغيل السنوية والكهرباء (OpEx Calculator)
        # إذا كان المبنى معزولاً ومطابقاً للشروط، تنخفض فواتير التشغيل السنوية بمعدل 40%
        base_opex_yearly = total_area_calc * 25 # كلفة تشغيل وخدمات وكهرباء تقديرية سنوياً بدون استدامة
        if is_compliant:
            final_opex_yearly = base_opex_yearly * 0.60 # توفير 40% من الطاقة التشغيلية بفعل العزل والألواح
        else:
            final_opex_yearly = base_opex_yearly
            
        annual_savings = base_opex_yearly - final_opex_yearly
        
        # 3. حاسبة فترة استرداد رأس المال (Payback Period Calculator)
        # قسمة الكلفة الإضافية التي دُفعت في الاستدامة على حجم التوفير المالي السنوي الناتج عنها
        if annual_savings > 0 and sustainability_premium > 0:
            payback_years = round(sustainability_premium / annual_savings, 1)
        else:
            payback_years = 0
            
        with st.container(border=True):
            st.markdown("📋 **مخرجات التحليل المالي والجدوى التشغيلية للمبنى:**")
            fc1, fc2 = st.columns(2)
            with fc1:
                st.markdown(f"الكلفة الإنشائية الأساسية للهيكل والمبنى (CapEx): **{total_capex:,.0f} ر.س**")
                st.markdown(f"الاستثمار الإضافي في تقنيات الاستدامة والعزل: **{sustainability_premium:,.0f} ر.س**")
                st.markdown(f"إجمالي كلفة البناء الكلية للمشروع المطور: **{final_capex_with_green:,.0f} ر.س**")
            with fc2:
                st.markdown(f"فاتورة التشغيل والصيانة السنوية المتوقعة (OpEx): **{final_opex_yearly:,.0f} ر.س**")
                if is_compliant:
                    st.markdown(f"حجم الوفر المالي الصافي الذي ستحققه سنوياً: <span style='color: #10B981; font-weight: bold;'>{annual_savings:,.0f} ر.س / سنة</span>", unsafe_allow_html=True)
                    st.markdown(f"⏱️ فترة استرداد رأس المال الإضافي المدفوع: <span style='color: #00FFCC; font-weight: bold; font-size: 18px;'>{payback_years} سنة</span>", unsafe_allow_html=True)
                    st.markdown("<span style='color: #64748B; font-size: 11px; display: block;'>*بعد هذه الفترة، يعتبر التوفير في الطاقة فواتير مجانية وأرباحاً صافية للمالك طوال عمر المبنى.*</span>", unsafe_allow_html=True)
                else:
                    st.markdown("<span style='color: #EF4444;'>❌ المبنى غير معزول حرارياً، لا يوجد توفير مالي وفواتير التشغيل ستكون مرتفعة جداً سنوياً.</span>", unsafe_allow_html=True)
                    
        # زر مخصص لطباعة كشف الجدوى الاقتصادية الشامل وتقديمه للمستثمرين أو الملاك
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📥 إصدار وثيقة الجدوى الاقتصادية وعائد الاستثمار (PDF Financial Report)", use_container_width=True):
            st.success("✅ جاري تجميع الحسابات الاستشارية وتوليد التقرير المالي الرسمي والجدول التحليلي المختوم بالـ QR Code المرجعي...")
            
            # تسجيل العملية وحفظها رقمياً في الصندوق الأسود السيادي للنظام
            from core.state_manager import log_action
            log_action(user="Eng. Abdulla", action_details=f"حسب دراسة الجدوى الاقتصادية وعائد الاستثمار للمشروع بفترة استرداد {payback_years} سنة.")

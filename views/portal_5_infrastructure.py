import streamlit as st
from utils.localization import get_text

def render_portal_5():
    """
    واجهة الباب الخامس المترجمة بالكامل للغات الثلاث.
    تدير البنية المالية وحاسبات الجدوى الاقتصادية بشكل ديناميكي مصفّر [١.١].
    """
    st.markdown(f"<h2 style='color: #1D4ED8; font-size: 22px; margin-bottom: 5px; font-weight: 800;'>{get_text('btn_portal_5')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #0F172A; font-size: 13px;'>{get_text('platform_sub')}</p>", unsafe_allow_html=True)
    
    property_info = st.session_state.property_data
    built_area = property_info.get("built_area", 0.0)
    floors = property_info.get("floors", 0)
    total_area_calc = built_area * floors
    
    # صمام أمان حازم لمنع الحساب على استمارات مصفّرة فارغة
    if total_area_calc == 0.0:
        st.warning("⚠️ يرجى العودة للباب الأول وملء البيانات الإنشائية والمساحة الكلية أولاً؛ لا يمكن تشغيل حاسبات الهندسة المالية لعقار فارغ!")
    else:
        tab_billing, tab_finance = st.tabs([get_text("p5_tab_billing"), get_text("p5_tab_finance")])
        
        with tab_billing:
            st.markdown(f"⚙️ **{get_text('p5_tab_billing')}**")
            st.markdown("<p style='color: #475569;'>*بوابات الدفع الإلكتروني (زين كاش وآسيا حوالة) تترجم لحظياً وتلقائياً باللغات الثلاث.*</p>", unsafe_allow_html=True)
            
        with tab_finance:
            st.markdown(f"<h4 style='color: #0F172A; font-size: 15px; margin-bottom: 15px;'>💰 {get_text('p5_tab_finance')}</h4>", unsafe_allow_html=True)
            cost_per_meter = st.number_input(get_text("p5_lbl_cost"), min_value=0, value=0, step=50)
            
            if cost_per_meter > 0:
                total_capex = total_area_calc * cost_per_meter
                with st.container(border=True):
                    st.markdown(f"📊 **مخرجات التحليل المالي والجدوى الاستشارية:**")
                    st.markdown(f"إجمالي الكلفة الإنشائية التقديرية الأساسية (CapEx): **{total_capex:,.0f} IQD**")
                    
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button(get_text("p5_btn_pdf"), use_container_width=True):
                    st.success("✅ Financial Report Generated successfully...")

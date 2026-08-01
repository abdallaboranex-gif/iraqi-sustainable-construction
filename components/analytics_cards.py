import streamlit as st

def render_side_analytics():
    """
    رسم كروت المؤشرات الستة المتقدمة في الجانب الأيمن من المنصة.
    تعرض نسب المطابقة، السلامة، توفير الطاقة، تقليل انبعاثات الكربون، والميزانية.
    """
    st.markdown("<h3 style='color: #F8FAFC; font-size: 18px; margin-bottom: 15px; font-weight: 700;'>📊 لوحة المؤشرات الحية</h3>", unsafe_allow_html=True)
    
    # 1. كرت مؤشر المطابقة الهندسية العامة (Engineering Compliance)
    with st.container(border=True):
        st.markdown(
            """
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <span style='color: #94A3B8; font-size: 11px; display: block;'>المطابقة الهندسية / Compliance</span>
                    <h2 style='color: #00FFCC; margin: 0; font-weight: 700; font-size: 26px;'>42%</h2>
                </div>
                <div style='background-color: rgba(0, 255, 204, 0.1); padding: 8px; border-radius: 6px; color: #00FFCC; font-weight: bold; font-size: 13px;'>
                    +12%
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        # رسم شريط تقدم مدمج (Progress Bar) لإعطاء انطباع مرئي متحرك داخل الكرت
        st.progress(0.42)
        
    # 2. كرت السلامة الإنشائية والامتثال للمدونة (Structural Integrity)
    with st.container(border=True):
        st.markdown(
            """
            <div>
                <span style='color: #94A3B8; font-size: 11px; display: block;'>السلامة الإنشائية / Integrity</span>
                <div style='display: flex; align-items: center; gap: 10px; margin-top: 4px;'>
                    <h2 style='color: #EF4444; margin: 0; font-weight: 700; font-size: 26px;'>0%</h2>
                    <span style='background-color: rgba(239, 68, 68, 0.1); color: #EF4444; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 600;'>
                        بانتظار فحص التربة
                    </span>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # 3. كرت استدامة الطاقة والمنظومات (Energy Optimization)
    with st.container(border=True):
        st.markdown(
            """
            <div>
                <span style='color: #94A3B8; font-size: 11px; display: block;'>استدامة الطاقة / Energy Score</span>
                <h2 style='color: #00FFCC; margin: 0; font-weight: 700; font-size: 26px;'>27%</h2>
                <span style='color: #64748B; font-size: 11px; display: block; margin-top: 2px;'>توفير متوقع في أحمال التكييف عبر العزل</span>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # 4. كرت الأثر البيئي وتقليل انبعاثات الكربون (Sustainability Impact)
    with st.container(border=True):
        st.markdown(
            """
            <div>
                <span style='color: #94A3B8; font-size: 11px; display: block;'>الأثر البيئي / Carbon Reduction</span>
                <h2 style='color: #10B981; margin: 0; font-weight: 700; font-size: 22px;'>128.5 Tons <span style='font-size: 12px; color: #64748B;'>CO₂/Year</span></h2>
                <div style='width: 100%; background-color: #334155; height: 4px; border-radius: 2px; margin-top: 8px;'>
                    <div style='width: 35%; background-color: #10B981; height: 4px; border-radius: 2px;'></div>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # 5. كرت كلفة إدارة المواد والميزانية (Cost Tracking)
    with st.container(border=True):
        st.markdown(
            """
            <div>
                <span style='color: #94A3B8; font-size: 11px; display: block;'>إدارة الكلفة الكلية / CapEx Budget</span>
                <div style='display: flex; justify-content: space-between; align-items: baseline; margin-top: 4px;'>
                    <h3 style='color: #F8FAFC; margin: 0; font-size: 16px; font-weight: 600;'>75,400 <span style='font-size: 11px; color: #64748B;'>ر.س</span></h3>
                    <span style='color: #94A3B8; font-size: 11px;'>من أصل 180K</span>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # 6. كرت الجدول الزمني المنقضي للمشروع (Timeline & Milestones)
    with st.container(border=True):
        st.markdown(
            """
            <div>
                <span style='color: #94A3B8; font-size: 11px; display: block;'>الجدول الزمني / Timeline</span>
                <div style='display: flex; justify-content: space-between; margin-top: 2px;'>
                    <span style='color: #00FFCC; font-size: 13px; font-weight: 600;'>18 يوماً منقضياً</span>
                    <span style='color: #64748B; font-size: 12px;'>المتبقي: 45 يوماً</span>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

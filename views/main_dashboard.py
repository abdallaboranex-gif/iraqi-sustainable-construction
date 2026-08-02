import streamlit as st
import datetime
import plotly.graph_objects as go
from utils.localization import get_text

def create_advanced_3d_gauge(value, max_value, suffix, color_hex):
    """
    محرك رسومي متطور يبني عداداً ثلاثي الأبعاد ذو عُمق وإضاءة حادة 
    تمنع التسطيح والتشوه البصري تماماً.
    """
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={'suffix': suffix, 'font': {'size': 18, 'color': '#0F172A', 'family': 'Inter'}},
        gauge={
            'axis': {'range': [0, max_value], 'tickwidth': 1, 'tickcolor': "#CBD5E1"},
            'bar': {'color': color_hex, 'thickness': 0.3}, # شريط القياس الملون بارز
            'bgcolor': "#F1F5F9",
            'borderwidth': 1,
            'bordercolor': "#E2E8F0",
            'steps': [
                {'range': [0, max_value], 'color': 'rgba(241, 245, 249, 0.5)'}
            ],
        }
    ))
    
    fig.update_layout(
        margin=dict(t=10, b=10, l=15, r=15),
        height=110,
        paper_bgcolor="rgba(0,0,0,0)", # دمج شفاف كامل مع بطاقة الخلفية البيضاء
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig

def render_main_dashboard():
    """
    لوحة التحكم المركزية - شاشة عرض المؤشرات ثلاثية الأبعاد فائقة التناسق.
    """
    st.markdown(
        """
        <style>
        .icon-monitor {
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://w3.org" viewBox="0 0 24 24" fill="%231D4ED8"><path d="M4 3H20C21.1 3 22 3.9 22 5V15C22 16.1 21.1 17 20 17H13V19H16V21H8V19H11V17H4C2.9 17 2 16.1 2 15V5C2 3.9 2.9 3 4 3ZM4 5V13H20V5H4Z"/></svg>');
            display: inline-block; width: 24px; height: 24px; vertical-align: middle; margin-right: 8px;
        }
        .icon-clock {
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://w3.org" viewBox="0 0 24 24" fill="%231D4ED8"><path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20ZM12.5 7V12.25L17 14.92L16.25 16.15L11 13V7H12.5Z"/></svg>');
            display: inline-block; width: 22px; height: 22px; vertical-align: middle; margin-bottom: 4px;
        }
        .icon-calendar {
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://w3.org" viewBox="0 0 24 24" fill="%231D4ED8"><path d="M9 1V3H15V1H17V3H21C21.5523 3 22 3.44772 22 4V20C22 20.5523 21.5523 21 21 21H3C2.44772 21 2 20.5523 2 20V4C2 3.44772 2.44772 3 3 3H7V1H9ZM20 11H4V19H20V11ZM7 5H4V9H20V5H17V7H15V5H9V7H7V5Z"/></svg>');
            display: inline-block; width: 22px; height: 22px; vertical-align: middle; margin-bottom: 4px;
        }
        
        .telemetry-header-card {
            background-color: #FFFFFF;
            padding: 16px;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            margin-bottom: 20px;
        }
        .telemetry-title { color: #0F172A !important; font-size: 18px; font-weight: 800; display: flex; align-items: center; gap: 8px; }
        .telemetry-desc { color: #475569 !important; font-size: 13px; margin-top: 4px; }
        
        .external-card {
            background-color: #FFFFFF;
            padding: 16px;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
            text-align: center;
        }
        .external-value { color: #1D4ED8 !important; font-size: 22px; font-weight: 800; display: flex; align-items: center; justify-content: center; gap: 8px; }
        .external-label { color: #64748B !important; font-size: 12px; font-weight: 600; margin-top: 6px; }
        
        /* بطاقة الدمج النظيفة المحدثة */
        .ring-card-combined {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 14px;
            text-align: center;
            box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.04);
        }
        .ring-card-label { color: #0F172A !important; font-size: 13px; font-weight: 700; margin-top: 8px; display: block; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # عنوان اللوحة الرئيسي
    st.markdown(
        f'''
        <div class="telemetry-header-card">
            <div class="telemetry-title"><span class="icon-monitor"></span>{get_text("Telemetry Indicators")}</div>
            <div class="telemetry-desc">{get_text("Environmental monitoring and network logs.")}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # 1. شاشة الوقت والتاريخ الحالي
    st.subheader(get_text("Time & Date"))
    
    current_moment = datetime.datetime.now()
    formatted_time = current_moment.strftime("%I:%M:%S %p")
    formatted_date = current_moment.strftime("%A, %B %d, %Y")
    
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.markdown(f'<div class="external-card"><div class="external-value"><span class="icon-clock"></span> {formatted_time}</div><div class="external-label">{get_text("Current Time")}</div></div>', unsafe_allow_html=True)
    with t_col2:
        st.markdown(f'<div class="external-card"><div class="external-value"><span class="icon-calendar"></span> {formatted_date}</div><div class="external-label">{get_text("Current Date")}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. مؤشرات الطقس ثلاثية الأبعاد المدمجة بالكامل (تم سحق الزيادات العلوية)
    target_governorate = st.session_state.property_data.get("governorate", "Baghdad")
    st.subheader(f"{get_text('Weather')} (📍 {target_governorate})")
    
    mock_temperature = 42.0 if target_governorate == "Basra" else 37.5
    mock_humidity = 18.0
    mock_wind_speed = 14.5
    
    w_col1, w_col2, w_col3 = st.columns(3)
    
    with w_col1:
        st.markdown('<div class="ring-card-combined">', unsafe_allow_html=True)
        t_color = "#EA580C" if mock_temperature >= 40.0 else "#1D4ED8"
        fig_temp = create_advanced_3d_gauge(mock_temperature, 60.0, "°C", t_color)
        st.plotly_chart(fig_temp, use_container_width=True, config={"displayModeBar": False}, key="gauge_temp_3d")
        st.markdown(f'<span class="ring-card-label">{get_text("Temperature")}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with w_col2:
        st.markdown('<div class="ring-card-combined">', unsafe_allow_html=True)
        fig_hum = create_advanced_3d_gauge(mock_humidity, 100.0, "%", "#06B6D4")
        st.plotly_chart(fig_hum, use_container_width=True, config={"displayModeBar": False}, key="gauge_hum_3d")
        st.markdown(f'<span class="ring-card-label">{get_text("Humidity")}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with w_col3:
        st.markdown('<div class="ring-card-combined">', unsafe_allow_html=True)
        fig_wind = create_advanced_3d_gauge(mock_wind_speed, 50.0, " km/h", "#10B981")
        st.plotly_chart(fig_wind, use_container_width=True, config={"displayModeBar": False}, key="gauge_wind_3d")
        st.markdown(f'<span class="ring-card-label">{get_text("Wind Speed")}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. حالة شبكة الاتصال وسرعة الاستجابة
    st.subheader(get_text("Network Status"))
    
    inf_col1, inf_col2 = st.columns(2)
    with inf_col1:
        st.metric(label=get_text("Server Latency"), value="24.2 ms")
    with inf_col2:
        st.warning(get_text("System Active: Monitoring entry logs."))

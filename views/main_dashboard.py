import streamlit as st
import datetime
import plotly.graph_objects as go
from utils.localization import get_text

def create_sovereign_gauge(value, max_value, suffix, color_hex):
    """
    مؤشر دائري مبسط يعرض القيمة في المنتصف بدون تعقيد بصري.
    """
    fig = go.Figure(go.Pie(
        values=[value, max_value - value],
        hole=0.75,
        direction="clockwise",
        sort=False,
        marker=dict(colors=[color_hex, "#E2E8F0"]),
        showlegend=False,
        hoverinfo="none",
        textinfo="none"
    ))
    
    fig.update_layout(
        margin=dict(t=5, b=5, l=5, r=5),
        height=130,
        width=130,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    
    fig.add_annotation(
        text=f"<b style='color:#0F172A; font-size:16px;'>{value}{suffix}</b>",
        x=0.5, y=0.5, showarrow=False
    )
    return fig

def render_main_dashboard():
    """
    عرض الوقت والتاريخ والطقس الحالي باستخدام أيقونات SVG مسطحة وعصرية.
    """
    st.markdown(
        """
        <style>
        /* تعريف الأيقونات كخلفيات مسطحة نظيفة ومدمجة */
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
        
        .ring-card-combined {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 16px;
            text-align: center;
            box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.04);
        }
        .ring-card-label { color: #0F172A !important; font-size: 13px; font-weight: 700; margin-top: 10px; display: block; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # عنوان اللوحة الرئيسي المحدث بأيقونة مسطحة هندسية
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

    # 2. مؤشرات الطقس الدائرية المدمجة كلياً داخل حاوية متناسقة وموحدة
    target_governorate = st.session_state.property_data.get("governorate", "Baghdad")
    st.subheader(f"{get_text('Weather')} (📍 {target_governorate})")
    
    mock_temperature = 42.0 if target_governorate == "Basra" else 37.5
    mock_humidity = 18.0
    mock_wind_speed = 14.5
    
    w_col1, w_col2, w_col3 = st.columns(3)
    
    with w_col1:
        st.markdown('<div class="ring-card-combined">', unsafe_allow_html=True)
        t_color = "#EA580C" if mock_temperature >= 40.0 else "#1D4ED8"
        fig_temp = create_sovereign_gauge(mock_temperature, 60.0, "°C", t_color)
        st.plotly_chart(fig_temp, use_container_width=True, config={"displayModeBar": False}, key="gauge_temp_plot")
        st.markdown(f'<span class="ring-card-label">{get_text("Temperature")}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with w_col2:
        st.markdown('<div class="ring-card-combined">', unsafe_allow_html=True)
        fig_hum = create_sovereign_gauge(mock_humidity, 100.0, "%", "#06B6D4")
        st.plotly_chart(fig_hum, use_container_width=True, config={"displayModeBar": False}, key="gauge_hum_plot")
        st.markdown(f'<span class="ring-card-label">{get_text("Humidity")}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with w_col3:
        st.markdown('<div class="ring-card-combined">', unsafe_allow_html=True)
        fig_wind = create_sovereign_gauge(mock_wind_speed, 50.0, " km/h", "#10B981")
        st.plotly_chart(fig_wind, use_container_width=True, config={"displayModeBar": False}, key="gauge_wind_plot")
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

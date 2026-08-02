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
    عرض الوقت والتاريخ الحالي مع مؤشرات الطقس الدائرية المتناسقة وحالة الشبكة.
    """
    st.markdown(
        """
        <style>
        .telemetry-header-card {
            background-color: #FFFFFF;
            padding: 16px;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            margin-bottom: 20px;
        }
        .telemetry-title { color: #0F172A !important; font-size: 18px; font-weight: 800; }
        .telemetry-desc { color: #475569 !important; font-size: 13px; }
        
        .external-card {
            background-color: #FFFFFF;
            padding: 14px;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
            text-align: center;
        }
        .external-value { color: #1D4ED8 !important; font-size: 22px; font-weight: 800; }
        .external-label { color: #64748B !important; font-size: 12px; font-weight: 600; margin-top: 4px; }
        
        /* حاوية موحدة تجمع الدائرة والنص معاً لمنع التفكك البصري */
        .ring-card-combined {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 16px;
            text-align: center;
            box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.04);
        }
        .ring-card-label {
            color: #0F172A !important;
            font-size: 13px;
            font-weight: 700;
            margin-top: 10px;
            display: block;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # عنوان اللوحة الرئيسي
    st.markdown(
        f'''
        <div class="telemetry-header-card">
            <div class="telemetry-title">🖥️ {get_text("Telemetry Indicators")}</div>
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
        st.markdown(f'<div class="external-card"><div class="external-value">⏰ {formatted_time}</div><div class="external-label">{get_text("Current Time")}</div></div>', unsafe_allow_html=True)
    with t_col2:
        st.markdown(f'<div class="external-card"><div class="external-value">📅 {formatted_date}</div><div class="external-label">{get_text("Current Date")}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. مؤشرات الطقس الدائرية المدمجة كلياً داخل حاوية متناسقة وموحدة
    target_governorate = st.session_state.property_data.get("governorate", "Baghdad")
    st.subheader(f"{get_text('Weather')} (📍 {target_governorate})")
    
    mock_temperature = 42.0 if target_governorate == "Basra" else 37.5
    mock_humidity = 18.0
    mock_wind_speed = 14.5
    
    w_col1, w_col2, w_col3 = st.columns(3)
    
    with w_col1:
        # فتح حاوية البطاقة الموحدة للمؤشر الأول
        st.markdown('<div class="ring-card-combined">', unsafe_allow_html=True)
        t_color = "#EA580C" if mock_temperature >= 40.0 else "#1D4ED8"
        fig_temp = create_sovereign_gauge(mock_temperature, 60.0, "°C", t_color)
        st.plotly_chart(fig_temp, use_container_width=True, config={"displayModeBar": False}, key="gauge_temp_plot")
        # كتابة النص فوراً قبل إغلاق الحاوية لضمان ثباته بالداخل
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

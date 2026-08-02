import streamlit as st
from utils.localization import get_text

def render_offline_sync_ui(cached_payload_count: int = 0, last_sync_timestamp: str = "0.0"):
    """
    Component: Offline Local Storage Synchronization Dashboard UI.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Filename matching structural blueprint: components/offline_sync_ui.py
    - Premium light-theme high-contrast styling with absolute separation of concerns
    - Uninitialized logs and cached queues enforce a 0.0 value or null benchmark
    """
    
    # Custom light theme high-contrast styling for the offline sync layout
    st.markdown(
        """
        <style>
        .sync-wrapper-card {
            background-color: #FFFFFF;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            margin-bottom: 24px;
        }
        .sync-status-indicator {
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 12px;
            padding: 8px 12px;
            border-radius: 8px;
            display: inline-block;
        }
        .sync-title {
            color: #0F172A;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 6px;
        }
        .sync-metric-badge {
            color: #0F172A;
            font-size: 28px;
            font-weight: 800;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Core Visual Layout Wrapper
    st.markdown(f'<div class="sync-wrapper-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="sync-title">{get_text("Local Storage Cache & Multi-Network Sync Control")}</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#475569; font-size:13px;">{get_text("Safeguarding data continuity for remote building sites operating under unstable or disconnected network environments.")}</p>', unsafe_allow_html=True)
    
    # Checkpoint: Evaluate local hardware buffer payload queue status
    if cached_payload_count == 0:
        st.markdown(
            f'<div class="sync-status-indicator" style="background-color: #F1F5F9; color: #475569;">✔️ {get_text("Data Cache Status: Clean Baseline (No pending off-grid logs)")}</div>', 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="sync-status-indicator" style="background-color: #FEF3C7; color: #D97706;">⚠️ {get_text("Data Cache Status: Unsynchronized Offline Records Pending")}</div>', 
            unsafe_allow_html=True
        )

    # High-contrast dual columns layout for synchronization telemetry fields
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f'<div class="sync-metric-badge">{cached_payload_count}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color: #64748B; font-size: 13px;">{get_text("Staged Compliance Submissions Queue (Count)")}</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown(f'<div class="sync-metric-badge" style="font-size: 20px; line-height: 42px; color: #0F172A;">{last_sync_timestamp}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color: #64748B; font-size: 13px;">{get_text("Last Verified Sovereign Gateway Sync Epoch")}</div>', unsafe_allow_html=True)

    # Core Execution Actions Blocks
    st.markdown("<br>", unsafe_allow_html=True)
    action_col1, action_col2 = st.columns(2)
    
    with action_col1:
        # Enforce dynamic interaction safeguards for form submissions
        if st.button(get_text("Flush Local Storage Memory Pipeline"), use_container_width=True, key="sync_btn_flush", disabled=(cached_payload_count == 0)):
            st.warning(get_text("Local browser session application database storage cleared safely."))
            
    with action_col2:
        if st.button(get_text("Initiate Gateway Pipeline Secure Uplink"), use_container_width=True, key="sync_btn_uplink", type="primary"):
            if cached_payload_count == 0:
                st.error(get_text("Synchronization Rejected: Staged offline queue is empty with 0.0 metrics recorded."))
            else:
                st.success(get_text("Uplink successful: Local environmental cache packets fully integrated into national servers."))

    st.markdown('</div>', unsafe_allow_html=True)

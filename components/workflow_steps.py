import streamlit as st
from utils.localization import get_text

def render_workflow_steps(current_step_index: int = 0):
    """
    Component: Sovereign Engineering Workflow Progress & Auditing Steps UI.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Filename matching structural blueprint: components/workflow_steps.py
    - Premium light-theme high-contrast styling with absolute separation of concerns
    - Default uninitialized steps index initializes at clean 0 state baseline
    """
    
    # Custom light theme high-contrast styling for the workflow progression array
    st.markdown(
        """
        <style>
        .workflow-container {
            background-color: #FFFFFF;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            margin-bottom: 24px;
        }
        .workflow-step-box {
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            font-size: 13px;
            font-weight: 600;
            border: 1px solid #E2E8F0;
        }
        .step-active {
            background-color: #0F172A;
            color: #FFFFFF;
            border-color: #0F172A;
        }
        .step-pending {
            background-color: #F8FAFC;
            color: #64748B;
        }
        .step-completed {
            background-color: #F1F5F9;
            color: #0F172A;
            border-color: #CBD5E1;
            text-decoration: line-through;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sovereign Blueprint Steps Configuration Matrix (Pure English Keys)
    workflow_steps_keys = [
        "Data Canvas Submission",
        "Automated OCR Verification",
        "GIS Environmental Clearance",
        "National Committee Audit",
        "Sovereign Green Certification"
    ]

    st.markdown('<div class="workflow-container">', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#0F172A; font-size:15px; font-weight:700; margin-bottom:16px;">{get_text("Project Compliance Evaluation Pipeline Status")}</p>', unsafe_allow_html=True)

    # Render localized progress alignment pillars dynamically using pure columns layout
    cols = st.columns(len(workflow_steps_keys))
    
    for index, step_key in enumerate(workflow_steps_keys):
        with cols[index]:
            # Structural state conditional execution switcher
            if index < current_step_index:
                style_class = "step-completed"
                prefix = "✔️ "
            elif index == current_step_index:
                style_class = "step-active"
                prefix = "⚡ "
            else:
                style_class = "step-pending"
                prefix = "⏳ "
                
            st.markdown(
                f'<div class="workflow-step-box {style_class}">{prefix}{get_text(step_key)}</div>', 
                unsafe_allow_html=True
            )
            
    st.markdown('</div>', unsafe_allow_html=True)

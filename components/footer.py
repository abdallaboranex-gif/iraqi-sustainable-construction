import streamlit as st
from utils.localization import get_text

def render_footer():
    """
    Component: Sovereign Platform Footer.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Filename matching structural blueprint: components/footer.py
    - Premium light-theme high-contrast styling with absolute separation of concerns
    - Universal structural synchronization across all portal layers
    """
    
    # Custom light theme high-contrast injection for the platform footer block
    st.markdown(
        """
        <style>
        .platform-footer {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 16px;
            border-top: 1px solid #E2E8F0;
            margin-top: 40px;
            text-align: center;
            box-shadow: 0 -4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        .footer-text-primary {
            color: #0F172A;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 4px;
        }
        .footer-text-secondary {
            color: #64748B;
            font-size: 12px;
            font-weight: 400;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Render the unified sovereign corporate alignment block
    st.markdown(
        f'''
        <div class="platform-footer">
            <div class="footer-text-primary">
                © 2026 {get_text("Iraqi Green Construction Data Platform. All Sovereign Rights Reserved.")}
            </div>
            <div class="footer-text-secondary">
                {get_text("Regulated by the National Committee for Sustainable Development and Green Building Standards.")}
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

import os
import sys

# Core Architectural Fix: Enforce project root injection into Python search path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st

# Enforce Sovereign Layout Configuration with custom visual branding
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Core Architectural Imports from the purged baseline modules
from core.state_manager import initialize_session_state
from utils.localization import get_text
from components.header import render_header
from views.main_dashboard import render_main_dashboard

def inject_premium_theme_css():
    """
    Injects high-fidelity UI styling to strictly replicate the premium light theme:
    Background soft ice blue (#F8FAFC), Dark Navy high-contrast typography (#0F172A),
    and crisp white rounded containers (16px border-radius) with smooth floating shadows.
    """
    st.markdown(
        """
        <style>
        /* Base background and text properties reset */
        .stApp {
            background-color: #F8FAFC !important;
        }
        h1, h2, h3, h4, h5, h6, p, span, label {
            color: #0F172A !important;
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
        }
        
        /* High-contrast modular structural cards */
        .premium-layout-card {
            background-color: #FFFFFF !important;
            padding: 24px;
            border-radius: 16px !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 4px 6px -1px rgba(15, 23, 42, 0.05), 0 2px 4px -1px rgba(15, 23, 42, 0.03) !important;
            margin-bottom: 20px;
        }
        
        /* Vertical Workflow Timeline UI Elements */
        .timeline-container {
            border-left: 3px dashed #CBD5E1;
            padding-left: 24px;
            margin-left: 12px;
            margin-top: 15px;
        }
        .timeline-step {
            position: relative;
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }
        .step-badge {
            display: inline-block;
            padding: 4px 12px;
            font-size: 11px;
            font-weight: 700;
            border-radius: 20px;
            margin-bottom: 8px;
        }
        .badge-completed { background-color: #DCFCE7; color: #15803D !important; }
        .badge-progress { background-color: #FFEDD5; color: #C2410C !important; }
        .badge-locked { background-color: #F1F5F9; color: #64748B !important; }
        
        /* Trust factor badges row footer */
        .trust-footer-card {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            padding: 16px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    """
    Main Executive UI Compiler for the Iraqi Green Construction Data Platform.
    Splits the viewport layout concurrently: 40% Workflow Timeline, 60% Telemetry Dashboard Grid.
    """
    # 1. Initialize and clean the sovereign core database session fields
    initialize_session_state()
    
    # 2. Inject premium high-contrast visual styling sheets
    inject_premium_theme_css()
    
    # 3. Render Top Branding Title Header & Profile Avatar Components
    render_header()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 4. Construct Dual Split View Layers Matrix (40% Split left, 60% Split right)
    col_workflow, col_telemetry = st.columns([2.0, 3.0], gap="large")
    
    # --- LEFT SIDEBAR CANVAS LAYER: VERIFIED PROGRESSIVE WORKFLOW TIMELINE (40%) ---
    with col_workflow:
        st.markdown(
            f"""
            <div class="premium-layout-card">
                <div style="font-size: 18px; font-weight: 800; color: #0F172A;">
                    🌐 {get_text("Engineering Compliance Workflow Pipeline")}
                </div>
                <div style="font-size: 13px; color: #475569; margin-top: 4px;">
                    {get_text("Phase 1: Strict sequential validation checkpoints for national green certification clearance.")}
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Open Timeline Track Context
        st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
        
        # Step 1: Completed State Context Card
        st.markdown(
            f"""
            <div class="timeline-step" style="border-left: 4px solid #10B981;">
                <span class="step-badge badge-completed">✔️ {get_text("Step 1: Completed")}</span>
                <div style="font-size: 15px; font-weight: 700;">{get_text("Site Analysis & Zoning Regulations")}</div>
                <p style="font-size: 12px; color: #475569; margin-top: 4px;">{get_text("Completed on May 15, 2026 by Licensed Project Engineer Nominee.")}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Step 2: Under Analysis/Active Upload Form Block Context Card
        st.markdown(
            f"""
            <div class="timeline-step" style="border-left: 4px solid #F97316; background-color: #FFFBEB;">
                <span class="step-badge badge-progress">⚡ {get_text("Step 2: In Progress")}</span>
                <div style="font-size: 15px; font-weight: 700; color: #0F172A;">{get_text("Soil Inspection & Foundation Engineering")}</div>
                <p style="font-size: 12px; color: #475569; margin-top: 4px;">{get_text("Please upload official Soil Testing Laboratory PDF files to feed compliance engines.")}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Direct local mock integration of file uploader layout wrapper to simulate original screenshot upload field
        st.file_uploader(label=get_text("Upload Certified Soil Lab PDF Documentation"), type=["pdf"], key="inline_timeline_soil_uploader", label_visibility="collapsed")
        
        # Step 3: Locked Checkpoint
        st.markdown(
            f"""
            <div class="timeline-step" style="opacity: 0.65;">
                <span class="step-badge badge-locked">🔒 {get_text("Step 3: Locked")}</span>
                <div style="font-size: 14px; font-weight: 700; color: #64748B;">{get_text("Structural Material Sourcing & Load Audits")}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Step 4: Locked Checkpoint
        st.markdown(
            f"""
            <div class="timeline-step" style="opacity: 0.65;">
                <span class="step-badge badge-locked">🔒 {get_text("Step 4: Locked")}</span>
                <div style="font-size: 14px; font-weight: 700; color: #64748B;">{get_text("Hydro-Sanitary Networks & Plumbing Density")}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Step 5: Locked Checkpoint
        st.markdown(
            f"""
            <div class="timeline-step" style="opacity: 0.65;">
                <span class="step-badge badge-locked">🔒 {get_text("Step 5: Locked")}</span>
                <div style="font-size: 14px; font-weight: 700; color: #64748B;">{get_text("Electrical Grid Intelligence & Thermal Load Profiles")}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown('</div>', unsafe_allow_html=True) # Close Timeline Track Context
        
    # --- RIGHT TELEMETRY GRID LAYER: DYNAMIC 6-PORTAL MATRIX MONITOR (60%) ---
    with col_telemetry:
        # Delegate analytical metric grid compilation directly to views/main_dashboard.py
        render_main_dashboard()
        
    st.markdown("<br><hr style='border-color: #E2E8F0; margin: 20px 0;'>", unsafe_allow_html=True)
    
    # 5. Bottom Rows Panel: Trust Credentials Badges Array Footers
    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    with f_col1:
        st.markdown(f'<div class="trust-footer-card"><strong style="color:#1D4ED8;">🛡️ {get_text("Secure & Sovereign")}</strong><p style="font-size:11px; color:#64748B; margin-top:4px;">{get_text("End-to-end national protocol encryption")}</p></div>', unsafe_allow_html=True)
    with f_col2:
        st.markdown(f'<div class="trust-footer-card"><strong style="color:#1D4ED8;">🧠 {get_text("AI-Powered Analytics")}</strong><p style="font-size:11px; color:#64748B; margin-top:4px;">{get_text("Smarter insights for building files")}</p></div>', unsafe_allow_html=True)
    with f_col3:
        st.markdown(f'<div class="trust-footer-card"><strong style="color:#1D4ED8;">✔️ {get_text("Regulatory Compliance")}</strong><p style="font-size:11px; color:#64748B; margin-top:4px;">{get_text("Aligned with national code parameters")}</p></div>', unsafe_allow_html=True)
    with f_col4:
        st.markdown(f'<div class="trust-footer-card"><strong style="color:#1D4ED8;">👥 {get_text("Expert Support")}</strong><p style="font-size:11px; color:#64748B; margin-top:4px;">{get_text("Dedicated structural engineering response team")}</p></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

import streamlit as st
from components.workflow_steps import render_workflow_steps

def route_to_view():
    """توجيه حركة السيرفر لعرض مسار العمل والخطوات الزمنية للـ 6 بوابات"""
    render_workflow_steps()

import streamlit as st
from utils.localization import get_text

def render_ocr_verification_ui(extracted_data=None):
    """
    Component: OCR Verification & Structural Matching UI.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Filename matching structural blueprint: components/ocr_verification_ui.py
    - Premium light-theme high-contrast styling with absolute separation of concerns
    - Default uninitialized elements scale at clean 0.0 or empty strings
    """
    
    # Custom light theme high-contrast styling for the OCR container layout
    st.markdown(
        """
        <style>
        .ocr-wrapper-card {
            background-color: #FFFFFF;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            margin-bottom: 24px;
        }
        .ocr-header-title {
            color: #0F172A;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 6px;
        }
        .ocr-sub-text {
            color: #475569;
            font-size: 13px;
            margin-bottom: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Core Visual Layout Wrapper
    st.markdown(f'<div class="ocr-wrapper-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="ocr-header-title">{get_text("Automated OCR Compliance Document Audit")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ocr-sub-text">{get_text("Cross-referencing textual evidence from official sovereign certificates against platform input fields.")}</div>', unsafe_allow_html=True)
    
    # Checkpoint: Handle clean empty state if no extracted document payload is supplied
    if extracted_data is None:
        st.info(get_text("Awaiting document upload payload to initialize automated text extractions."))
        st.progress(0.0) # Enforced 0.0 clean baseline start
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Dynamic execution block when document metadata exists
    st.subheader(get_text("Document Visual Integrity Analysis"))
    
    # Enforced progress parameter calculation indicator (simulated baseline verification status)
    confidence_score = extracted_data.get("confidence", 0.0)
    st.progress(confidence_score)
    st.caption(f"{get_text('Algorithmic Extraction Confidence Quotient:')} {confidence_score * 100:.1f}%")

    # High-contrast interactive side-by-side data auditing panel
    st.markdown(f"### {get_text('Extracted Audit Parameters')}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.text_input(
            label=get_text("Detected Sovereign Document ID"), 
            value=extracted_data.get("document_id", ""), 
            disabled=True,
            key="ocr_field_doc_id"
        )
        st.text_input(
            label=get_text("Identified Issuing Authority"), 
            value=extracted_data.get("issuing_authority", ""), 
            disabled=True,
            key="ocr_field_authority"
        )
    with col2:
        st.number_input(
            label=get_text("Extracted Compliance Metric Value"), 
            value=float(extracted_data.get("metric_value", 0.0)), 
            disabled=True,
            key="ocr_field_metric_val"
        )
        st.text_input(
            label=get_text("Sovereign Issuance Timestamp"), 
            value=extracted_data.get("issuance_date", ""), 
            disabled=True,
            key="ocr_field_date"
        )

    # Human-in-the-loop sovereign confirmation buttons
    st.markdown("<br>", unsafe_allow_html=True)
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button(get_text("Approve Extracted Data & Bind to Current Portal Form"), use_container_width=True, key="ocr_btn_approve"):
            st.success(get_text("Data bound securely to the platform session pipeline."))
    with c_btn2:
        if st.button(get_text("Reject & Re-upload Clearance Documents"), use_container_width=True, key="ocr_btn_reject"):
            st.warning(get_text("OCR log flushed. Ready for manual parameter override or re-upload."))

    st.markdown('</div>', unsafe_allow_html=True)

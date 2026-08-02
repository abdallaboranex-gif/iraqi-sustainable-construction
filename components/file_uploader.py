import streamlit as st
from utils.localization import get_text

def render_file_uploader(uploader_key: str, allowed_extensions=["pdf", "png", "jpg", "jpeg"]):
    """
    Component: Sovereign File Uploader Core.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Filename matching structural blueprint: components/file_uploader.py
    - Premium light-theme high-contrast styling with absolute separation of concerns
    - Enforced baseline safeguards to reject empty uploads or malicious extensions
    """
    
    # Custom light theme high-contrast injection for the upload container area
    st.markdown(
        """
        <style>
        .uploader-container {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 16px;
            border: 2px dashed #CBD5E1;
            margin-bottom: 20px;
            text-align: center;
        }
        .uploader-hint {
            color: #64748B;
            font-size: 13px;
            margin-top: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Wrap the uploader in a clean visual layout container
    st.markdown(f'<div class="uploader-container">', unsafe_allow_html=True)
    
    # Core Streamlit File Uploader component using Pure English labels
    uploaded_file = st.file_uploader(
        label=get_text("Upload Official Construction Compliance Document / Architectural Blueprint"),
        type=allowed_extensions,
        key=f"file_uploader_{uploader_key}",
        label_visibility="visible"
    )
    
    # Render dynamic local structural hints via the translation engine
    extensions_hint = ", ".join(allowed_extensions).upper()
    st.markdown(
        f'<div class="uploader-hint">{get_text("Authorized Formats:")} {extensions_hint} | {get_text("Maximum Permissible File Size: 10MB")}</div>',
        unsafe_allow_html=True
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Strict Validation Layer & Verification Checkpoints
    if uploaded_file is not None:
        # Safeguard 1: Verify file contents are not completely empty (0 bytes)
        if uploaded_file.size == 0:
            st.error(get_text("Upload Exception: The submitted file is completely empty or corrupted."))
            return None
            
        # Safeguard 2: Enforce strict byte-size barrier constraint (10 Megabytes)
        max_bytes = 10 * 1024 * 1024
        if uploaded_file.size > max_bytes:
            st.error(get_text("Upload Exception: File size exceeds the sovereign 10MB data pipeline limit."))
            return None

        # Success checkpoint verification confirmation
        st.success(f"✔️ {get_text('File securely staged in buffer memory:')} {uploaded_file.name}")
        return uploaded_file
        
    return None

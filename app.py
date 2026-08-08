import streamlit as st
import os
import sys
from PIL import Image

# Ensure Python can find your backend files inside the 'app' folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app.main_orchestrator import run_orchestration # Adjust if your main function has a different name
    backend_ready = True
except ImportError:
    backend_ready = False

# Page Setup
st.set_page_config(page_title="MaanakAI Demo Portal", page_icon="🛡️", layout="wide")

st.title("🛡️ MaanakAI: Intelligent Compliance Orchestrator")
st.markdown("### Live FSSAI Label Audit & Regulatory Shield Demo")

# Sidebar navigation
app_mode = st.sidebar.selectbox("Select Portal Mode", ["B2B Manufacturer Portal", "B2C Consumer Trust Engine"])

# --- B2B MANUFACTURER PORTAL ---
if app_mode == "B2B Manufacturer Portal":
    st.header("🏭 B2B Compliance & Audit Dashboard")
    st.write("Snap a product label using your phone camera or upload an image file to test your compliance engine.")

    input_method = st.radio("Choose Input Method", ["Use Phone Camera / Webcam", "Upload Image File"])
    
    label_image = None

    if input_method == "Use Phone Camera / Webcam":
        camera_file = st.camera_input("Capture product label")
        if camera_file is not None:
            label_image = Image.open(camera_file)
    else:
        uploaded_file = st.file_uploader("Upload Label Image (PNG, JPG)", type=["png", "jpg", "jpeg"])
        if uploaded_file is not None:
            label_image = Image.open(uploaded_file)

    if label_image is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Captured Label Preview")
            st.image(label_image, use_container_width=True)

        with col2:
            st.subheader("AI Audit Engine Output")
            
            if st.button("Run Compliance Audit"):
                with st.spinner("Processing through MaanakAI backend engine..."):
                    
                    # If you want to temporarily save the image for your backend script to read:
                    temp_path = "temp_label.jpg"
                    label_image.save(temp_path)
                    
                    # --- HOOK YOUR BACKEND HERE ---
                    # If your backend code processes files directly, call it here.
                    
                    st.success("Audit Completed Successfully!")
                    
                    # Display results metrics with expanded width for m1 to prevent text clipping
                    m1, m2 = st.columns([1.5, 1])
                    m1.metric("Compliance Status", "REVIEW REQUIRED", delta="1 Flagged Claim", delta_color="inverse")
                    m2.metric("Execution Time", "0.41s")

                    st.markdown("#### Audit Breakdown:")
                    st.markdown("- **FSSAI License #:** ✅ PASS")
                    st.markdown("- **Batch & Expiry:** ✅ PASS")
                    st.markdown("- **Absolute / '100%' Claims:** ❌ FAIL (Flagged by Guardrails)")

                    # Mock Report Download
                    st.download_button(
                        label="Download Official Audit Report (PDF)",
                        data=b"Mock PDF Report Content",
                        file_name="MaanakAI_Audit_Report.pdf",
                        mime="application/pdf"
                    )

# --- B2C CONSUMER TRUST ENGINE ---
elif app_mode == "B2C Consumer Trust Engine":
    st.header("🛒 Consumer Trust & Transparency Scanner")
    st.write("Scan any product label with your camera to check its safety score and manufacturer verification.")
    
    consumer_cam = st.camera_input("Scan product label")
    if consumer_cam is not None:
        st.info("Cross-referencing batch data against B2B ledger...")
        st.error("⚠️ CAUTION: Absolute marketing descriptor detected")
        st.markdown("**Status:** Verified FBO Partner - Core compliance validated.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>MaanakAI Live Demo Environment</p>", unsafe_allow_html=True)
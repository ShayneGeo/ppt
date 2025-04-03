import streamlit as st
import requests
import tempfile
import os
import subprocess
from pdf2image import convert_from_path

def main():
    st.title("Display PPT Slides as Images from GitHub")
    ppt_url = "https://github.com/ShayneGeo/ppt/raw/refs/heads/main/NIROPS_DatasetDescription.pptx"

    if "images" not in st.session_state:
        st.session_state.images = []
        st.session_state.current_slide = 0

    if st.button("Load PPT from GitHub"):
        response = requests.get(ppt_url)
        if response.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pptx") as tmp:
                tmp.write(response.content)
                ppt_path = tmp.name

            # Convert PPTX to PDF using LibreOffice (requires LibreOffice installed)
            output_dir = os.path.dirname(ppt_path)
            subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", ppt_path, "--outdir", output_dir], check=True)
            pdf_path = ppt_path.replace(".pptx", ".pdf")

            # Convert PDF pages to images using pdf2image (requires pdf2image and poppler)
            images = convert_from_path(pdf_path)
            st.session_state.images = images
            st.session_state.current_slide = 0
        else:
            st.error("Failed to download PPT from GitHub")

    if st.session_state.images:
        total_slides = len(st.session_state.images)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous", disabled=(st.session_state.current_slide == 0)):
                st.session_state.current_slide -= 1
        with col2:
            if st.button("Next", disabled=(st.session_state.current_slide == total_slides - 1)):
                st.session_state.current_slide += 1

        st.write(f"Slide {st.session_state.current_slide + 1} of {total_slides}")
        st.image(st.session_state.images[st.session_state.current_slide], use_column_width=True)

if __name__ == "__main__":
    main()

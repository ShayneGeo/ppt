import streamlit as st
import requests
from pptx import Presentation
import tempfile

def main():
    st.title("PPT from GitHub Demo")

    # Replace this URL with the direct "raw" link to your PPT file in GitHub
    ppt_github_url = "https://github.com/ShayneGeo/ppt/raw/refs/heads/main/NIROPS_DatasetDescription.pptx"

    if st.button("Load PPT from GitHub"):
        response = requests.get(ppt_github_url)
        if response.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pptx") as tmp:
                tmp.write(response.content)
                tmp_path = tmp.name

            pres = Presentation(tmp_path)
            for i, slide in enumerate(pres.slides):
                st.subheader(f"Slide {i+1}")
                slide_text = ""
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        slide_text += shape.text + "\n"
                st.write(slide_text)
        else:
            st.error("Failed to download PPT from GitHub")

if __name__ == "__main__":
    main()

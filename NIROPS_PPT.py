# import streamlit as st
# import urllib.parse
# import streamlit.components.v1 as components

# def load_file_viewer(file_url, file_type):
#     encoded_url = urllib.parse.quote(file_url, safe='')
    
#     if file_type == "pptx":
#         viewer_url = f"https://view.officeapps.live.com/op/embed.aspx?src={encoded_url}"
#     elif file_type == "pdf":
#         viewer_url = f"https://docs.google.com/gview?embedded=true&url={encoded_url}"
#     else:
#         st.error("Unsupported file type")
#         return

#     html_code = f"""
#     <html>
#     <head>
#         <meta name="viewport" content="width=device-width, initial-scale=1">
#         <style>
#             html, body {{
#                 margin: 0;
#                 padding: 0;
#                 height: 100%;
#                 overflow: hidden;
#             }}
#             iframe {{
#                 border: none;
#                 width: 100%;
#                 height: 100vh;
#             }}
#         </style>
#     </head>
#     <body>
#         <iframe src="{viewer_url}"></iframe>
#     </body>
#     </html>
#     """
#     components.html(html_code, height=800)

# def main():
#     st.title("Viewer for PPTX and PDF Files")

#     ppt_options = {
#         "NIROPS Dataset Description (PPTX)": ("https://github.com/ShayneGeo/ppt/raw/refs/heads/main/NIROPS_DatasetDescription.pptx", "pptx"),
#         "Black Bear Bark Thesis (PDF)": ("https://github.com/ShayneGeo/ppt/raw/refs/heads/main/BlackBearBark_ThesisDefense_PPT.pdf", "pdf"),
#     }

#     for label, (url, ftype) in ppt_options.items():
#         if st.button(f"Start Viewer - {label}", key=label):
#             load_file_viewer(url, ftype)

# if __name__ == "__main__":
#     main()

















import streamlit as st
import requests
import fitz  # PyMuPDF
import tempfile
from PIL import Image

def load_pdf_pages(pdf_url):
    response = requests.get(pdf_url)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(response.content)
        pdf_path = tmp_file.name

    doc = fitz.open(pdf_path)
    pages = []
    for page_num in range(len(doc)):
        pix = doc.load_page(page_num).get_pixmap(dpi=150)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        pages.append(img)
    return pages

def main():
    st.title("PDF Viewer with Clickable Pages")

    pdf_url = "https://github.com/ShayneGeo/ppt/raw/refs/heads/main/BlackBearBark_ThesisDefense_PPT.pdf"

    if "pdf_pages" not in st.session_state:
        st.session_state.pdf_pages = []
        st.session_state.current_page = 0

    if st.button("Load PDF"):
        st.session_state.pdf_pages = load_pdf_pages(pdf_url)
        st.session_state.current_page = 0

    if st.session_state.pdf_pages:
        total = len(st.session_state.pdf_pages)
        st.image(st.session_state.pdf_pages[st.session_state.current_page], use_column_width=True)
        col1, col2 = st.columns(2)
        with col1:
            st.button("Previous", on_click=lambda: st.session_state.update(current_page=max(0, st.session_state.current_page - 1)), disabled=st.session_state.current_page == 0)
        with col2:
            st.button("Next", on_click=lambda: st.session_state.update(current_page=min(total - 1, st.session_state.current_page + 1)), disabled=st.session_state.current_page == total - 1)
        st.caption(f"Page {st.session_state.current_page + 1} of {total}")

if __name__ == "__main__":
    main()











import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

def load_file_viewer(file_url, file_type):
    encoded_url = urllib.parse.quote(file_url, safe='')
    
    if file_type == "pptx":
        viewer_url = f"https://view.officeapps.live.com/op/embed.aspx?src={encoded_url}"
    elif file_type == "pdf":
        viewer_url = f"https://docs.google.com/gview?embedded=true&url={encoded_url}"
    else:
        st.error("Unsupported file type")
        return

    html_code = f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                height: 100%;
                overflow: hidden;
            }}
            iframe {{
                border: none;
                width: 100%;
                height: 100vh;
            }}
        </style>
    </head>
    <body>
        <iframe src="{viewer_url}"></iframe>
    </body>
    </html>
    """
    components.html(html_code, height=800)

def main():
    st.title("Viewer for PPTX and PDF Files")

    ppt_options = {
        "NIROPS Dataset Description (PPTX)": ("https://github.com/ShayneGeo/ppt/raw/refs/heads/main/NIROPS_DatasetDescription.pptx", "pptx"),
        "Black Bear Bark Thesis (PDF)": ("https://github.com/ShayneGeo/ppt/raw/refs/heads/main/BlackBearBark_ThesisDefense_PPT.pdf", "pdf"),
    }

    for label, (url, ftype) in ppt_options.items():
        if st.button(f"Start Viewer - {label}", key=label):
            load_file_viewer(url, ftype)

if __name__ == "__main__":
    main()

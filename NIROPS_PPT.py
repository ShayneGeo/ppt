import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

def load_ppt_viewer(ppt_url):
    encoded_url = urllib.parse.quote_plus(ppt_url)
    viewer_url = f"https://view.officeapps.live.com/op/embed.aspx?src={encoded_url}"
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
    st.title("Embedded PPT Viewer from GitHub")

    ppt_options = {
        "NIROPS Dataset Description": "https://github.com/ShayneGeo/ppt/raw/refs/heads/main/NIROPS_DatasetDescription.pptx",
        "Another PPT": "https://github.com/ShayneGeo/ppt/raw/refs/heads/main/NIROPS_DatasetDescription.pptx",
        "Third PPT": "https://github.com/ShayneGeo/ppt/raw/refs/heads/main/NIROPS_DatasetDescription.pptx",
    }

    for label, url in ppt_options.items():
        if st.button(f"Start Viewer - {label}", key=label):
            load_ppt_viewer(url)

if __name__ == "__main__":
    main()

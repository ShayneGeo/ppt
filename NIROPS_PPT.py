import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

def main():
    st.title("Embedded PPT Viewer from GitHub")

    if st.button("Start Viewer"):
        # URL to your PPTX file (must be publicly accessible)
        ppt_url = "https://github.com/ShayneGeo/ppt/raw/refs/heads/main/NIROPS_DatasetDescription.pptx"
        # URL encode the PPT file URL
        encoded_url = urllib.parse.quote_plus(ppt_url)
        # Create the embed URL for Microsoft Office Web Viewer
        viewer_url = f"https://view.officeapps.live.com/op/embed.aspx?src={encoded_url}"
        
        # HTML with an iframe that autofits the screen using viewport units.
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
        # The height parameter here sets the height of the container in Streamlit;
        # setting it high helps simulate a fullscreen experience.
        components.html(html_code, height=800)

if __name__ == "__main__":
    main()

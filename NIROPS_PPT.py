import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

def main():
    st.title("Embedded PPT Viewer from GitHub")

    # URL to your PPTX file (must be publicly accessible)
    ppt_url = "https://github.com/ShayneGeo/ppt/raw/refs/heads/main/NIROPS_DatasetDescription.pptx"
    # URL encode the PPT file URL
    encoded_url = urllib.parse.quote_plus(ppt_url)
    # Create the embed URL for Microsoft Office Web Viewer
    viewer_url = f"https://view.officeapps.live.com/op/embed.aspx?src={encoded_url}"

    st.write("Below is the embedded PPT viewer. Use the navigation provided by the viewer.")
    components.iframe(viewer_url, width=800, height=600, scrolling=True)

if __name__ == "__main__":
    main()

import streamlit as st
from streamlit_card import card
from PIL import Image
import io
import uuid
import html
import st_aggrid
import streamlit_extras as stx
import pandas as pd
# ┌──────────────────────────────────┐
# │ Copyright © 2024 BlackBots.net   │
# │ (https://BlackBots.net)          │
# ├──────────────────────────────────┤
# │ Developer: @Supreme.Ciento       │
# └──────────────────────────────────┘

st.markdown("""
<style>
  #GithubIcon{visibility: hidden;}
  .styles_terminalButton__JBj5T{visibility: hidden;}
  .styles_terminalButton__JBj5T{display:none}
  .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}
  .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}
</style>
""", unsafe_allow_html=True)
side_image = Image.open('static/4.png')

with st.sidebar:
    st.image(side_image)
    st.caption("Full Sail Student Card Gen.")
    name = st.text_input('Your name', value="@Supreme.Ciento")
    stu = st.text_input('Student id #', value="012345678")
    degree = st.text_input('Your degree', value="Game Development")
    memo = st.text_input('Memo', value="Good luck!")
    img = st.text_input('Background Image', value="https://www.ieabroad.com/wp-content/uploads/Full-Sail-University.png", placeholder='https://www.ieabroad.com/wp-content/uploads/Full-Sail-University.png')
    link = st.text_input('URL when clicked')

def generate_unique_key():
    unique_id = str(uuid.uuid4())
    hashed_key = hashlib.sha256(unique_id.encode()).hexdigest()
    return hashed_key
def generate_card():
    card(
        title=name,
        text=[f"#{stu}", f"{degree}", f"{memo}"],
        image=img,
        url=link,
        key=generate_unique_key()
    )

generate_card()

def inject_js_code(source: str) -> None:
    div_id = uuid.uuid4()

    st.markdown(
        f"""
    <div style="display:none" id="{div_id}">
        <iframe src="javascript: \
            var script = document.createElement('script'); \
            script.type = 'text/javascript'; \
            script.text = {html.escape(repr(source))}; \
            var div = window.parent.document.getElementById('{div_id}'); \
            div.appendChild(script); \
            div.parentElement.parentElement.parentElement.style.display = 'none'; \
        "/>
    </div>
    """,
        unsafe_allow_html=True,
    )


def print_window() -> None:
    # JS Code to be executed
    source = r"window.print()"

    inject_js_code(source=source)


def screenshot_window() -> None:
    # JS Code to be executed
    source = """
// Function to detect if the current browser is Chrome
const isChrome = () => /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);

const button = document.getElementById('reportButton');
button.addEventListener('click', function() {
    // Alert and exit if the browser is Chrome
    if (isChrome()) {
        //alert("Currently this function is available only on Firefox!");
        //button.style.display = 'none'; // Hides the button
        //return;
    }

    // Load a script dynamically and execute a callback after loading
    const loadScript = (url, isLoaded, callback) => {
        if (!isLoaded()) {
            const script = document.createElement('script');
            script.type = 'text/javascript';
            script.onload = callback;
            script.src = url;
            document.head.appendChild(script);
        } else {
            callback();
        }
    };

    // Check if html2canvas library is loaded
    const isHtml2CanvasLoaded = () => typeof html2canvas !== 'undefined';

    // Capture an individual iframe and call a callback with the result
    const captureIframe = (iframe, callback) => {
        try {
            const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
            html2canvas(iframeDoc.body, {
                scale: 1,
                logging: true,
                useCORS: true,
                allowTaint: true
            }).then(canvas => {
                callback(canvas ? canvas : null);
            }).catch(error => {
                console.error('Could not capture iframe:', error);
                callback(null);
            });
        } catch (error) {
            console.error('Could not access iframe:', error);
            callback(null);
        }
    };

    // Main function to capture all windows
    const captureAllWindows = () => {
        const streamlitDoc = window.parent.document;
        const stApp = streamlitDoc.querySelector('.main > .block-container');
        const iframes = Array.from(stApp.querySelectorAll('iframe'));
        let capturedImages = [];

        // Process each iframe sequentially
        const processIframes = (index = 0) => {
            if (index < iframes.length) {
                captureIframe(iframes[index], function(canvas) {
                    if (canvas) {
                        const img = document.createElement('img');
                        img.src = canvas.toDataURL('image/png');
                        capturedImages.push({iframe: iframes[index], img: img});
                    } else {
                        console.error('Skipping an iframe due to capture failure.');
                    }
                    processIframes(index + 1);
                });
            } else {
                // Capture the main app window after processing all iframes
                html2canvas(stApp, {
                    onclone: function(clonedDocument) {
                        const clonedIframes = Array.from(clonedDocument.querySelectorAll('iframe'));
                        capturedImages.forEach(({img}, index) => {
                            if (index < clonedIframes.length) {
                                const clonedIframe = clonedIframes[index];
                                clonedIframe.parentNode.replaceChild(img, clonedIframe);
                            }
                        });
                    },
                    scale: 1,
                    logging: true,
                    useCORS: true,
                    allowTaint: true,
                    ignoreElements: () => {}
                }).then(finalCanvas => {
                    // Create a download link for the captured image
                    finalCanvas.toBlob(blob => {
                        const url = window.URL.createObjectURL(blob);
                        var link = document.createElement('a');
                        link.style.display = 'none';
                        link.href = url;
                        link.download = 'screenshot.png';
                        document.body.appendChild(link);
                        link.click();
                        document.body.removeChild(link);
                        window.URL.revokeObjectURL(url);
                    });
                }).catch(error => {
                    console.error('Screenshot capture failed:', error);
                });
            }
        };

        processIframes();
    };

    loadScript(
        'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.3.2/html2canvas.min.js',
        isHtml2CanvasLoaded,
        captureAllWindows
    );
});
"""

    inject_js_code(source=source)


def add_reportgen_button():
    st.markdown(
        """
        <button id="reportButton" class="st-style-button">Generate Page Report</button>

        <style>
        .st-style-button {
            display: inline-flex;
            -webkit-box-align: center;
            align-items: center;
            -webkit-box-pack: center;
            justify-content: center;
            font-weight: 400;
            padding: 0.25rem 0.75rem;
            border-radius: 0.5rem;
            min-height: 38.4px;
            margin: 0px;
            line-height: 1.6;
            color: inherit;
            width: auto;
            user-select: none;
            background-color: white; /* Set a white background */
            border: 1px solid rgba(49, 51, 63, 0.2);
            outline: none; !important
            box-shadow: none !important;
        }

        /* Change background on mouse-over */
        .st-style-button:hover {
            background-color: white;
            color: #0A04D2;
            border: 1px solid #0A04D2;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
    screenshot_window()


if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Screenshot test", layout="wide")
    add_reportgen_button()

    # Sample Data
    sample_df = pd.DataFrame(
        data={
            "A": [1, 2, 4],
            "B": [2, "F", True],
            "C": [[0, 1, 1, 0], [1, 20, 2, 0], [45, 7, 22, 80]],
        }
    )

    columns = st.columns(2)

    # Streamlit native components
    with columns[0]:

        st.title("Streamlit metric")
        st.metric(label="Example Metric", value=10, delta=0.5)

        st.divider()

        st.title("Streamlit dataframe")
        st.dataframe(
            data=sample_df,
            use_container_width=True,
            column_config={
                "C": st.column_config.LineChartColumn(),
            },
        )

        st.divider()

        st.title("Streamlit chart")
        st.line_chart(data=sample_df[["A", "B"]])

    with columns[1]:

        st.title("Streamlit AgGrid")
        st_aggrid.AgGrid(
            data=sample_df,
            use_container_width=True,
            fit_columns_on_grid_load=True,
        )


import streamlit as st
from streamlit_card import card
from PIL import Image
import io

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

def example():
    card(
        title=name,
        text=[f"#{stu}", f"{degree}", f"{memo}"],
        image=img,
        url=link,
    )

# Generate the card
example()

# Get the current Streamlit report context
ctx = st.report_thread.get_report_ctx()

# Save the generated card image to a temporary buffer
buffer = io.BytesIO()
example()
st.image(buffer, caption='Download your card', use_column_width=True)

# Convert the generated card image to bytes
buffer.seek(0)
card_image_bytes = buffer.getvalue()

# Provide the generated card image for download
st.markdown(get_binary_file_downloader_html('student_card.png', card_image_bytes, 'Download Card'), unsafe_allow_html=True)

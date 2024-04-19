import streamlit as st
from streamlit_card import card
from PIL import Image
import io
import uuid
import hashlib

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

# Generate the card
generate_card()

# Provide the generated card image for download
st.download_button(label="Download Card", data=generate_card, file_name="student_card.png")


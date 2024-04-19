# ┌──────────────────────────────────┐
# │ Copyright © 2024 BlackBots.net   │
# │ (https://BlackBots.net)          │
# ├──────────────────────────────────┤
# │ Developer: @Supreme.Ciento       │
# └──────────────────────────────────┘
__author__ = "BlackBots.net"
__credits__ = ["@Supreme.Ciento"]
__license__ = "MIT"
__version__ = "1.12.24"

import streamlit as st
from streamlit_card import card
from PIL import Image
import io
import uuid
import html
import hashlib

side_image = Image.open('static/4.png')

with st.sidebar:
    st.image(side_image)
    st.caption("Full Sail Student Card Gen.")
    name = st.text_input('Your name', value="Your Name Here")
    stu = st.text_input('Student id #', value="012345678")
    degree = st.text_input('Your degree', value="Degree Here")
    memo = st.text_input('Memo', value="Good luck!")
    img = st.text_input('Background Image', value="https://www.ieabroad.com/wp-content/uploads/Full-Sail-University.png", placeholder='https://www.ieabroad.com/wp-content/uploads/Full-Sail-University.png')
    link = st.text_input('URL when Card is clicked', value="https://one.fullsail.edu/")
    
    url = 'https://www.instagram.com/supreme.ciento/'
    st.caption("Credit: [@Supreme.Ciento](%s)" % url)

def unique_key():
    unique_id = str(uuid.uuid4())
    hashed_key = hashlib.sha256(unique_id.encode()).hexdigest()
    return hashed_key

def generate_card():
    card_content = card(
        title=name,
        text=[f"#{stu}", f"{degree}", f"{memo}"],
        image=img,
        url=link,
        key=unique_key(),
        styles={
            "card": {
                "width": "500px",
                "height": "500px",
                "border-radius": "60px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            },
            "text": {
                "font-family": "serif",
            }
        }
    )
        

generate_card()
st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=FSCard!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)

# ┌──────────────────────────────────┐
# │ Copyright © 2024 BlackBots.net   │
# │ (https://BlackBots.net)          │
# ├──────────────────────────────────┤
# │ Developer: @Supreme.Ciento       │
# └──────────────────────────────────┘
__author__ = "Guillermo Matas Ruiz"
__credits__ = ["Guillermo Matas Ruiz"]
__license__ = "MIT"
__version__ = "1.0.0"

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
    name = st.text_input('Your name', value="@Supreme.Ciento")
    stu = st.text_input('Student id #', value="012345678")
    degree = st.text_input('Your degree', value="Game Development")
    memo = st.text_input('Memo', value="Good luck!")
    img = st.text_input('Background Image', value="https://www.ieabroad.com/wp-content/uploads/Full-Sail-University.png", placeholder='https://www.ieabroad.com/wp-content/uploads/Full-Sail-University.png')
    link = st.text_input('URL when Card is clicked')

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
        key=unique_key()
    )
    
generate_card()

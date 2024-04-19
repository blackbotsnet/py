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
    st.download_button('Download', download_card, args=(card_content,))

def download_card(card_content):
    # Convert card to image
    image = card_to_image(card_content)
    # Save image to BytesIO
    image_io = io.BytesIO()
    image.save(image_io, format='PNG')
    # Download image
    st.write(image_io.getvalue(), format='PNG', download="card.png")

def card_to_image(card_content):
    # This is where you'll implement the logic to convert the card to an image
    # You may use libraries like PIL or matplotlib for this purpose
    # Here's a placeholder implementation using PIL
    img = Image.new('RGB', (300, 250), color='white')
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), card_content, fill='black')
    return img

generate_card()

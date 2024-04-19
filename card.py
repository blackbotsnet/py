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


icob = Image.open('static/-.ico')

st.set_page_config(
    page_title="FSS: Card Gen",
    page_icon=icob,
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        <br><hr><center>
        .reportview-container {background: black;}
        .sidebar .siderbar-content {background: black;}
        .st-ck:hover {
        color: #gold;
        }
        color: lime;
        cursor: pointer;
        }
        img {
        width:75%;
        }
        width:578px;
        vertical-align: middle;
        horizontal-align: middle;
        max-width: 300px;
        margin: auto;
        }
        .css-yhwc6k{
        text-align: center;
        }
        #audio{autoplay:true;}
        #MainMenu{visibility: hidden;}
        footer{visibility: hidden;}
        .css-14xtw13 e8zbici0{visibility: hidden;}
        .css-m70y {display:none}
        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}
        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}
        .styles_terminalButton__JBj5T{visibility: hidden;}
        .styles_terminalButton__JBj5T{display:none}
        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}
        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}
        [data-testid='stSidebarNav'] > ul {
            min-height: 50vh;
        }
        [data-testid='stSidebarNav'] > ul {
            color: red;
        }
    </style>
""", unsafe_allow_html=True)

side_image = Image.open('static/4.png')

with st.sidebar:
    st.caption("Full Sail Student Card Gen.")
    name = st.text_input('Name:', value="Your Name Here")
    stu = st.text_input('Student ID:', value="012345678")
    degree = st.text_input('Degree/Certification', value="Degree Here")
    memo = st.text_input('Memo', value="Good luck!")
    img = st.text_input('Background Image', value="https://www.ieabroad.com/wp-content/uploads/Full-Sail-University.png", placeholder='https://www.ieabroad.com/wp-content/uploads/Full-Sail-University.png')
    link = st.text_input('Click Link', value="https://one.fullsail.edu/")
    siz = st.slider('Width', 100, 1000, 300)
    hiz = st.slider('Height', 100, 1000, 400)
    st.write('')
    st.write('')
    st.write('')
    st.image(side_image)
    url = 'https://www.instagram.com/supreme.ciento/'
    st.caption("Credit: [@Supreme.Ciento](%s)" % url)

def maintain_aspect_ratio(original_width, original_height, new_width):
    return (original_height / original_width) * new_width

original_width = 300
original_height = 400
new_width = siz
new_height = maintain_aspect_ratio(original_width, original_height, new_width)

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
                "width": new_width,
                "height": hiz,
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

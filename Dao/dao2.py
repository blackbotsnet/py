#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Supreme ciento"
__copyright__ = "Copyright 2023, Cloud Bots™ BlackBots"
__credits__ = ["Supreme Ciento"]
__license__ = "GPL"
__maintainer__ = "Cloud Bots™"
__email__ = "admin@BlackBots.net"
__status__ = "Production"

__version__ = "12.21.21"


import sys
import streamlit as st
import base64
from bs4 import BeautifulSoup
import textwrap
import requests
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.customize_running import center_running
from streamlit_extras.add_vertical_space import add_vertical_space
from annotated_text import annotated_text
from tts import TextToSpeech

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.header("BlackDao")
res_box=st.empty()
placeholder = st.empty()

URL = placeholder.text_input(':orange[Enter DaoTranslate.com URL]',key='input',help='Enter your DAOTranslate URL into the input field.')

ok=st.button('📩',help='📖Read',key='1237')
if ok:

    center_running()
    url = URL
    try:
        resp=requests.get(url)
    except:
        res_box.markdown(f":blue[Book:  ]Enter a valid url before running.")
        raise SystemExit
    
    if resp.status_code==200:
                
        soup=BeautifulSoup(resp.text,'html.parser')    
        st.markdown("""<style>
              .stMarkdown{color: black;}
              .st-c8:hover{color:orange;}
              .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}
              </style>""",
              unsafe_allow_html=True
        )
        d=soup.find("div",{"class":"epcontent entry-content"})
        with st.expander("Click to view text"):
                    annotated_text("",
                                          (d.text, "", "#fea"),
                                  "")

        add_vertical_space(1)

        txt2speech = TextToSpeech()
        conversion_text = d.text
        if st.button('Convert'):
            txt2speech.convert(text=conversion_text)
            with open('hello.mp3', 'rb') as audio_file:
                audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')

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
from io import StringIO,BytesIO
from gtts import gTTS
import requests
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.customize_running import center_running
from streamlit_extras.stoggle import stoggle


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
with st.expander("See Instructions"):
    st.write("*1:* Visit [DaoTranslate.com](https://daotranslate.com/az-list/)")
    st.write("*2:* Get link such as: *https://daotranslate.com/blackbook-chapter-2-english/*")
    st.write("*3:* Paste link into field below")
    st.write("*4:* Press Button to Start")
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )
def ReadIt():

    center_running()
    url = URL
    try:
        resp=requests.get(url)
    except:
        res_box.markdown(f":blue[Book:  ]Enter a valid url before running.")
        raise SystemExit
    
    if resp.status_code==200:
                
        soup=BeautifulSoup(resp.text,'html.parser')    
                
        d=soup.find("div",{"class":"epcontent entry-content"})
        stoggle(
                "Click to view text",
                d.text,
        )
        speech=BytesIO()
                
        speech_=gTTS(text=d.text,lang='en',slow=False)
                
        speech_.save("dao.mp3")
        
        autoplay_audio("dao.mp3")
                
        oldurl = url
        chap = ''.join([n for n in oldurl if n.isdigit()])
        nxtchap = str(int(chap) + int(+1))
        prvchap = str(int(chap))

        st.write("\n\nChapter Complete: " + prvchap + "\n\nNEXT CHAPTER\nChapter: " + nxtchap)

    else:
        res_box.markdown(f":blue[Book: ]There appears to be something wrong with the website.")
        raise SystemExit

    def Next():
        
        oldurl = url
        chap = ''.join([n for n in oldurl if n.isdigit()])
        nxtchap = str(int(chap) + int(+1))
        nxtUrl = str(oldurl.replace(chap, nxtchap))
        URL = nxtUrl
        input = placeholder.text_input(URL, value='', key=1)

    nxt=st.button('📖Next Ch.',help='📖Next Chapter',key='13337')
            
    if nxt:
        Next()

if ok:
    ReadIt()
    

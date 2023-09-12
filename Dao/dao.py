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
from streamlit_extras.add_vertical_space import add_vertical_space
from annotated_text import annotated_text


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
        speech=BytesIO()
        speech_=gTTS(text=d.text,lang='en',slow=False)
        speech_.save("dao.mp3")
        autoplay_audio("dao.mp3")
                
        oldurl = url
        chap = ''.join([n for n in oldurl if n.isdigit()])
        nxtchap = str(int(chap) + int(+1))
        prvchap = str(int(chap))

        st.write(f"\n\n:orange[Chapter Complete: :red[*{prvchap}*] Next Chapter: :green[*{nxtchap}*]]")

        nxtUrl = str(oldurl.replace(chap, nxtchap))
        st.write(f"URL: {nxtUrl}")
    def NEXT():
                url = nxtUrl
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
                    speech=BytesIO()
                    speech_=gTTS(text=d.text,lang='en',slow=False)
                    speech_.save("dao.mp3")
                    #autoplay_audio("dao.mp3")
                    st.audio("dao.mp3")
                else:
                    res_box.markdown(f":blue[Book: ]There appears to be something wrong with the website.")
                    raise SystemExit
                oldurl = url
                chap = ''.join([n for n in oldurl if n.isdigit()])
                nxtchap = str(int(chap) + int(+1))
                prvchap = str(int(chap))
                nxtUrl = str(oldurl.replace(chap, nxtchap))
                st.write(f"\n\n:orange[Chapter Complete: :red[*{prvchap}*] Next Chapter: :green[*{nxtchap}*]]")
                st.write(f"URL: {nxtUrl}")
    NEXT()
    NEXT()
    NEXT()
if ok:
    ReadIt()
    

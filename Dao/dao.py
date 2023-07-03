#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import os
#import sys
#owd=sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import streamlit as st

__author__ = "Supreme ciento"
__copyright__ = "Copyright 2023, Cloud Bots™ BlackBots"
__credits__ = ["Supreme Ciento"]
__license__ = "GPL"
__maintainer__ = "Cloud Bots™"
__email__ = "cloudbotsbiz@gmail.com"
__status__ = "Production"

__version__ = "12.21.21"


import requests
from threading import Thread
import textwrap
from PIL import Image
from io import BytesIO
import threading
import sys
import time
from bs4 import BeautifulSoup
from contextlib import contextmanager


st.header("BlackDao")
res_box=st.empty()
URL = st.text_area(':orange[Enter DaoTranslate.com URL]',key='input',help='Enter your DAOTranslate URL into the input field.')

def threading():
    t = Thread(target=ReadIt)
    t.start()

@contextmanager
def ReadIt():
    url = URL
    try:
        resp=requests.get(url)
    except:
        res_box.markdown(f":blue[Book:  ]Enter a valid url before running.")
        raise SystemExit
    
    if resp.status_code==200:

        soup=BeautifulSoup(resp.text,'html.parser')    
        d=soup.find("div",{"class":"epcontent entry-content"})
        
        for d in d.findAll("p"):
            with st_stdout("code"):
                res_box.markdown(f":blue[Book:  ]"+d.text)
            
            finished = False
            while not finished:
                res_box.markdown(f":blue[Book:  ]Reading..")
                finished = True
                if finished is True:
                    speech=BytesIO();speech_=gTTS(text=d.text,lang='en',slow=False);speech_.write_to_fp(speech);st.audio(speech)
                    st.download_button('Save Text',d.text,key='847*');st.markdown('---')
                    break
    else:
        res_box.markdown(f":blue[Book: ]There appears to be something wrong with the website.")
        raise SystemExit

    def Next():
        ## EDIT #############################
        oldurl = url
        chap = ''.join([n for n in oldurl if n.isdigit()])
        nxtchap = str(int(chap) + int(+1))
        nxtUrl = str(oldurl.replace(chap, nxtchap))


ok=st.button('📩',help='📖Read',key='1237',use_container_width=False);memory=[];res_box.markdown(f":blue[Book:  ]")
if ok:
  threading()

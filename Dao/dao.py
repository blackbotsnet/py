#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
def working_directory(directory):
    owd = os.getcwd()
    try:
        os.chdir(directory)
        yield directory
    finally:
        os.chdir(owd)
import streamlit as st

__author__ = "Supreme ciento"
__copyright__ = "Copyright 2023, Cloud Bots™ BlackBots"
__credits__ = ["Supreme Ciento"]
__license__ = "GPL"
__maintainer__ = "Cloud Bots™"
__email__ = "cloudbotsbiz@gmail.com"
__status__ = "Production"

__version__ = "12.21.21"


from contextlib import contextmanager
@contextmanager

os.environ["DISPLAY"] = ":0"
import PySimpleGUI as sg
from xmlrpc.client import boolean
import requests
from bs4 import BeautifulSoup
from threading import Thread
from platform import system
from time import sleep
import textwrap
import requests
from PIL import Image
import io
import threading
import time



st.header("BlackDao")
res_box=st.empty()
URL = st.text_area(':orange[Enter DaoTranslate.com URL]',key='input',help='Enter your DAOTranslate URL into the input field.')

def threading():
    t = Thread(target=ReadIt)
    t.start()

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
            res_box.markdown(f":blue[Book:  ]"+d.text)

            finished = False
            while not finished:
                speech=BytesIO();speech_=gTTS(text=d.text,lang='en',slow=False);speech_.write_to_fp(speech);st.audio(speech)
                finished = True
                if finished is True:
                    break
        st.download_button('Save Text',d.text,key='847*');st.markdown('---')

    else:
        spk.Speak('There appears to be something wrong with the website.')
        spk.Skip()
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
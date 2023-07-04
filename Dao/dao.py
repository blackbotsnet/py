#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import os
import sys
#owd=sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import streamlit as st
import base64

__author__ = "Supreme ciento"
__copyright__ = "Copyright 2023, Cloud Bots™ BlackBots"
__credits__ = ["Supreme Ciento"]
__license__ = "GPL"
__maintainer__ = "Cloud Bots™"
__email__ = "cloudbotsbiz@gmail.com"
__status__ = "Production"

__version__ = "12.21.21"


from streamlit_extras.switch_page_button import switch_page


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.header("BlackDao")
res_box=st.empty()
URL = st.text_input(':orange[Enter DaoTranslate.com URL]',key='input',help='Enter your DAOTranslate URL into the input field.')

ok=st.button('📩',help='📖Read',key='1237');memory=[];res_box.markdown(f":blue[Book:  ]")

if ok:
    switch_page("trans")
    

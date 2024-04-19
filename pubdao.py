# ┌──────────────────────────────────┐
# │ BlackGram - Manga Dōjutsu v1.23  │
# ├──────────────────────────────────┤
# │ Copyright © 2024 BlackBots.net   │
# │ (https://BlackBots.net)          │
# ├──────────────────────────────────┤
# │ Developer: @Supreme.Ciento       │
# ├──────────────────────────────────┤
# │ Licensed under the MIT           │
# │ (https://BlackBots.net/license)  │
# └──────────────────────────────────┘
#            マンガアプリ

# 010011010110000101101110011001110110000101000100011011110110101001110101011101000111001101110101
 
# 77971101039768111106117116115117 
                                                                      
#    x*8888x.:*8888: -"888:                                                                     
#   X   48888X `8888H  8888                                                         
#  X8x.  8888X  8888X  !888>               x@88k u@88c.                  
#  X8888 X8888  88888   "*8%-    us888u.  ^"8888""8888"  .ue888Nc..    us888u.                  
#  '*888!X8888> X8888  xH8>   .@88 "8888"   8888  888R  d88E`"888E` .@88 "8888"                 
#    `?8 `8888  X888X X888>   9888  9888    8888  888R  888E  888E  9888  9888                  
#    -^  '888"  X888  8888>   9888  9888    8888  888R  888E  888E  9888  9888                  
#     dx '88~x. !88~  8888>   9888  9888    8888  888R  888E  888E  9888  9888                  
#   .8888Xf.888x:!    X888X.: 9888  9888   "*88*" 8888" 888& .888E  9888  9888                  
#  :""888":~"888"     `888*"  "888*""888"    ""   'Y"   *888" 888&  "888*""888"                 
#      "~'    "~        ""     ^Y"   ^Y'                 `"   "888E  ^Y"   ^Y'                  
#                                                       .dWi   `88E                             
#                                                       4888~  J8%                              
#                                                        ^"===*"`                               
#         ....                                                          .x+=:.                  
#     .xH888888Hx.                     .                               z`    ^%                 
#   .H8888888888888:     *^^^^^^^*    888>                    .88             <k
#   888*"""?""*88888X    ...ue888b    "8P    .@88k  z88u     :888ooo    .@8Ned8"  .@88k  z88u   
#  'f     d8x.   ^%88k   888R Y888r    .    ~"8888  8888   -*8888888  .@^%8888"  ~"8888  8888   
#  '>    <88888X   '?8   888R I888>  u888u.   8888  888R     8888    x88:  `)8b.   8888  888R   
#   `:..:`888888>    8>  888R I888> `'888E    8888  888R     8888    8888N=*8888   8888  888R   
#          `"*88     X   888R I888>   888E    8888  888R     8888     %8"    R88   8888  888R   
#     .xHHhx.."      !  u8888cJ888    888E    8888 ,888B .  .8888Lu=   @8Wou 9%    8888 ,888B . 
#    X88888888hx. ..!    "*888*P"     888E   "8888Y 8888"   ^%888*   .888888P`    "8888Y 8888"  
#   !   "*888888888"       'Y"        888E    `Y"   'YP       'Y"    `   ^"F       `Y"   'YP    
#          ^"***"`                    888E                                                      
#                                     888E                                                      
#                                     888P                                                      
#                                   .J88" "                                                     
_S='daotrans'
_R='https://manhuaaz.com/manga/'
_Q='always'
_P='series/'
_O='mdthumb'
_N='listupd'
_M='Searching..'
_L='Loading text & audio..'
_K='current_image_index'
_J='image_links'
_I='Copy'
_H='href'
_G='src'
_F='html.parser'
_E='en'
_D='class'
_C='div'
_B=False
_A=True
import os,base64,time,random,tempfile,io
from io import BytesIO
import uuid,hashlib,re,requests
from pydub import AudioSegment
from pydub.effects import speedup
from gtts import gTTS
from PIL import Image
import easyocr as ocr,numpy as np
from easyocr import Reader
import streamlit as st,streamlit_nested_layout,streamlit.components.v1 as components,streamlit_extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from bs4 import BeautifulSoup
import webbrowser
def generate_unique_key():A=str(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def autoplay_audio(file_path):
        with open(file_path,'rb')as A:B=A.read();C=base64.b64encode(B).decode();D=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{C}" type="audio/mp3">\n            </audio>\n            ';st.markdown(D,unsafe_allow_html=_A)
def get_driver():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',_B);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=A)
def perform_img_actions(url):
        if _J not in st.session_state:st.session_state.image_links=[]
        if _K not in st.session_state:st.session_state.current_image_index=0
        try:driver.get(url)
        except:pass
        with st.spinner(_L):
                st.session_state.image_links=get_image_links(url);st.session_state.current_image_index=0
                if st.session_state.image_links:
                        for A in st.session_state.image_links:st.image(A,use_column_width=_A)
                        st.write(f"Total Images: {len(st.session_state.image_links)}");transcribe_to_audio(st.session_state.image_links)
def get_image_links(url):
        try:driver.get(url)
        except WebDriverException as C:
                if driver.current_url==url:return[]
                else:st.write(f"Error loading URL: {C}");return[]
        B=[];D=driver.find_elements(By.CSS_SELECTOR,'img')
        for E in D:
                A=E.get_attribute(_G)
                if A and is_image_link(A):B.append(A)
        driver.quit();return B
def transcribe_to_audio(image_links):
        D=[]
        for(J,B)in enumerate(image_links,start=1):
                try:
                        if not is_supported_image_format(B):continue
                        with st.spinner(' Getting image text '):
                                F=ocr.Reader([_E]);G=F.readtext(B);E=[]
                                for A in G:E.append(A[1].strip())
                        A=filter_english_words(E)
                        if A:
                                C=os.path.join('audio',os.path.splitext(os.path.basename(B))[0]+'.mp3')
                                if not os.path.exists(C):H=gTTS(text=A,lang=_E,slow=_B);H.save(C)
                                D.append(C)
                                if on:res_box.markdown(f":blue[RAWR: ]:green[*{A}*]")
                        else:res_box.markdown(f":blue[Dao: ]:orange[No Text]")
                except Exception as I:st.write(f"Error processing {B}: {I}")
        return D
def is_supported_image_format(image_url):
        A=['.png','.jpg','.jpeg']
        for format in A:
                if image_url.lower().endswith(format):return _A
        return _B
def is_image_link(link):
        A=['.png','.jpg','.jpeg']
        for B in A:
                if link.lower().endswith(B):return _A
        return _B
def load_model():return ocr.Reader([_E],model_storage_directory='.')
def filter_english_words(text):A=text;B='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';C=re.findall(B,A);D=' '.join(C);A=D.lower();return A
def readit(url):
        M='file.mp3';H='\n';C=url;D=get_driver()
        try:D.get(C)
        except:pass
        if not C:res_box.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
        else:
                try:
                        I=requests.get(C)
                        if I.status_code==200:
                                N=BeautifulSoup(I.text,_F);E=N.find(_C,{_D:'epcontent entry-content'})
                                if E:
                                        c='';O=len(E.findAll('p'));B=E.findAll('p');F=1;d=O//F;P=[B[A:A+F]for A in range(0,len(B),F)];A=''
                                        for Q in B:A+=Q.text+H
                                        A=A.replace('<p>','');A=A.replace('"','');st.markdown('<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>',unsafe_allow_html=_A)
                                        with st.spinner('Loading text..'):
                                                with st.expander('Read'):from annotated_text import annotated_text as R;B=A.split(H);S=[(A,'','#fea')for A in B];R(*S);st.caption(f"{len(A)} characters in this chapter.");J=C;G=''.join([A for A in J if A.isdigit()]);T=str(int(G)+int(+1));U=str(int(G));K=str(J.replace(G,T));st.caption(':green[Chapter Complete:] '+U+'\n\n:orange[Next Chapter:] '+K);e=st.text_area('Link',f"{K}",key=generate_unique_key())
                                        with st.spinner('Loading audio..'):
                                                with tempfile.NamedTemporaryFile(suffix='.mp3',delete=_B)as L:A=A.replace('"','');V=gTTS(text=A,lang=_E,slow=_B);V.save(L.name);W=AudioSegment.from_mp3(L.name);X=speedup(W,1.2,150);X.export(M,format='mp3');autoplay_audio(M)
                                        for Y in P:
                                                Z=''
                                                for a in Y:Z+=a.text+H
                                        D.quit()
                                else:st.write('')
                        else:st.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
                except Exception as b:st.write(f":blue[Dao: ]:green[*Error occurred: {b}*]")
        D.quit()
history=[]
ih=''
icob=Image.open('static/-.ico')
ranum=random.randint(1,99999)
st.set_page_config(page_title='Manga Dōjutsu',page_icon=icob,layout='centered',initial_sidebar_state='expanded')
st.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {\n            min-height: 50vh;\n        }\n        [data-testid='stSidebarNav'] > ul {\n            color: red;\n        }\n    </style>\n",unsafe_allow_html=_A)
main_image=Image.open('static/dojutsu.png')
side_image=Image.open('static/4.png')
st.sidebar.write('BlackDao: Manga Dōjutsu')
if _J not in st.session_state:st.session_state.image_links=[]
if _K not in st.session_state:st.session_state.current_image_index=0
genre=None
with st.sidebar:
        st.image(side_image);st.caption('Manga Text or Image To Speach');on=st.checkbox('Stream Story (Disabled)',value=_B,disabled=_A);st.divider();st.header('Google Play Store');st.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');st.header('Official PC Version');st.caption('Download from: https://blackbots.gumroad.com/l/manga');st.caption('Join Our Discord: https://discord.gg/HcVPaSpF');st.divider()
        with st.expander('Help'):st.caption('How to use BlackDao: Manga Dōjutsu');st.caption('- Enter search term into `Search` field to find `Links`');st.caption('- `Copy` a Link');st.caption('- `Paste` Link onto `Enter Link` field');st.caption('- `Press Read`');st.caption('- View Image Based Links with the `Image Based` tab')
col1,col2=st.columns(2)
outer_cols=st.columns([1,2])
search_variable=st.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
if search_variable:
        with st.spinner(_M):
                with st.expander(':mag: Search'):
                        search_url=f"https://daotranslate.us/?s={search_variable}";resp=requests.get(search_url)
                        if resp.status_code==200:
                                soup=BeautifulSoup(resp.text,_F);search_result_div=soup.find(_C,{_D:_N})
                                if search_result_div:
                                        titles=search_result_div.find_all(_C,{_D:_O})
                                        for title in titles:
                                                title_url=title.a[_H];title_name=title_url.split(_P)[1].replace('/','').title();ih=f"https://daotranslate.us/{title_name}-chapter-1/"
                                                with st.spinner(_M):
                                                        st.write(f"[{title_name}]({ih})");img_url=title.img[_G]
                                                        if img_url:st.image(img_url,caption=ih)
                                                        if ih:txt=st.text_area(_I,f"{ih}",key=generate_unique_key())
                                                        st.divider()
with col1:
        with st.expander(':books: Random Titles'):
                resp=requests.get('https://daotranslate.us/?s=i')
                if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,_F);manga_list_div=soup.find(_C,{_D:_N})
                        if manga_list_div:
                                titles=manga_list_div.find_all(_C,{_D:_O})
                                for title in titles:
                                        title_url=title.a[_H];title_name=title_url.split(_P)[1].replace('/','').title();ch=f"https://daotranslate.us/{title_name}-chapter-1/";st.write(f"[{title_name}]({ch})");img_url=title.img[_G]
                                        if img_url:st.image(img_url,caption=ch,use_column_width=_Q)
                                        if ch:txt=st.text_area(_I,f"{ch}",key=generate_unique_key())
                                        st.divider()
with col2:
        with st.expander(':frame_with_picture: Image'):
                resp=requests.get('https://manhuaaz.com/')
                if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,_F);manga_links=soup.find_all('a',href=lambda href:href and href.startswith(_R))
                        for link in manga_links:
                                href=link.get(_H);manga_name=href.split(_R)[1]
                                if'chapter'not in manga_name:cch=f"{href}chapter-1/"
                                else:cch=href
                                st.write(f"[{manga_name}]({cch})");img_tag=link.find('img')
                                if img_tag:img_url=img_tag.get('data-src');st.image(img_url,caption=cch,use_column_width=_Q)
                                if cch:txt=st.text_area(_I,f"{cch}",key=generate_unique_key())
                                st.divider()
st.image(main_image)
res_box=st.empty()
xx=st.text_input(':orange[Enter Link:]',value='',placeholder='https://daotranslate.us/solo-leveling-ragnarok-chapter-1/',key='readfield',help='Enter manga chapter URL here')
ok=st.button(':green_book: Read',help='Read',key='readbutton',use_container_width=_B)
tab1,tab2=st.tabs(['Text Based','Image Based'])
with tab1:
        if _S in xx:
                if ok:
                        with st.spinner('Loading, please be patient..'):readit(xx)
with tab2:
        if _S not in xx.lower():
                if tab2:
                        if ok:
                                with st.spinner(_L):
                                        st.session_state.image_links=get_image_links(url);st.session_state.current_image_index=0
                                        if st.session_state.image_links:
                                                for image_link in st.session_state.image_links:st.image(image_link,use_column_width=_A)
                                                st.write(f"Total Images: {len(st.session_state.image_links)}");transcribe_to_audio(st.session_state.image_links)
st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=_A)
st.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=_A)

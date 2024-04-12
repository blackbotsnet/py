# ┌──────────────────────────────────┐
# │ BlackGram - Manga Dōjutsu v1.22  │
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
_Y='https://manhuaaz.com/manga/'
_X='🚧Image Based🚧'
_W='series/'
_V='mdthumb'
_U='listupd'
_T='orange'
_S='\n\nNEXT CHAPTER\nChapter: '
_R='Chapter Complete: '
_Q='Next Chapter'
_P='Next CH.'
_O='epcontent entry-content'
_N='src'
_M='href'
_L='next_button'
_K='.mp3'
_J='Read'
_I='Loading text & audio..'
_H='file.mp3'
_G='en'
_F='html.parser'
_E='\n'
_D='class'
_C='div'
_B=True
_A=False
import os,base64,time,tempfile,io
from io import BytesIO
import re,requests
from pydub import AudioSegment
from pydub.effects import speedup
from gtts import gTTS
from PIL import Image
import easyocr as ocr,numpy as np
from easyocr import Reader
import streamlit as st,streamlit_nested_layout,streamlit.components.v1 as components
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from bs4 import BeautifulSoup
import webbrowser
history=[]
ih=''
icob=Image.open('static/-.ico')
st.set_page_config(page_title='Manga Dōjutsu',page_icon=icob,layout='centered',initial_sidebar_state='expanded')
st.markdown('\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n    </style>\n',unsafe_allow_html=_B)
options=Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension',_A)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36')
options.add_argument('--dns-prefetch-disable')
options.add_argument('--no-sandbox')
options.add_argument('--lang=en-US')
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--ignore-certificate-errors')
def get_driver():return webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=options)
def autoplay_audio(file_path):
        with open(file_path,'rb')as A:B=A.read();C=base64.b64encode(B).decode();D=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{C}" type="audio/mp3">\n            </audio>\n            ';st.markdown(D,unsafe_allow_html=_B)
def perform_ok_actions(url):
        B=url
        with st.spinner(_I):
                B=ih;L=get_driver()
                try:L.get(B)
                except:pass
                if not B:res_box.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
                else:
                        try:
                                G=requests.get(B)
                                if G.status_code==200:
                                        M=BeautifulSoup(G.text,_F);D=M.find(_C,{_D:_O})
                                        if D:
                                                a='';N=len(D.findAll('p'));C=D.findAll('p');E=1;b=N//E;O=[C[A:A+E]for A in range(0,len(C),E)];A=''
                                                for P in C:A+=P.text+_E
                                                A=A.replace('<p>','');A=A.replace('"','');st.markdown('<style>\n                              .stMarkdown{color: black;}\n                              .st-c8:hover{color:orange;}\n                              .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                              </style>',unsafe_allow_html=_B)
                                                with st.expander(_J):from annotated_text import annotated_text as Q;C=A.split(_E);R=[(A,'','#fea')for A in C];Q(*R)
                                                with tempfile.NamedTemporaryFile(suffix=_K,delete=_A)as H:A=A.replace('"','');S=gTTS(text=A,lang=_G,slow=_A);S.save(H.name);T=AudioSegment.from_mp3(H.name);U=speedup(T,1.2,150);U.export(_H,format='mp3');autoplay_audio(_H)
                                                for V in O:
                                                        W=''
                                                        for I in V:W+=I.text+_E
                                                        if on:res_box.markdown(f":blue[Dao: ]:green[*{I.text}*]");time.sleep(5)
                                                X=st.button(_P,key=_L,help=_Q,use_container_width=_A)
                                                if X:J=B;F=''.join([A for A in J if A.isdigit()]);K=str(int(F)+int(+1));Y=str(int(F));c=str(J.replace(F,K));st.caption(_R+Y+_S+K,text_color=_T)
                                        else:res_box.markdown(f":blue[Dao: ]: ...")
                                else:res_box.markdown(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
                        except Exception as Z:res_box.markdown(f":blue[Dao: ]:green[*Error occurred: {Z}*]")
main_image=Image.open('static/dojutsu.png')
side_image=Image.open('static/1.png')
st.image(main_image)
res_box=st.empty()
with st.sidebar:
        st.image(side_image);st.caption('Manga Text or Image To Speech');on=st.checkbox('Stream Story',value=_A,disabled=_B);search_variable=st.text_input(':orange[Search:]',placeholder='',key='search',help='Enter a title here to search for')
        if search_variable:
                with st.expander('Search Results..'):
                        search_url=f"https://daotranslate.us/?s={search_variable}";resp=requests.get(search_url)
                        if resp.status_code==200:
                                soup=BeautifulSoup(resp.text,_F);search_result_div=soup.find(_C,{_D:_U})
                                if search_result_div:
                                        titless=search_result_div.find_all(_C,{_D:_V})
                                        for title in titless:
                                                title_url=title.a[_M];title_name=title_url.split(_W)[1];title_name=title_name.replace('/','');title_name=title_name.title();img_url=title.img[_N];st.image(img_url,caption=title_name);ch=f"https://daotranslate.us/{title_name}-chapter-1/";st.write(f"{ch}");ih=ch;button_key=title_name
                                                if ih:
                                                        lisp=st.button('Play',key=button_key+ch)
                                                        if lisp:perform_ok_actions(ih)
        with st.expander('Latest Releases'):
                resp=requests.get('https://daotranslate.us/?s=e')
                if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,_F);manga_list_div=soup.find(_C,{_D:_U})
                        if manga_list_div:
                                titles=manga_list_div.find_all(_C,{_D:_V})
                                for title in titles:
                                        title_url=title.a[_M];title_name=title_url.split(_W)[1].replace('/','').title();ih=f"https://daotranslate.us/{title_name}-chapter-1/";st.write(f"[{title_name} - Chapter 1]({ih})");img_url=title.img[_N];st.image(img_url,caption=title_name);button_key=title_name
                                        if ih:
                                                lisp=st.button('Play',key=button_key+ih)
                                                if lisp:perform_ok_actions(ih)
        with st.expander(_X):
                resp=requests.get('https://manhuaaz.com/')
                if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,_F);manga_links=soup.find_all('a',href=lambda href:href and href.startswith(_Y))
                        for link in manga_links:href=link.get(_M);manga_name=href.split(_Y)[1];ch=f"{href}";st.caption(manga_name);st.write(f"{ch}")
        url=st.text_input(':orange[Enter URL:]',value=ih,placeholder='https://daotranslate.us/solo-leveling-ragnarok-chapter-1/',key='input',help='Enter manga chapter URL here');ok=st.button('📚Read',help=_J,key='123',use_container_width=_A);st.header('Google Play Store');st.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');st.header('Official PC Version');st.caption('Download from: https://blackbots.gumroad.com/l/manga');st.caption('Join Our Discord: https://discord.gg/HcVPaSpF')
tab1,tab2=st.tabs(['Text Based',_X])
with tab1:
        if tab1:
                if ok:
                        with st.spinner(_I):
                                driver=get_driver()
                                try:driver.get(url)
                                except:pass
                                if not url:res_box.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
                                else:
                                        try:
                                                resp=requests.get(url)
                                                if resp.status_code==200:
                                                        soup=BeautifulSoup(resp.text,_F);d=soup.find(_C,{_D:_O})
                                                        if d:
                                                                all_text='';num_paragraphs=len(d.findAll('p'));paragraphs=d.findAll('p');desired_group_size=1;num_groups=num_paragraphs//desired_group_size;groups=[paragraphs[A:A+desired_group_size]for A in range(0,len(paragraphs),desired_group_size)];story=''
                                                                for paragraph in paragraphs:story+=paragraph.text+_E
                                                                story=story.replace('<p>','');story=story.replace('"','');st.markdown('<style>\n                                      .stMarkdown{color: black;}\n                                      .st-c8:hover{color:orange;}\n                                      .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                                      </style>',unsafe_allow_html=_B)
                                                                with st.expander(_J):from annotated_text import annotated_text;paragraphs=story.split(_E);formatted_paragraphs=[(A,'','#fea')for A in paragraphs];annotated_text(*formatted_paragraphs)
                                                                with tempfile.NamedTemporaryFile(suffix=_K,delete=_A)as tmp_file:story=story.replace('"','');tts=gTTS(text=story,lang=_G,slow=_A);tts.save(tmp_file.name);audio=AudioSegment.from_mp3(tmp_file.name);new_file=speedup(audio,1.2,150);new_file.export(_H,format='mp3');autoplay_audio(_H)
                                                                for group in groups:
                                                                        group_text=''
                                                                        for d_paragraph in group:group_text+=d_paragraph.text+_E
                                                                        if on:res_box.markdown(f":blue[Dao: ]:green[*{d_paragraph.text}*]");time.sleep(5)
                                                                next_ch=st.button(_P,key=_L,help=_Q,use_container_width=_A)
                                                                if next_ch:oldurl=url;chap=''.join([A for A in oldurl if A.isdigit()]);nxtchap=str(int(chap)+int(+1));prvchap=str(int(chap));nxtUrl=str(oldurl.replace(chap,nxtchap));st.caption(_R+prvchap+_S+nxtchap,text_color=_T)
                                                        else:res_box.markdown(f":blue[Dao: ]: ...")
                                                else:res_box.markdown(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
                                        except Exception as e:res_box.markdown(f":blue[Dao: ]:green[*Error occurred: {e}*]")
def get_image_links(url):
        try:driver.get(url)
        except WebDriverException as C:
                if driver.current_url==url:return[]
                else:st.write(f"Error loading URL: {C}");return[]
        B=[];D=driver.find_elements(By.CSS_SELECTOR,'img')
        for E in D:
                A=E.get_attribute(_N)
                if A and is_image_link(A):B.append(A)
        driver.quit();return B
def transcribe_to_audio(image_links):
        D=[]
        for(J,B)in enumerate(image_links,start=1):
                try:
                        if not is_supported_image_format(B):continue
                        with st.spinner(' Getting image text '):
                                F=ocr.Reader([_G]);G=F.readtext(B);E=[]
                                for A in G:E.append(A[1].strip())
                        A=filter_english_words(E)
                        if A:
                                C=os.path.join('audio',os.path.splitext(os.path.basename(B))[0]+_K)
                                if not os.path.exists(C):H=gTTS(text=A,lang=_G,slow=_A);H.save(C)
                                D.append(C)
                                if on:res_box.markdown(f":blue[RAWR: ]:green[*{A}*]")
                        else:res_box.markdown(f":blue[Dao: ]:orange[No Text]")
                except Exception as I:st.write(f"Error processing {B}: {I}")
        return D
def is_supported_image_format(image_url):
        A=['.png','.jpg','.jpeg']
        for format in A:
                if image_url.lower().endswith(format):return _B
        return _A
def is_image_link(link):
        A=['.png','.jpg','.jpeg']
        for B in A:
                if link.lower().endswith(B):return _B
        return _A
if'image_links'not in st.session_state:st.session_state.image_links=[]
if'current_image_index'not in st.session_state:st.session_state.current_image_index=0
@st.cache_resource
def load_model():return ocr.Reader([_G],model_storage_directory='.')
def filter_english_words(text):A=text;B='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';C=re.findall(B,A);D=' '.join(C);A=D.lower();return A
with tab2:
        if ok:
                with st.spinner(_I):
                        st.session_state.image_links=get_image_links(url);st.session_state.current_image_index=0
                        if st.session_state.image_links:st.image(st.session_state.image_links[0],use_column_width=_B)
                        st.write(f"Total Images: {len(st.session_state.image_links)}")
                        try:
                                if st.session_state.image_links:
                                        current_image_index=st.session_state.current_image_index;current_image_link=st.session_state.image_links[current_image_index];st.image(current_image_link,use_column_width=_B);next_button_clicked=st.button('Next',key=_L,help='Show next image',use_container_width=_A)
                                        if next_button_clicked:
                                                current_image_index+=1
                                                if current_image_index>=len(st.session_state.image_links):current_image_index=0
                                                st.session_state.current_image_index=current_image_index;current_image_link=st.session_state.image_links[current_image_index];st.image(current_image_link,use_column_width=_B);transcribe_to_audio([current_image_link])
                        except Exception as e:st.write(f"Error: {e}")
st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=_B)
st.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=_B)

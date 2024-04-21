# ┌─────────────────────────────────────┐
# │ BlackGram - Manga Dōjutsu v2.12.21  │
# ├─────────────────────────────────────┤
# │   Copyright © 2024 BlackBots.net    │
# │      (https://BlackBots.net)        │
# ├─────────────────────────────────────┤
# │     Developer: @Supreme.Ciento      │
# ├─────────────────────────────────────┤
# │       Licensed under the MIT        │
# │   (https://BlackBots.net/license)   │
# └─────────────────────────────────────┘
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
_Z='daotrans'
_Y='data-src'
_X='chapter'
_W='series/'
_V='mdthumb'
_U='listupd'
_T='Searching..'
_S='Restart'
_R='\n\n:orange[Next Chapter:] '
_Q=':green[Chapter Complete:] '
_P='Loading text & audio..'
_O='current_image_index'
_N='image_links'
_M='Copy Code'
_L='src'
_K='img'
_J='always'
_I='href'
_H='https://manhuaaz.com/manga/'
_G='Read'
_F='java'
_E='class'
_D='div'
_C='html.parser'
_B=False
_A=True
import os,io,base64,hashlib,random,string,tempfile,time,uuid
from io import BytesIO
import re,requests
from PIL import Image
import numpy as np,easyocr as ocr
from easyocr import Reader
from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup
import streamlit as st,streamlit_nested_layout,streamlit.components.v1 as components,streamlit_extras
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import webbrowser
def generate_unique_key():A=str(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def autoplay_audio(file_path):
        with open(file_path,'rb')as A:B=A.read();C=base64.b64encode(B).decode();D=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{C}" type="audio/mp3">\n            </audio>\n            ';st.markdown(D,unsafe_allow_html=_A)
def get_driver():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',_B);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=A)
def perform_img_actions(url):
        if _N not in st.session_state:st.session_state.image_links=[]
        if _O not in st.session_state:st.session_state.current_image_index=0
        try:driver.get(url)
        except:pass
        with st.spinner(_P):
                st.session_state.image_links=get_image_links(url);st.session_state.current_image_index=0
                if st.session_state.image_links:
                        for A in st.session_state.image_links:st.image(A,use_column_width=_A)
                        st.write(f"Total Images: {len(st.session_state.image_links)}");transcribe_to_audio(st.session_state.image_links)
def get_image_links(url):
        try:driver.get(url)
        except WebDriverException as C:
                if driver.current_url==url:return[]
                else:st.write(f"Error loading URL: {C}");return[]
        B=[];D=driver.find_elements(By.CSS_SELECTOR,_K)
        for E in D:
                A=E.get_attribute(_L)
                if A and is_image_link(A):B.append(A)
        driver.quit();return B
def transcribe_to_audio(image_links):
        D=[];E=load_model()
        for(J,A)in enumerate(image_links,start=1):
                if not is_supported_image_format(A):continue
                with st.spinner(' Getting image text '):F=requests.get(A).content;G=E.readtext(F);H=[A[1].strip()for A in G]
                B=filter_english_words(H)
                if B:
                        C=os.path.join('audio',os.path.splitext(os.path.basename(A))[0]+'.mp3')
                        if not os.path.exists(C):I=gTTS(text=B,lang='en',slow=_B);I.save(C)
                        D.append(C)
                        if on:res_box.markdown(f":blue[RAWR: ]:green[*{B}*]")
                else:res_box.markdown(f":blue[Dao: ]:orange[No Text]")
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
def load_model():return ocr.Reader(['en'],model_storage_directory='.')
def filter_english_words(text):
        A=text
        try:
                if not isinstance(A,str):raise ValueError('Input must be a string')
                B='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';C=re.findall(B,A);D=' '.join(C);A=D.lower()
        except Exception as E:st.write(f"Error filtering English words: {E}");A=''
        return A
def readit(url):
        N='file.mp3';H='\n';B=url;D=get_driver()
        try:D.get(B)
        except:pass
        if not B:res_box.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
        else:
                try:
                        I=requests.get(B)
                        if I.status_code==200:
                                O=BeautifulSoup(I.text,_C);E=O.find(_D,{_E:'epcontent entry-content'})
                                if E:
                                        e='';P=len(E.findAll('p'));C=E.findAll('p');F=1;f=P//F;Q=[C[A:A+F]for A in range(0,len(C),F)];A=''
                                        for R in C:A+=R.text+H
                                        A=A.replace('<p>','');A=A.replace('"','');st.markdown('<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>',unsafe_allow_html=_A)
                                        with st.expander(_G):from annotated_text import annotated_text as S;C=A.split(H);T=[(A,'','#fea')for A in C];S(*T);st.caption(f"{len(A)} characters in this chapter.");J=B;G=''.join([A for A in J if A.isdigit()]);K=str(int(G)+int(+1));U=str(int(G));V=str(J.replace(G,K));L,W=obfuscate(V);st.caption(_Q+U+_R+K);st.caption(L);B=deobfuscate(L,W);st.button('Continue',on_click=readit,args=[B],key=generate_unique_key())
                                        with tempfile.NamedTemporaryFile(suffix='.mp3',delete=_B)as M:A=A.replace('"','');X=gTTS(text=A,lang='en',slow=_B);X.save(M.name);Y=AudioSegment.from_mp3(M.name);Z=speedup(Y,1.2,150);Z.export(N,format='mp3');autoplay_audio(N)
                                        for a in Q:
                                                b=''
                                                for c in a:b+=c.text+H
                                        D.quit()
                                else:st.write('')
                        else:st.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
                except Exception as d:st.write(f":blue[Dao: ]:green[*Error occurred: {d}*]")
        D.quit()
def obfuscate(text):
        A={}
        for B in range(26):A[chr(65+B)]=chr((B+1)%26+65);A[chr(97+B)]=chr((B+1)%26+97)
        C=''.join(A.get(B,B)for B in text);return C,A
def deobfuscate(obfuscated_text,mapping):B={B:A for(A,B)in mapping.items()};A=''.join(B.get(A,A)for A in obfuscated_text);return A
history=[]
ih=''
icob=Image.open('static/-.ico')
ranum=random.randint(1,99999)
st.set_page_config(page_title='Manga Dōjutsu',page_icon=icob,layout='centered',initial_sidebar_state='expanded')
st.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}\n        [data-testid='stSidebarNav'] > ul {color: red;}\n        .language-java {color: black;}\n    </style>\n",unsafe_allow_html=_A)
main_image=Image.open('static/dojutsu.png')
side_image=Image.open('static/4.png')
st.sidebar.write('BlackDao: Manga Dōjutsu')
if _N not in st.session_state:st.session_state.image_links=[]
if _O not in st.session_state:st.session_state.current_image_index=0
genre=None
with st.sidebar:
        if'value'not in st.session_state:st.session_state.value=''
        def update_value():st.session_state.value=_S
        st.image(side_image);st.caption('Manga Text or Image To Speach');on=st.checkbox('Stream Story (Disabled)',value=_B,disabled=_A);st.divider();st.header('Google Play Store');st.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');st.header('Official PC Version');st.caption('Download from: https://blackbots.gumroad.com/l/manga');st.caption('Join Our Discord: https://discord.gg/HcVPaSpF');st.divider()
        with st.expander('Help'):st.caption('How to use BlackDao: Manga Dōjutsu');st.caption('- `Copy` a Code');st.caption('- `Paste` Code onto `Manga Code` field');st.caption('- `Press Read`')
        st.button(_S,on_click=update_value,key='keyy')
col1,col2=st.columns(2)
outer_cols=st.columns([1,2])
search_variable=st.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
if search_variable:
        with st.spinner(_T):
                with st.expander(':mag: Search'):
                        search_url_1=f"https://daotranslate.us/?s={search_variable}";resp_1=requests.get(search_url_1);search_url_2=f"https://manhuaaz.com/?s={search_variable}&post_type=wp-manga&op=&author=&artist=&release=&adult=";resp_2=requests.get(search_url_2)
                        if resp_1.status_code==200 and resp_2.status_code==200:
                                soup_1=BeautifulSoup(resp_1.text,_C);soup_2=BeautifulSoup(resp_2.text,_C);search_result_div_1=soup_1.find(_D,{_E:_U});search_result_div_2=soup_2.find_all('a',href=lambda href:href and href.startswith(_H))
                                if search_result_div_1 and search_result_div_2:
                                        titles=search_result_div_1.find_all(_D,{_E:_V});manga_links=iter(search_result_div_2)
                                        for title in titles:
                                                title_url=title.a[_I];title_name=title_url.split(_W)[1].replace('/','').title();titlename=title_name.replace('-',' ');ih=f"https://daotranslate.us/{title_name}-chapter-1/"
                                                with st.spinner(_T):
                                                        st.write(f"[{titlename}]({ih})");img_url=title.img[_L];original_string=ih;obfuscated_text,mapping=obfuscate(original_string)
                                                        if img_url:st.image(img_url,use_column_width=_J)
                                                        if ih:txt=f"\n                                {obfuscated_text}\n                                ";url=deobfuscate(obfuscated_text,mapping);st.code(txt,language=_F);st.button(_G,on_click=readit,args=[url],key=generate_unique_key())
                                                        st.divider()
                                                        try:
                                                                link=next(manga_links);href=link.get(_I)
                                                                if _X not in href:cch=f"{href}chapter-1/"
                                                                else:cch=href
                                                                manga_name=href.split(_H)[1];img_tag=link.find(_K);original_string=cch;obfuscated_text,mapping=obfuscate(original_string)
                                                                if img_tag:st.write(f"[{manga_name}]({cch})");img_url=img_tag.get(_Y);st.image(img_url,caption=obfuscated_text,use_column_width=_J);txt=f"\n                                    {obfuscated_text}\n                                    ";st.code(txt,language=_F);st.caption(_M);st.divider()
                                                        except StopIteration:break
with col1:
        with st.expander(':books: Random Titles(Text)'):
                resp=requests.get('https://daotranslate.us/?s=i')
                if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,_C);manga_list_div=soup.find(_D,{_E:_U})
                        if manga_list_div:
                                titles=manga_list_div.find_all(_D,{_E:_V})
                                for title in titles:
                                        title_url=title.a[_I];title_name=title_url.split(_W)[1].replace('/','').title();titlename=title_name.replace('-',' ');ch=f"https://daotranslate.us/{title_name}-chapter-1/";st.write(f"[{titlename}]({ch})");img_url=title.img[_L];original_string=ch;obfuscated_text,mapping=obfuscate(original_string)
                                        if img_url:st.image(img_url,use_column_width=_J)
                                        if ch:txt=f"\n                        {obfuscated_text}\n                        ";url=deobfuscate(obfuscated_text,mapping);st.code(txt,language=_F);st.button(_G,on_click=readit,args=[url],key=generate_unique_key())
                                        st.divider()
with col2:
        with st.expander(f":frame_with_picture: Comics(Images)"):
                resp=requests.get('https://manhuaaz.com/')
                if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,_C);manga_links=soup.find_all('a',href=lambda href:href and href.startswith(_H))
                        for link in manga_links:
                                href=link.get(_I)
                                if _X not in href:cch=f"{href}chapter-1/"
                                else:cch=href
                                manga_name=href.split(_H)[1];img_tag=link.find(_K);original_string=cch;obfuscated_text,mapping=obfuscate(original_string)
                                if img_tag:st.write(f"[{manga_name}]({cch})");img_url=img_tag.get(_Y);st.image(img_url,use_column_width=_J);url=deobfuscate(obfuscated_text,mapping);txt=f"\n                    {obfuscated_text}\n                    ";st.code(txt,language=_F);st.caption(_M);st.divider()
st.image(main_image)
res_box=st.empty()
xx=st.text_input(':orange[Manga Code:]',value='',placeholder='iuuqt://ebhdrrghmbuf.vt/..',key='readfield',help='Enter Manga Code here')
ok=st.button(':green_book: Read',help=_G,key='readbutton',use_container_width=_B)
if ok:
        url=deobfuscate(xx,mapping)
        if _Z in url:
                with st.spinner('Loading, please be patient..'):readit(url)
        if _Z not in url.lower():
                with st.spinner(_P):
                        driver=get_driver();st.session_state.image_links=get_image_links(url);st.session_state.current_image_index=0
                        if st.session_state.image_links:
                                for image_link in st.session_state.image_links:st.image(image_link,use_column_width=_A)
                                st.write(f"Total Images: {len(st.session_state.image_links)}");transcribe_to_audio(st.session_state.image_links);oldurl=url;chap=''.join([A for A in oldurl if A.isdigit()]);nxtchap=str(int(chap)+int(+1));prvchap=str(int(chap));nxtUrl=str(oldurl.replace(chap,nxtchap));obfuscated_text,mapping=obfuscate(nxtUrl);st.caption(_Q+prvchap+_R+obfuscated_text);txt=f"\n                {obfuscated_text}\n                ";st.code(txt,language=_F);st.caption(_M)
st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=_A)
st.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=_A)

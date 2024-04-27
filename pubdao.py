# ┌──────────────────────────────────┐
# │ BlackDao: Manga Dōjutsu v4.12.21 │
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
Ah='daotrans'
Ag='chapter'
Af='series/'
Ae='mdthumb'
Ad='listupd'
Ac='Searching..'
Ab='Restart'
Aa='\n\n:orange[Next Chapter:] '
AZ=':green[Chapter Complete:] '
AY='Loading text & audio..'
AX='current_image_index'
AW='image_links'
AC='always'
AB='data-src'
AA='PANEL/'
A9='NOVEL/'
A8='TOP/'
A7=range
A6=Exception
w='Copy Code'
v='/'
u='https://manhuaaz.com/manga/'
t='Read'
s='src'
r='img'
q=chr
m='href'
l='class'
k=' '
d='java'
c='div'
b='html.parser'
U=False
T=int
S=str
N=len
J=True
B=''
import os,io,base64,hashlib,random as AD,string,tempfile as Ai,time,uuid
from io import BytesIO
import re,requests as O
from PIL import Image as e
import numpy as BH,pandas as BI,pickle,easyocr as Aj
from easyocr import Reader
from gtts import gTTS
from pydub import AudioSegment as Ak
from pydub.effects import speedup
import streamlit as A,streamlit_nested_layout,streamlit.components.v1 as BJ,streamlit_extras
from bs4 import BeautifulSoup as Z
from selenium import webdriver as Al
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as Am
from webdriver_manager.chrome import ChromeDriverManager as An
from webdriver_manager.core.os_manager import ChromeType as Ao
import webbrowser
from utils import recommendations,read_object
def x():A=S(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def Ap(file_path):
	with open(file_path,'rb')as B:C=B.read();D=base64.b64encode(C).decode();E=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{D}" type="audio/mp3">\n            </audio>\n            ';A.markdown(E,unsafe_allow_html=J)
def y():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',U);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return Al.Chrome(service=Service(An(chrome_type=Ao.CHROMIUM).install()),options=A)
def BK(url):
	if AW not in A.session_state:A.session_state.image_links=[]
	if AX not in A.session_state:A.session_state.current_image_index=0
	try:BC.get(url)
	except:pass
	with A.spinner(AY):
		A.session_state.image_links=AE(url);A.session_state.current_image_index=0
		if A.session_state.image_links:
			for B in A.session_state.image_links:A.image(B,use_column_width=J)
			A.write(f"Total Images: {N(A.session_state.image_links)}");AF(A.session_state.image_links)
def AE(url):
	B=y()
	try:B.get(url)
	except Am as F:
		if B.current_url==url:return[]
		else:A.write(f"Error loading URL: {F}");return[]
	C=[];G=B.find_elements(By.CSS_SELECTOR,r)
	for H in G:
		D=H.get_attribute(s)
		if D and AG(D):C.append(D)
	I=B.find_elements(By.CSS_SELECTOR,'img[id^="image-"]')
	for J in I:
		E=J.get_attribute(s)
		if E and AG(E):C.append(E)
	B.quit();return C
def AF(image_links):
	F=[];H=Ar()
	for(M,D)in enumerate(image_links,start=1):
		if not Aq(D):continue
		with A.spinner(' Getting image text '):
			I=O.get(D).content
			try:J=H.readtext(I);G=[A[1].strip()for A in J];C=k.join(G);C=AH(C)
			except A6 as K:A.write(f"Error processing text: {K}");C=B
		C=AH(G)
		if C:
			E=os.path.join('audio',os.path.splitext(os.path.basename(D))[0]+'.mp3')
			if not os.path.exists(E):L=gTTS(text=C,lang='en',slow=U);L.save(E)
			F.append(E)
			if Aw:A4.markdown(f":blue[Streaming: ]:green[*{C}*]")
		else:A4.markdown(f":blue[Dao: ]:orange[No Text]")
	return F
def Aq(image_url):
	A=['.png','.jpg','.jpeg']
	for format in A:
		if image_url.lower().endswith(format):return J
	return U
def AG(link):
	A=['.png','.jpg','.jpeg']
	for B in A:
		if link.lower().endswith(B):return J
	return U
def Ar():return Aj.Reader(['en'],model_storage_directory='.')
def AH(text):
	C=text
	try:
		if not isinstance(C,S):raise ValueError('Input must be a string')
		D='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';E=re.findall(D,C);F=k.join(E);C=F.lower()
	except A6 as G:A.write(f"Error filtering English words: {G}");C=B
	return C
def n(url):
	W='file.mp3';K='\n';D=url;F=y()
	try:F.get(D)
	except:pass
	if not D:A4.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
	else:
		try:
			L=O.get(D)
			if L.status_code==200:
				X=Z(L.text,b);G=X.find(c,{l:'epcontent entry-content'})
				if G:
					u=B;Y=N(G.findAll('p'));E=G.findAll('p');H=1;v=Y//H;d=[E[A:A+H]for A in A7(0,N(E),H)];C=B
					for e in E:C+=e.text+K
					C=C.replace('<p>',B);C=C.replace('"',B);A.markdown('<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>',unsafe_allow_html=J)
					with A.expander(t):from annotated_text import annotated_text as f;E=C.split(K);g=[(A,B,'#fea')for A in E];f(*g);A.caption(f"{N(C)} characters in this chapter.");M=D;I=B.join([A for A in M if A.isdigit()]);P=S(T(I)+T(+1));h=S(T(I));i=S(M.replace(I,P));Q,j=V(i);A.caption(AZ+h+Aa+P);A.caption(Q);D=a(Q,j);A.button('Continue',on_click=n,args=[D],key=x())
					with Ai.NamedTemporaryFile(suffix='.mp3',delete=U)as R:C=C.replace('"',B);k=gTTS(text=C,lang='en',slow=U);k.save(R.name);m=Ak.from_mp3(R.name);o=speedup(m,1.2,150);o.export(W,format='mp3');Ap(W)
					for p in d:
						q=B
						for r in p:q+=r.text+K
					F.quit()
				else:A.write(B)
			else:A.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
		except A6 as s:A.write(f":blue[Dao: ]:green[*Error occurred: {s}*]")
	F.quit()
def V(text):
	C=text;D={}
	for E in A7(26):D[q(65+E)]=q((E+1)%26+65);D[q(97+E)]=q((E+1)%26+97)
	A=B.join(D.get(A,A)for A in C)
	if'nightcomic.com'in C:A=A8+A
	if'daotranslate'in C:A=A9+A
	if'manhuaaz.com'in C:A=AA+A
	return A,D
def a(obfuscated_text,mapping):
	A=obfuscated_text
	if A.startswith(A8):A=A[N(A8):]
	if A.startswith(A9):A=A[N(A9):]
	if A.startswith(AA):A=A[N(AA):]
	C={B:A for(A,B)in mapping.items()};D=B.join(C.get(A,A)for A in A);return D
BL=[]
o=B
As=e.open('static/-.ico')
BM=AD.randint(1,99999)
A.set_page_config(page_title='Manga Dōjutsu',page_icon=As,layout='centered',initial_sidebar_state='expanded')
A.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}\n        [data-testid='stSidebarNav'] > ul {color: red;}\n        .language-java {color: black;}\n    </style>\n",unsafe_allow_html=J)
At=e.open('static/dojutsu.png')
Au=e.open('static/4.png')
A.sidebar.write('BlackDao: Manga Dōjutsu')
if AW not in A.session_state:A.session_state.image_links=[]
if AX not in A.session_state:A.session_state.current_image_index=0
BN=None
with A.sidebar:
	if'value'not in A.session_state:A.session_state.value=B
	def Av():A.session_state.value=Ab
	A.image(Au);A.caption('Manga Text or Image To Speach');Aw=A.checkbox('Stream Story (Disabled)',value=U,disabled=J)
	with open('titles.txt','r')as Ax:AI=Ax.readlines()
	AJ=N(AI);Ay=(AJ-1)//10+1;AK=A.slider('Popular Titles',1,Ay,1);Az=(AK-1)*10;A_=min(AK*10,AJ)
	for B0 in A7(Az,A_):A.write(AI[B0])
	A.divider();A.header('Google Play Store');A.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');A.header('Official PC Version');A.caption('Download from: https://blackbots.gumroad.com/l/manga');A.caption('Join Our Discord: https://discord.gg/HcVPaSpF');A.divider()
	with A.expander('Help'):A.caption('How to use BlackDao: Manga Dōjutsu');A.caption('- `Copy` a Code');A.caption('- `Paste` Code onto `Manga Code` field');A.caption('- `Press Read`')
	A.button(Ab,on_click=Av,key='keyy')
def f(img_url,scale_factor):A=scale_factor;C=O.get(img_url);B=e.open(BytesIO(C.content));D,E=B.size;F=T(D*A);G=T(E*A);H=B.resize((F,G),e.LANCZOS);return H
K=A.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
AL=0
AM=0
if K:
	K=K.replace('"',B);K=K.replace('-',k);K=K.replace(':',B)
	with A.spinner(Ac):
		with A.expander(':mag: Search'):
			B1=f"https://daotranslate.net/?s={K}";AN=O.get(B1);B2=f"https://manhuaaz.com/?s={K}&post_type=wp-manga&op=&author=&artist=&release=&adult=";AO=O.get(B2)
			if AN.status_code==200 and AO.status_code==200:
				B3=Z(AN.text,b);B4=Z(AO.text,b);AP=B3.find(c,{l:Ad});AQ=B4.find_all('a',href=lambda href:href and href.startswith(u))
				if AP and AQ:
					z=AP.find_all(c,{l:Ae});A0=iter(AQ)
					for W in z:
						if AL>=10:break
						A1=W.a[m];g=A1.split(Af)[1].replace(v,B).title();A2=g.replace('-',k);o=f"https://daotranslate.net/{g}-chapter-1/"
						with A.spinner(Ac):
							h,E,i=A.columns(3)
							with E:A.write(f"[{A2}]({o})")
							F=W.img[s];L=o;C,I=V(L)
							if F:
								try:
									M=f(F,scale_factor=4);h,E,i=A.columns(3)
									with E:A.image(M,use_column_width=None)
								except:pass
							if o:
								h,E,i=A.columns(3)
								with E:G=f"\n                                    {C}\n                                    ";H=a(C,I);A.code(G,language=d);A.button(t,on_click=n,args=[H],key=x())
							A.divider();AL+=1
							try:
								P=next(A0);D=P.get(m)
								if Ag not in D:X=f"{D}chapter-1/"
								else:X=D
								Y=D.split(u)[1];Y=Y.replace(v,B);Q=P.find(r);L=X;C,I=V(L)
								if Q:
									if AM>=10:break
									h,E,i=A.columns(3)
									with E:A.write(f"[{Y}]({X})")
									F=Q.get(AB)
									try:
										M=f(F,scale_factor=4);h,E,i=A.columns(3)
										with E:A.image(M,use_column_width=None)
									except:pass
									h,E,i=A.columns(3)
									with E:G=f"\n                                    \t{C}\n                                    \t";A.code(G,language=d);A.caption(w);A.divider();AM+=1
							except StopIteration:break
B5,B6,B7=A.columns(3)
BO=A.columns([1,2])
AR=0
with B5:
	B8=AD.choice(string.ascii_uppercase)
	with A.expander(':loud_sound: Text & Audio '):
		R=O.get(f"https://daotranslate.net/?s={B8}")
		if R.status_code==200:
			j=Z(R.text,b);AS=j.find(c,{l:Ad})
			if AS:
				z=AS.find_all(c,{l:Ae})
				for W in z:
					if AR>=10:break
					A1=W.a[m];g=A1.split(Af)[1].replace(v,B).title();A2=g.replace('-',k);A3=f"https://daotranslate.net/{g}-chapter-1/";A.write(f"[{A2}]({A3})");F=W.img[s];L=A3;C,I=V(L)
					if F:
						try:M=f(F,scale_factor=4);A.image(M,use_column_width=AC)
						except:pass
					if A3:G=f"\n                        {C}\n                        ";H=a(C,I);A.code(G,language=d);A.button(t,on_click=n,args=[H],key=x())
					A.divider();AR+=1
AT=0
with B6:
	with A.expander(f":chart_with_upwards_trend: Top Rated"):
		R=O.get('https://nightcomic.com/')
		if R.status_code==200:
			j=Z(R.text,b);B9=j.find_all(c,class_='page-item-detail manga')
			for p in B9:
				P=p.find('a',class_='btn-link');Q=p.find(r);W=p.find('h3',class_='h5').text.strip();BA=p.find('span',class_='score').text.strip()
				if P and Q:
					if AT>=10:break
					D=P.get(m);F=Q.get(AB);L=D;C,I=V(L);H=a(C,I);A.write(f"[{W}]({D}) - Rating: {BA}")
					try:M=f(F,scale_factor=4);A.image(M,use_column_width=AC)
					except:pass
					G=f"\n                    {C}\n                    ";A.code(G,language=d);A.caption(w);A.divider();AT+=1
AU=0
with B7:
	with A.expander(f":frame_with_picture: Panels"):
		R=O.get('https://manhuaaz.com/')
		if R.status_code==200:
			j=Z(R.text,b);A0=j.find_all('a',href=lambda href:href and href.startswith(u))
			for P in A0:
				D=P.get(m)
				if Ag not in D:X=f"{D}chapter-1/"
				else:X=D
				Y=D.split(u)[1];Y=Y.replace(v,B);Q=P.find(r);L=X;C,I=V(L)
				if Q:
					if AU>=10:break
					A.write(f"[{Y}]({X})");F=Q.get(AB)
					try:M=f(F,scale_factor=4);A.image(M,use_column_width=AC)
					except:pass
					H=a(C,I);G=f"\n                    {C}\n                    ";A.code(G,language=d);A.caption(w);A.divider();AU+=1
A.image(At)
A4=A.empty()
H=a(A.text_input(':orange[Manga Code:]',value=B,placeholder='iuuqt://ebhdrrghmbuf.vt/..',key='readfield',help='Enter Manga Code here'),I)
BB=A.button(':green_book: Read',help=t,key='readbutton',use_container_width=U)
if BB:
	if Ah in H:
		with A.spinner('Loading, please be patient..'):n(H)
	if Ah not in H.lower():
		with A.spinner(AY):
			BC=y();A.session_state.image_links=AE(H);A.session_state.current_image_index=0
			if A.session_state.image_links:
				for BD in A.session_state.image_links:A.image(BD,use_column_width=J)
				A.write(f"Total Images: {N(A.session_state.image_links)}");AF(A.session_state.image_links);AV=H;A5=B.join([A for A in AV if A.isdigit()]);BE=S(T(A5)+T(+1));BF=S(T(A5));BG=S(AV.replace(A5,BE));C,I=V(BG);A.caption(AZ+BF+Aa+C);G=f"\n                {C}\n                ";A.code(G,language=d);A.caption(w)
A.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=J)
A.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=J)

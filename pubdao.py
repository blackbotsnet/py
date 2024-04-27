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
x='Copy Code'
w='/'
v='https://manhuaaz.com/manga/'
u='Read'
t='src'
s='img'
r=chr
m='href'
l='class'
k=' '
d='java'
c='div'
b='html.parser'
U=int
T=str
O=len
K=True
D=False
B=''
import os,io,base64,hashlib,random as AD,string,tempfile as Ai,time,uuid
from io import BytesIO
import re,requests as P
from PIL import Image as e
import numpy as BG,pandas as BH,pickle
from paddleocr import PaddleOCR as Aj
from gtts import gTTS
from pydub import AudioSegment as Ak
from pydub.effects import speedup
import streamlit as A,streamlit_nested_layout,streamlit.components.v1 as BI,streamlit_extras
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
def y():A=T(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def Ap(file_path):
	with open(file_path,'rb')as B:C=B.read();D=base64.b64encode(C).decode();E=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{D}" type="audio/mp3">\n            </audio>\n            ';A.markdown(E,unsafe_allow_html=K)
def z():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',D);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return Al.Chrome(service=Service(An(chrome_type=Ao.CHROMIUM).install()),options=A)
def BJ(url):
	if AW not in A.session_state:A.session_state.image_links=[]
	if AX not in A.session_state:A.session_state.current_image_index=0
	try:BB.get(url)
	except:pass
	with A.spinner(AY):
		A.session_state.image_links=AE(url);A.session_state.current_image_index=0
		if A.session_state.image_links:
			for B in A.session_state.image_links:A.image(B,use_column_width=K)
			A.write(f"Total Images: {O(A.session_state.image_links)}");AF(A.session_state.image_links)
def AE(url):
	B=z()
	try:B.get(url)
	except Am as F:
		if B.current_url==url:return[]
		else:A.write(f"Error loading URL: {F}");return[]
	C=[];G=B.find_elements(By.CSS_SELECTOR,s)
	for H in G:
		D=H.get_attribute(t)
		if D and AG(D):C.append(D)
	I=B.find_elements(By.CSS_SELECTOR,'img[id^="image-"]')
	for J in I:
		E=J.get_attribute(t)
		if E and AG(E):C.append(E)
	B.quit();return C
def AF(image_links):
	G=[];H=Aj(use_angle_cls=K,lang='en')
	for(N,E)in enumerate(image_links,start=1):
		if not Aq(E):continue
		with A.spinner(' Getting image text '):
			I=P.get(E).content
			try:
				J=H.ocr(I,det=D,rec=D,use_gpu=D,cls=D);A.write('OCR Result:',J);C=k.join(result_text);C=Ar(result_text)
				if C:
					F=os.path.join('audio',os.path.splitext(os.path.basename(E))[0]+'.mp3')
					if not os.path.exists(F):L=gTTS(text=C,lang='en',slow=D);L.save(F)
					G.append(F)
					if AH:q.markdown(f":blue[Streaming: ]:green[*{C}*]")
				else:q.markdown(f":blue[Dao: ]:orange[No Text]")
			except A6 as M:A.write(f"Error processing text: {M}");C=B
	return G
def Aq(image_url):
	A=['.png','.jpg','.jpeg']
	for format in A:
		if image_url.lower().endswith(format):return K
	return D
def AG(link):
	A=['.png','.jpg','.jpeg']
	for B in A:
		if link.lower().endswith(B):return K
	return D
def Ar(text):
	C=text
	try:
		if not isinstance(C,T):raise ValueError('Input must be a string')
		D='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';E=re.findall(D,C);F=k.join(E);C=F.lower()
	except A6 as G:A.write(f"Error filtering English words: {G}");C=B
	return C
def n(url):
	X='file.mp3';L='\n';E=url;G=z()
	try:G.get(E)
	except:pass
	if not E:q.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
	else:
		try:
			M=P.get(E)
			if M.status_code==200:
				Y=Z(M.text,b);H=Y.find(c,{l:'epcontent entry-content'})
				if H:
					v=B;d=O(H.findAll('p'));F=H.findAll('p');I=1;w=d//I;e=[F[A:A+I]for A in A7(0,O(F),I)];C=B
					for f in F:C+=f.text+L
					C=C.replace('<p>',B);C=C.replace('"',B);A.markdown('<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>',unsafe_allow_html=K)
					with A.expander(u):from annotated_text import annotated_text as g;F=C.split(L);h=[(A,B,'#fea')for A in F];g(*h);A.caption(f"{O(C)} characters in this chapter.");N=E;J=B.join([A for A in N if A.isdigit()]);Q=T(U(J)+U(+1));i=T(U(J));j=T(N.replace(J,Q));R,k=V(j);A.caption(AZ+i+Aa+Q);A.caption(R);E=a(R,k);A.button('Continue',on_click=n,args=[E],key=y())
					with Ai.NamedTemporaryFile(suffix='.mp3',delete=D)as S:C=C.replace('"',B);m=gTTS(text=C,lang='en',slow=D);m.save(S.name);o=Ak.from_mp3(S.name);p=speedup(o,1.2,150);p.export(X,format='mp3');Ap(X)
					for r in e:
						s=B
						for W in r:s+=W.text+L
						if AH:q.markdown(f":blue[Dao: ]:green[*{W.text}*]");time.sleep(5)
					G.quit()
				else:A.write(B)
			else:A.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
		except A6 as t:A.write(f":blue[Dao: ]:green[*Error occurred: {t}*]")
	G.quit()
def V(text):
	C=text;D={}
	for E in A7(26):D[r(65+E)]=r((E+1)%26+65);D[r(97+E)]=r((E+1)%26+97)
	A=B.join(D.get(A,A)for A in C)
	if'nightcomic.com'in C:A=A8+A
	if'daotranslate'in C:A=A9+A
	if'manhuaaz.com'in C:A=AA+A
	return A,D
def a(obfuscated_text,mapping):
	A=obfuscated_text
	if A.startswith(A8):A=A[O(A8):]
	if A.startswith(A9):A=A[O(A9):]
	if A.startswith(AA):A=A[O(AA):]
	C={B:A for(A,B)in mapping.items()};D=B.join(C.get(A,A)for A in A);return D
BK=[]
o=B
As=e.open('static/-.ico')
BL=AD.randint(1,99999)
A.set_page_config(page_title='Manga Dōjutsu',page_icon=As,layout='centered',initial_sidebar_state='expanded')
A.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}\n        [data-testid='stSidebarNav'] > ul {color: red;}\n        .language-java {color: black;}\n    </style>\n",unsafe_allow_html=K)
At=e.open('static/dojutsu.png')
Au=e.open('static/4.png')
A.sidebar.write('BlackDao: Manga Dōjutsu')
if AW not in A.session_state:A.session_state.image_links=[]
if AX not in A.session_state:A.session_state.current_image_index=0
BM=None
with A.sidebar:
	if'value'not in A.session_state:A.session_state.value=B
	def Av():A.session_state.value=Ab
	A.image(Au);A.caption('Manga Text or Image To Speach');AH=A.checkbox('Stream Story (Experimental)',value=D,disabled=D)
	with open('titles.txt','r')as Aw:AI=Aw.readlines()
	AJ=O(AI);Ax=(AJ-1)//10+1;AK=A.slider('Popular Titles',1,Ax,1);Ay=(AK-1)*10;Az=min(AK*10,AJ)
	for A_ in A7(Ay,Az):A.write(AI[A_])
	A.divider();A.header('Google Play Store');A.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');A.header('Official PC Version');A.caption('Download from: https://blackbots.gumroad.com/l/manga');A.caption('Join Our Discord: https://discord.gg/HcVPaSpF');A.divider()
	with A.expander('Help'):A.caption('How to use BlackDao: Manga Dōjutsu');A.caption('- `Copy` a Code');A.caption('- `Paste` Code onto `Manga Code` field');A.caption('- `Press Read`')
	A.button(Ab,on_click=Av,key='keyy')
def f(img_url,scale_factor):A=scale_factor;C=P.get(img_url);B=e.open(BytesIO(C.content));D,E=B.size;F=U(D*A);G=U(E*A);H=B.resize((F,G),e.LANCZOS);return H
L=A.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
AL=0
AM=0
if L:
	L=L.replace('"',B);L=L.replace('-',k);L=L.replace(':',B)
	with A.spinner(Ac):
		with A.expander(':mag: Search'):
			B0=f"https://daotranslate.net/?s={L}";AN=P.get(B0);B1=f"https://manhuaaz.com/?s={L}&post_type=wp-manga&op=&author=&artist=&release=&adult=";AO=P.get(B1)
			if AN.status_code==200 and AO.status_code==200:
				B2=Z(AN.text,b);B3=Z(AO.text,b);AP=B2.find(c,{l:Ad});AQ=B3.find_all('a',href=lambda href:href and href.startswith(v))
				if AP and AQ:
					A0=AP.find_all(c,{l:Ae});A1=iter(AQ)
					for W in A0:
						if AL>=3:break
						A2=W.a[m];g=A2.split(Af)[1].replace(w,B).title();A3=g.replace('-',k);o=f"https://daotranslate.net/{g}-chapter-1/"
						with A.spinner(Ac):
							h,F,i=A.columns(3)
							with F:A.write(f"[{A3}]({o})")
							G=W.img[t];M=o;C,J=V(M)
							if G:
								try:
									N=f(G,scale_factor=4);h,F,i=A.columns(3)
									with F:A.image(N,use_column_width=None)
								except:pass
							if o:
								h,F,i=A.columns(3)
								with F:H=f"\n                                    {C}\n                                    ";I=a(C,J);A.code(H,language=d);A.button(u,on_click=n,args=[I],key=y())
							A.divider();AL+=1
							try:
								Q=next(A1);E=Q.get(m)
								if Ag not in E:X=f"{E}chapter-1/"
								else:X=E
								Y=E.split(v)[1];Y=Y.replace(w,B);R=Q.find(s);M=X;C,J=V(M)
								if R:
									if AM>=3:break
									h,F,i=A.columns(3)
									with F:A.write(f"[{Y}]({X})")
									G=R.get(AB)
									try:
										N=f(G,scale_factor=4);h,F,i=A.columns(3)
										with F:A.image(N,use_column_width=None)
									except:pass
									h,F,i=A.columns(3)
									with F:H=f"\n                                    \t{C}\n                                    \t";A.code(H,language=d);A.caption(x);A.divider();AM+=1
							except StopIteration:break
B4,B5,B6=A.columns(3)
BN=A.columns([1,2])
AR=0
with B4:
	B7=AD.choice(string.ascii_uppercase)
	with A.expander(':loud_sound: Text & Audio '):
		S=P.get(f"https://daotranslate.net/?s={B7}")
		if S.status_code==200:
			j=Z(S.text,b);AS=j.find(c,{l:Ad})
			if AS:
				A0=AS.find_all(c,{l:Ae})
				for W in A0:
					if AR>=3:break
					A2=W.a[m];g=A2.split(Af)[1].replace(w,B).title();A3=g.replace('-',k);A4=f"https://daotranslate.net/{g}-chapter-1/";A.write(f"[{A3}]({A4})");G=W.img[t];M=A4;C,J=V(M)
					if G:
						try:N=f(G,scale_factor=4);A.image(N,use_column_width=AC)
						except:pass
					if A4:H=f"\n                        {C}\n                        ";I=a(C,J);A.code(H,language=d);A.button(u,on_click=n,args=[I],key=y())
					A.divider();AR+=1
AT=0
with B5:
	with A.expander(f":chart_with_upwards_trend: Top Rated"):
		S=P.get('https://nightcomic.com/')
		if S.status_code==200:
			j=Z(S.text,b);B8=j.find_all(c,class_='page-item-detail manga')
			for p in B8:
				Q=p.find('a',class_='btn-link');R=p.find(s);W=p.find('h3',class_='h5').text.strip();B9=p.find('span',class_='score').text.strip()
				if Q and R:
					if AT>=3:break
					E=Q.get(m);G=R.get(AB);M=E;C,J=V(M);I=a(C,J);A.write(f"[{W}]({E}) - Rating: {B9}")
					try:N=f(G,scale_factor=4);A.image(N,use_column_width=AC)
					except:pass
					H=f"\n                    {C}\n                    ";A.code(H,language=d);A.caption(x);A.divider();AT+=1
AU=0
with B6:
	with A.expander(f":frame_with_picture: Panels"):
		S=P.get('https://manhuaaz.com/')
		if S.status_code==200:
			j=Z(S.text,b);A1=j.find_all('a',href=lambda href:href and href.startswith(v))
			for Q in A1:
				E=Q.get(m)
				if Ag not in E:X=f"{E}chapter-1/"
				else:X=E
				Y=E.split(v)[1];Y=Y.replace(w,B);R=Q.find(s);M=X;C,J=V(M)
				if R:
					if AU>=3:break
					A.write(f"[{Y}]({X})");G=R.get(AB)
					try:N=f(G,scale_factor=4);A.image(N,use_column_width=AC)
					except:pass
					I=a(C,J);H=f"\n                    {C}\n                    ";A.code(H,language=d);A.caption(x);A.divider();AU+=1
A.image(At)
q=A.empty()
I=a(A.text_input(':orange[Manga Code:]',value=B,placeholder='iuuqt://ebhdrrghmbuf.vt/..',key='readfield',help='Enter Manga Code here'),J)
BA=A.button(':green_book: Read',help=u,key='readbutton',use_container_width=D)
if BA:
	if Ah in I:
		with A.spinner('Loading, please be patient..'):n(I)
	if Ah not in I.lower():
		with A.spinner(AY):
			BB=z();A.session_state.image_links=AE(I);A.session_state.current_image_index=0
			if A.session_state.image_links:
				for BC in A.session_state.image_links:A.image(BC,use_column_width=K)
				A.write(f"Total Images: {O(A.session_state.image_links)}");AF(A.session_state.image_links);AV=I;A5=B.join([A for A in AV if A.isdigit()]);BD=T(U(A5)+U(+1));BE=T(U(A5));BF=T(AV.replace(A5,BD));C,J=V(BF);A.caption(AZ+BE+Aa+C);H=f"\n                {C}\n                ";A.code(H,language=d);A.caption(x)
A.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=K)
A.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=K)

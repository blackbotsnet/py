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
Al='daotrans'
Ak='.list-chapter .chapter-item a.btn-link'
Aj='page-item-detail manga'
Ai='series/'
Ah='mdthumb'
Ag='https://manhuaaz.com/manga/'
Af='listupd'
Ae='Searching..'
Ad='Restart'
Ac='\n\n:orange[Next Chapter:] '
Ab=':green[Chapter Complete:] '
Aa='Loading text & audio..'
AZ='current_image_index'
AY='image_links'
AE='always'
AD='PANEL/'
AC='NOVEL/'
AB='TOP/'
w='Copy Code'
v='a'
u=None
t='Read'
s='img'
r=chr
l=' '
c='java'
b='html.parser'
a=Exception
Y='href'
X='div'
W='src'
T=len
O='class'
N=str
J=False
I=int
C=True
B=''
import os,io,base64,hashlib,random as AF,string,tempfile as Am,time,uuid
from io import BytesIO as AG
import re,requests as K
from PIL import Image as P
import numpy as BN,pandas as BO,pickle
from paddleocr import PaddleOCR as An
from gtts import gTTS
from pydub import AudioSegment as Ao
from pydub.effects import speedup
import streamlit as A,streamlit_nested_layout,streamlit.components.v1 as BP,streamlit_scrollable_textbox as Ap,streamlit_extras
from bs4 import BeautifulSoup as Z
from selenium import webdriver as Aq
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as Ar
from webdriver_manager.chrome import ChromeDriverManager as As
from webdriver_manager.core.os_manager import ChromeType as At
import webbrowser
from utils import recommendations,read_object
def x():A=N(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def Au(file_path):
	with open(file_path,'rb')as B:D=B.read();E=base64.b64encode(D).decode();F=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{E}" type="audio/mp3">\n            </audio>\n            ';A.markdown(F,unsafe_allow_html=C)
def y():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',J);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return Aq.Chrome(service=Service(As(chrome_type=At.CHROMIUM).install()),options=A)
def BQ(url):
	if AY not in A.session_state:A.session_state.image_links=[]
	if AZ not in A.session_state:A.session_state.current_image_index=0
	try:BI.get(url)
	except:A.stop();pass
	with A.spinner(Aa):
		A.session_state.image_links=AH(url);A.session_state.current_image_index=0
		if A.session_state.image_links:
			for B in A.session_state.image_links:A.image(B,use_column_width=C)
			A.write(f"Total Images: {T(A.session_state.image_links)}");AI(A.session_state.image_links)
def AH(url):
	B=y()
	try:B.get(url)
	except Ar as M:
		if B.current_url==url:return[]
		else:A.stop();return[]
	C=[];G=B.find_elements(By.CSS_SELECTOR,s)
	for H in G:
		D=H.get_attribute(W)
		if D and z(D):C.append(D)
	I=B.find_elements(By.CSS_SELECTOR,'img[id^="image-"]')
	for J in I:
		E=J.get_attribute(W)
		if E and z(E):C.append(E)
	K=B.find_elements(By.CSS_SELECTOR,'img.wp-manga-chapter-img')
	for L in K:
		F=L.get_attribute(W)
		if F and z(F):C.append(F)
	B.quit();return C
def AI(image_links):
	M='converted_img.jpg';G=[];O=An(use_angle_cls=C,lang='en');H=[]
	for(X,E)in enumerate(image_links,start=1):
		if not Av(E):continue
		with A.spinner(' Getting image text '):
			try:Q=K.get(E).content;R=io.BytesIO(Q);S=P.open(R);T=S.convert('RGB');T.save(M,'JPEG')
			except a as I:continue
			try:
				U=O.ocr(M,det=J,cls=C);V=U[0][0][0];D=Aw(N(V));H.append(D);L=l.join(H);A.write('All Text:',L)
				if L:
					F=os.path.join('audio',os.path.splitext(os.path.basename(E))[0]+'.mp3')
					if not os.path.exists(F):W=gTTS(text=D,lang='en',slow=J);W.save(F)
					G.append(F)
					if AJ:q.markdown(f":blue[Streaming: ]:green[*{D}*]")
				else:q.markdown(f":blue[Dao: ]:orange[No Text]")
			except a as I:A.write(f"Error processing text: {I}");D=B
	return G
def Av(image_url):
	A=['.png','.jpg','.jpeg','.webp']
	for format in A:
		if image_url.lower().endswith(format):return C
	return J
def z(link):
	A=['.png','.jpg','.jpeg','.webp']
	for B in A:
		if link.lower().endswith(B):return C
	return J
def Aw(text):
	C=text
	try:
		if not isinstance(C,N):raise ValueError('Input must be a string')
		D='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';E=re.findall(D,C);F=l.join(E);C=F.lower()
	except a as G:A.write(f"Error filtering English words: {G}");C=B
	return C
def m(url):
	c='file.mp3';P='\n';E=url;G=y()
	try:G.get(E)
	except:pass
	if not E:q.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
	else:
		try:
			Q=K.get(E)
			if Q.status_code==200:
				d=Z(Q.text,b);H=d.find(X,{O:'epcontent entry-content'})
				if H:
					v=B;e=T(H.findAll('p'));F=H.findAll('p');L=1;w=e//L;f=[F[A:A+L]for A in range(0,T(F),L)];D=B
					for g in F:D+=g.text+P
					D=D.replace('<p>',B);D=D.replace('"',B);A.markdown('<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>',unsafe_allow_html=C)
					with A.expander(t):from annotated_text import annotated_text as h;F=D.split(P);i=[(A,B,'#fea')for A in F];h(*i);A.caption(f"{T(D)} characters in this chapter.");R=E;M=B.join([A for A in R if A.isdigit()]);S=N(I(M)+I(+1));j=N(I(M));k=N(R.replace(M,S));V,l=U(k);A.caption(Ab+j+Ac+S);A.caption(V);E=n(V,l);A.button('Continue',on_click=m,args=[E],key=x())
					with Am.NamedTemporaryFile(suffix='.mp3',delete=J)as W:D=D.replace('"',B);o=gTTS(text=D,lang='en',slow=J);o.save(W.name);p=Ao.from_mp3(W.name);r=speedup(p,1.2,150);r.export(c,format='mp3');Au(c)
					for s in f:
						u=B
						for Y in s:u+=Y.text+P
						if AJ:q.markdown(f":blue[Dao: ]:green[*{Y.text}*]");time.sleep(5)
					G.quit()
				else:A.write(B)
			else:A.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
		except a as z:pass
	G.quit()
def U(text):
	C=text;D={}
	for E in range(26):D[r(65+E)]=r((E+1)%26+65);D[r(97+E)]=r((E+1)%26+97)
	A=B.join(D.get(A,A)for A in C)
	if'nightcomic.com'in C:A=AB+A
	if'daotranslate'in C:A=AC+A
	if'manhuaaz.com'in C:A=AD+A
	return A,D
def n(obfuscated_text,mapping):
	A=obfuscated_text
	if A.startswith(AB):A=A[T(AB):]
	if A.startswith(AC):A=A[T(AC):]
	if A.startswith(AD):A=A[T(AD):]
	C={B:A for(A,B)in mapping.items()};D=B.join(C.get(A,A)for A in A);return D
BR=[]
o=B
Ax=P.open('static/-.ico')
BS=AF.randint(1,99999)
A.set_page_config(page_title='Manga Dōjutsu',page_icon=Ax,layout='centered',initial_sidebar_state='expanded')
A.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}\n        [data-testid='stSidebarNav'] > ul {color: red;}\n        .language-java {color: black;}\n        .css-nps9tx, .e1m3hlzs0, .css-1p0bytv, .e1m3hlzs1 {\n        visibility: collapse;\n        height: 0px;\n        }\n\t .stException {\n\t    display: none;\n\t}\n    </style>\n",unsafe_allow_html=C)
Ay=P.open('static/dojutsu.png')
Az=P.open('static/4.png')
A.sidebar.write('BlackDao: Manga Dōjutsu')
if AY not in A.session_state:A.session_state.image_links=[]
if AZ not in A.session_state:A.session_state.current_image_index=0
BT=u
with A.sidebar:
	if'value'not in A.session_state:A.session_state.value=B
	def A_():A.session_state.value=Ad
	A.image(Az);A.caption('Manga Text or Image To Speach');AJ=A.checkbox('Stream Story (Experimental)',value=J,disabled=J)
	with open('titles.txt','r')as B0:B1=B0.readlines()
	B2=B1;Ap.scrollableTextbox(B2,height=300,border=u);A.divider();A.header('Google Play Store');A.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');A.header('Official PC Version');A.caption('Download from: https://blackbots.gumroad.com/l/manga');A.caption('Join Our Discord: https://discord.gg/HcVPaSpF');A.divider()
	with A.expander('Help'):A.caption('How to use BlackDao: Manga Dōjutsu');A.caption('- `Copy` a Code');A.caption('- `Paste` Code onto `Manga Code` field');A.caption('- `Press Read`')
	A.button(Ad,on_click=A_,key='keyy')
def A0(img_url,scale_factor):A=scale_factor;C=K.get(img_url);B=P.open(AG(C.content));D,E=B.size;F=I(D*A);G=I(E*A);H=B.resize((F,G),P.LANCZOS);return H
def AK(img_url,scale_factor):B=scale_factor;D=K.get(img_url);C=P.open(AG(D.content));E,F=C.size;G=I(E*B);H=I(F*B);J=C.resize((G,H),P.LANCZOS);A=io.BytesIO();J.save(A,format='PNG');A=A.getvalue();return A
L=A.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
AL=0
AM=0
if L:
	L=L.replace('"',B);L=L.replace('-',l);L=L.replace(':',B)
	with A.spinner(Ae):
		with A.expander(':mag: Search'):
			B3=f"https://daotranslate.net/?s={L}";AN=K.get(B3);B4=f"https://manhuaaz.com/?s={L}&post_type=wp-manga&op=&author=&artist=&release=&adult=";AO=K.get(B4)
			if AN.status_code==200 and AO.status_code==200:
				B5=Z(AN.text,b);B6=Z(AO.text,b);AP=B5.find(X,{O:Af});AQ=B6.find_all(v,href=lambda href:href and href.startswith(Ag))
				if AP and AQ:
					A1=AP.find_all(X,{O:Ah});B7=iter(AQ)
					for d in A1:
						if AL>=10:break
						A2=d.a[Y];e=A2.split(Ai)[1].replace('/',B).title();A3=e.replace('-',l);o=f"https://daotranslate.net/{e}-chapter-1/"
						with A.spinner(Ae):
							f,E,g=A.columns(3)
							with E:A.write(f"[{A3}]({o})")
							F=d.img[W];h=o;D,Q=U(h)
							if F:
								try:
									i=A0(F,scale_factor=4);f,E,g=A.columns(3)
									with E:A.image(i,use_column_width=u)
								except:pass
							if o:
								f,E,g=A.columns(3)
								with E:G=f"\n                                    {D}\n                                    ";M=n(D,Q);A.code(G,language=c);A.button(t,on_click=m,args=[M],key=x())
							A.divider();AL+=1
							try:
								AR=next(B7);p=AR.get(Y)
								if'chapter'not in p:A4=f"{p}chapter-1/"
								else:A4=p
								A5=p.split(Ag)[1];A5=A5.replace('/',B);R=AR.find(s);h=A4;D,Q=U(h)
								if R:
									if AM>=10:break
									f,E,g=A.columns(3)
									with E:A.write(f"[{A5}]({A4})")
									F=R.get('data-src')
									try:
										i=A0(F,scale_factor=4);f,E,g=A.columns(3)
										with E:A.image(i,use_column_width=u)
									except:pass
									f,E,g=A.columns(3)
									with E:G=f"\n                                    \t{D}\n                                    \t";A.code(G,language=c);A.caption(w);A.divider();AM+=1
							except StopIteration:break
B8,B9,BA=A.columns(3)
BU=A.columns([1,2])
AS=0
with B8:
	BB=AF.choice(string.ascii_uppercase)
	with A.expander(':loud_sound: Text & Audio '):
		S=K.get(f"https://daotranslate.net/?s={BB}")
		if S.status_code==200:
			j=Z(S.text,b);AT=j.find(X,{O:Af})
			if AT:
				A1=AT.find_all(X,{O:Ah})
				for d in A1:
					if AS>=10:break
					A2=d.a[Y];e=A2.split(Ai)[1].replace('/',B).title();A3=e.replace('-',l);A6=f"https://daotranslate.net/{e}-chapter-1/";A.write(f"[{A3}]({A6})");F=d.img[W];h=A6;D,Q=U(h)
					if F:
						try:i=A0(F,scale_factor=4);A.image(i,use_column_width=AE)
						except:pass
					if A6:G=f"\n                        {D}\n                        ";M=n(D,Q);A.code(G,language=c);A.button(t,on_click=m,args=[M],key=x());A.divider();AS+=1
AU=0
with B9:
	with A.expander(f":chart_with_upwards_trend: Top Rated"):
		S=K.get('https://mangatx.to/')
		if S.status_code==200:
			j=Z(S.text,b);A7=j.find_all(X,{O:Aj})
			for H in A7:
				if AU>=10:break
				A8=H.find('h3',{O:'h5'}).text.strip();BC=H.find(v,href=C)[Y];k=H.select(Ak)
				if k:V=k[0][Y]
				else:V=B
				A.write(f"[{A8}]({V})");R=H.find(s,src=C)
				if R:
					F=R[W]
					try:A9=AK(F,scale_factor=4);A.image(A9,use_column_width=AE)
					except a as BD:pass
				D,Q=U(V);G=f"{D}";A.code(G,language=c);A.caption(w);A.divider();AU+=1
AV=0
with BA:
	with A.expander(f":frame_with_picture: Updated"):
		S=K.get('https://www.mangaread.org/')
		if S.status_code==200:
			j=Z(S.text,b);A7=j.find_all(X,{O:Aj})
			for H in A7:
				if AV>=10:break
				A8=H.find('h3',{O:'h5'}).text.strip();BC=H.find(v,href=C)[Y];k=H.select(Ak)
				if k:V=k[0][Y]
				else:V=B
				A.write(f"[{A8}]({V})");R=H.find(s,src=C)
				if R:
					F=R[W]
					try:A9=AK(F,scale_factor=4);A.image(A9,use_column_width=AE)
					except a as BD:pass
				BE=H.select('.list-chapter .chapter-item')
				for AW in BE:BF=AW.find(v,class_='btn-link').text.strip();BG=AW.find('span',class_='post-on').text.strip()
				A.write(f"Chapter: {BF}");A.write(f"Released: {BG}");D,Q=U(V);G=f"{D}";A.code(G,language=c);A.caption(w);A.divider();AV+=1
A.image(Ay)
q=A.empty()
M=n(A.text_input(':orange[Manga Code:]',value=B,placeholder='iuuqt://ebhdrrghmbuf.vt/..',key='readfield',help='Enter Manga Code here'),Q)
BH=A.button(':green_book: Read',help=t,key='readbutton',use_container_width=J)
if BH:
	if Al in M:
		with A.spinner('Loading, please be patient..'):m(M)
	if Al not in M.lower():
		with A.spinner(Aa):
			BI=y();A.session_state.image_links=AH(M);A.session_state.current_image_index=0
			if A.session_state.image_links:
				for BJ in A.session_state.image_links:A.image(BJ,use_column_width=C)
				A.write(f"Total Images: {T(A.session_state.image_links)}");AI(A.session_state.image_links);AX=M;AA=B.join([A for A in AX if A.isdigit()]);BK=N(I(AA)+I(+1));BL=N(I(AA));BM=N(AX.replace(AA,BK));D,Q=U(BM);A.caption(Ab+BL+Ac+D);G=f"\n                {D}\n                ";A.code(G,language=c);A.caption(w)
A.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=C)
A.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=C)

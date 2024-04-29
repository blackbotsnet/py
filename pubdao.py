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
Ap='daotrans'
Ao='.list-chapter .chapter-item a.btn-link'
An='page-item-detail manga'
Am='series/'
Al='mdthumb'
Ak='https://manhuaaz.com/manga/'
Aj='listupd'
Ai='Searching..'
Ah='Restart'
Ag='\n\n:orange[Next Chapter:] '
Af=':green[Chapter Complete:] '
Ae='Loading text & audio..'
Ad='current_image_index'
Ac='image_links'
AF='always'
AE='PANEL/'
AD='NOVEL/'
AC='TOP/'
AB=range
v='Copy Code'
u='a'
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
P='class'
O=len
N=str
J=False
I=int
C=True
B=''
import os,io,base64,hashlib,random as AG,string,tempfile as Aq,time,uuid
from io import BytesIO as AH
import re,requests as K
from PIL import Image as Q
import numpy as BR,pandas as BS,pickle
from paddleocr import PaddleOCR as Ar
from gtts import gTTS
from pydub import AudioSegment as As
from pydub.effects import speedup
import streamlit as A,streamlit_nested_layout,streamlit.components.v1 as BT,streamlit_extras
from bs4 import BeautifulSoup as Z
from selenium import webdriver as At
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as Au
from webdriver_manager.chrome import ChromeDriverManager as Av
from webdriver_manager.core.os_manager import ChromeType as Aw
import webbrowser
from utils import recommendations,read_object
def w():A=N(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def Ax(file_path):
	with open(file_path,'rb')as B:D=B.read();E=base64.b64encode(D).decode();F=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{E}" type="audio/mp3">\n            </audio>\n            ';A.markdown(F,unsafe_allow_html=C)
def x():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',J);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return At.Chrome(service=Service(Av(chrome_type=Aw.CHROMIUM).install()),options=A)
def BU(url):
	if Ac not in A.session_state:A.session_state.image_links=[]
	if Ad not in A.session_state:A.session_state.current_image_index=0
	try:BM.get(url)
	except:pass
	with A.spinner(Ae):
		A.session_state.image_links=AI(url);A.session_state.current_image_index=0
		if A.session_state.image_links:
			for B in A.session_state.image_links:A.image(B,use_column_width=C)
			A.write(f"Total Images: {O(A.session_state.image_links)}");AJ(A.session_state.image_links)
def AI(url):
	B=x()
	try:B.get(url)
	except Au as G:
		if B.current_url==url:return[]
		else:A.write(f"Error loading URL: {G}");return[]
	C=[];H=B.find_elements(By.CSS_SELECTOR,s)
	for I in H:
		D=I.get_attribute(W)
		if D and y(D):C.append(D)
	J=B.find_elements(By.CSS_SELECTOR,'img[id^="image-"]')
	for K in J:
		E=K.get_attribute(W)
		if E and y(E):C.append(E)
	L=B.find_elements(By.CSS_SELECTOR,'img.wp-manga-chapter-img')
	for M in L:
		F=M.get_attribute(W)
		if F and y(F):C.append(F)
	B.quit();return C
def AJ(image_links):
	M='converted_img.jpg';G=[];O=Ar(use_angle_cls=C,lang='en');H=[]
	for(X,E)in enumerate(image_links,start=1):
		if not Ay(E):continue
		with A.spinner(' Getting image text '):
			try:P=K.get(E).content;R=io.BytesIO(P);S=Q.open(R);T=S.convert('RGB');T.save(M,'JPEG')
			except a as I:continue
			try:
				U=O.ocr(M,det=J,cls=C);V=U[0][0][0];D=Az(N(V));H.append(D);L=l.join(H);A.write('All Text:',L)
				if L:
					F=os.path.join('audio',os.path.splitext(os.path.basename(E))[0]+'.mp3')
					if not os.path.exists(F):W=gTTS(text=D,lang='en',slow=J);W.save(F)
					G.append(F)
					if AK:q.markdown(f":blue[Streaming: ]:green[*{D}*]")
				else:q.markdown(f":blue[Dao: ]:orange[No Text]")
			except a as I:A.write(f"Error processing text: {I}");D=B
	return G
def Ay(image_url):
	A=['.png','.jpg','.jpeg','.webp']
	for format in A:
		if image_url.lower().endswith(format):return C
	return J
def y(link):
	A=['.png','.jpg','.jpeg','.webp']
	for B in A:
		if link.lower().endswith(B):return C
	return J
def Az(text):
	C=text
	try:
		if not isinstance(C,N):raise ValueError('Input must be a string')
		D='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';E=re.findall(D,C);F=l.join(E);C=F.lower()
	except a as G:A.write(f"Error filtering English words: {G}");C=B
	return C
def m(url):
	c='file.mp3';Q='\n';E=url;G=x()
	try:G.get(E)
	except:pass
	if not E:q.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
	else:
		try:
			R=K.get(E)
			if R.status_code==200:
				d=Z(R.text,b);H=d.find(X,{P:'epcontent entry-content'})
				if H:
					y=B;e=O(H.findAll('p'));F=H.findAll('p');L=1;z=e//L;f=[F[A:A+L]for A in AB(0,O(F),L)];D=B
					for g in F:D+=g.text+Q
					D=D.replace('<p>',B);D=D.replace('"',B);A.markdown('<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>',unsafe_allow_html=C)
					with A.expander(t):from annotated_text import annotated_text as h;F=D.split(Q);i=[(A,B,'#fea')for A in F];h(*i);A.caption(f"{O(D)} characters in this chapter.");S=E;M=B.join([A for A in S if A.isdigit()]);T=N(I(M)+I(+1));j=N(I(M));k=N(S.replace(M,T));V,l=U(k);A.caption(Af+j+Ag+T);A.caption(V);E=n(V,l);A.button('Continue',on_click=m,args=[E],key=w())
					with Aq.NamedTemporaryFile(suffix='.mp3',delete=J)as W:D=D.replace('"',B);o=gTTS(text=D,lang='en',slow=J);o.save(W.name);p=As.from_mp3(W.name);r=speedup(p,1.2,150);r.export(c,format='mp3');Ax(c)
					for s in f:
						u=B
						for Y in s:u+=Y.text+Q
						if AK:q.markdown(f":blue[Dao: ]:green[*{Y.text}*]");time.sleep(5)
					G.quit()
				else:A.write(B)
			else:A.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
		except a as v:A.write(f":blue[Dao: ]:green[*Error occurred: {v}*]")
	G.quit()
def U(text):
	C=text;D={}
	for E in AB(26):D[r(65+E)]=r((E+1)%26+65);D[r(97+E)]=r((E+1)%26+97)
	A=B.join(D.get(A,A)for A in C)
	if'nightcomic.com'in C:A=AC+A
	if'daotranslate'in C:A=AD+A
	if'manhuaaz.com'in C:A=AE+A
	return A,D
def n(obfuscated_text,mapping):
	A=obfuscated_text
	if A.startswith(AC):A=A[O(AC):]
	if A.startswith(AD):A=A[O(AD):]
	if A.startswith(AE):A=A[O(AE):]
	C={B:A for(A,B)in mapping.items()};D=B.join(C.get(A,A)for A in A);return D
BV=[]
o=B
A_=Q.open('static/-.ico')
BW=AG.randint(1,99999)
A.set_page_config(page_title='Manga Dōjutsu',page_icon=A_,layout='centered',initial_sidebar_state='expanded')
A.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}\n        [data-testid='stSidebarNav'] > ul {color: red;}\n        .language-java {color: black;}\n    </style>\n",unsafe_allow_html=C)
B0=Q.open('static/dojutsu.png')
B1=Q.open('static/4.png')
A.sidebar.write('BlackDao: Manga Dōjutsu')
if Ac not in A.session_state:A.session_state.image_links=[]
if Ad not in A.session_state:A.session_state.current_image_index=0
BX=None
with A.sidebar:
	if'value'not in A.session_state:A.session_state.value=B
	def B2():A.session_state.value=Ah
	A.image(B1);A.caption('Manga Text or Image To Speach');AK=A.checkbox('Stream Story (Experimental)',value=J,disabled=J)
	with open('titles.txt','r')as B3:AL=B3.readlines()
	AM=O(AL);B4=(AM-1)//10+1;AN=A.slider('Popular Titles',1,B4,1);B5=(AN-1)*10;B6=min(AN*10,AM)
	for B7 in AB(B5,B6):A.write(AL[B7])
	A.divider();A.header('Google Play Store');A.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');A.header('Official PC Version');A.caption('Download from: https://blackbots.gumroad.com/l/manga');A.caption('Join Our Discord: https://discord.gg/HcVPaSpF');A.divider()
	with A.expander('Help'):A.caption('How to use BlackDao: Manga Dōjutsu');A.caption('- `Copy` a Code');A.caption('- `Paste` Code onto `Manga Code` field');A.caption('- `Press Read`')
	A.button(Ah,on_click=B2,key='keyy')
def z(img_url,scale_factor):A=scale_factor;C=K.get(img_url);B=Q.open(AH(C.content));D,E=B.size;F=I(D*A);G=I(E*A);H=B.resize((F,G),Q.LANCZOS);return H
def AO(img_url,scale_factor):B=scale_factor;D=K.get(img_url);C=Q.open(AH(D.content));E,F=C.size;G=I(E*B);H=I(F*B);J=C.resize((G,H),Q.LANCZOS);A=io.BytesIO();J.save(A,format='PNG');A=A.getvalue();return A
L=A.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
AP=0
AQ=0
if L:
	L=L.replace('"',B);L=L.replace('-',l);L=L.replace(':',B)
	with A.spinner(Ai):
		with A.expander(':mag: Search'):
			B8=f"https://daotranslate.net/?s={L}";AR=K.get(B8);B9=f"https://manhuaaz.com/?s={L}&post_type=wp-manga&op=&author=&artist=&release=&adult=";AS=K.get(B9)
			if AR.status_code==200 and AS.status_code==200:
				BA=Z(AR.text,b);BB=Z(AS.text,b);AT=BA.find(X,{P:Aj});AU=BB.find_all(u,href=lambda href:href and href.startswith(Ak))
				if AT and AU:
					A0=AT.find_all(X,{P:Al});BC=iter(AU)
					for d in A0:
						if AP>=3:break
						A1=d.a[Y];e=A1.split(Am)[1].replace('/',B).title();A2=e.replace('-',l);o=f"https://daotranslate.net/{e}-chapter-1/"
						with A.spinner(Ai):
							f,E,g=A.columns(3)
							with E:A.write(f"[{A2}]({o})")
							F=d.img[W];h=o;D,R=U(h)
							if F:
								try:
									i=z(F,scale_factor=4);f,E,g=A.columns(3)
									with E:A.image(i,use_column_width=None)
								except:pass
							if o:
								f,E,g=A.columns(3)
								with E:G=f"\n                                    {D}\n                                    ";M=n(D,R);A.code(G,language=c);A.button(t,on_click=m,args=[M],key=w())
							A.divider();AP+=1
							try:
								AV=next(BC);p=AV.get(Y)
								if'chapter'not in p:A3=f"{p}chapter-1/"
								else:A3=p
								A4=p.split(Ak)[1];A4=A4.replace('/',B);S=AV.find(s);h=A3;D,R=U(h)
								if S:
									if AQ>=3:break
									f,E,g=A.columns(3)
									with E:A.write(f"[{A4}]({A3})")
									F=S.get('data-src')
									try:
										i=z(F,scale_factor=4);f,E,g=A.columns(3)
										with E:A.image(i,use_column_width=None)
									except:pass
									f,E,g=A.columns(3)
									with E:G=f"\n                                    \t{D}\n                                    \t";A.code(G,language=c);A.caption(v);A.divider();AQ+=1
							except StopIteration:break
BD,BE,BF=A.columns(3)
BY=A.columns([1,2])
AW=0
with BD:
	BG=AG.choice(string.ascii_uppercase)
	with A.expander(':loud_sound: Text & Audio '):
		T=K.get(f"https://daotranslate.net/?s={BG}")
		if T.status_code==200:
			j=Z(T.text,b);AX=j.find(X,{P:Aj})
			if AX:
				A0=AX.find_all(X,{P:Al})
				for d in A0:
					if AW>=3:break
					A1=d.a[Y];e=A1.split(Am)[1].replace('/',B).title();A2=e.replace('-',l);A5=f"https://daotranslate.net/{e}-chapter-1/";A.write(f"[{A2}]({A5})");F=d.img[W];h=A5;D,R=U(h)
					if F:
						try:i=z(F,scale_factor=4);A.image(i,use_column_width=AF)
						except:pass
					if A5:G=f"\n                        {D}\n                        ";M=n(D,R);A.code(G,language=c);A.button(t,on_click=m,args=[M],key=w());A.divider();AW+=1
AY=0
with BE:
	with A.expander(f":chart_with_upwards_trend: Top Rated"):
		T=K.get('https://mangatx.to/')
		if T.status_code==200:
			j=Z(T.text,b);A6=j.find_all(X,{P:An})
			for H in A6:
				if AY>=3:break
				A7=H.find('h3',{P:'h5'}).text.strip();BH=H.find(u,href=C)[Y];k=H.select(Ao)
				if k:V=k[0][Y]
				else:V=B
				A.write(f"[{A7}]({V})");S=H.find(s,src=C)
				if S:
					F=S[W]
					try:A8=AO(F,scale_factor=4);A.image(A8,use_column_width=AF)
					except a as A9:print(A9)
				D,R=U(V);G=f"{D}";A.code(G,language=c);A.caption(v);A.divider();AY+=1
AZ=0
with BF:
	with A.expander(f":frame_with_picture: Updated"):
		T=K.get('https://www.mangaread.org/')
		if T.status_code==200:
			j=Z(T.text,b);A6=j.find_all(X,{P:An})
			for H in A6:
				if AZ>=3:break
				A7=H.find('h3',{P:'h5'}).text.strip();BH=H.find(u,href=C)[Y];k=H.select(Ao)
				if k:V=k[0][Y]
				else:V=B
				A.write(f"[{A7}]({V})");S=H.find(s,src=C)
				if S:
					F=S[W]
					try:A8=AO(F,scale_factor=4);A.image(A8,use_column_width=AF)
					except a as A9:print(A9)
				BI=H.select('.list-chapter .chapter-item')
				for Aa in BI:BJ=Aa.find(u,class_='btn-link').text.strip();BK=Aa.find('span',class_='post-on').text.strip()
				A.write(f"Chapter: {BJ}");A.write(f"Released: {BK}");D,R=U(V);G=f"{D}";A.code(G,language=c);A.caption(v);A.divider();AZ+=1
A.image(B0)
q=A.empty()
M=n(A.text_input(':orange[Manga Code:]',value=B,placeholder='iuuqt://ebhdrrghmbuf.vt/..',key='readfield',help='Enter Manga Code here'),R)
BL=A.button(':green_book: Read',help=t,key='readbutton',use_container_width=J)
if BL:
	if Ap in M:
		with A.spinner('Loading, please be patient..'):m(M)
	if Ap not in M.lower():
		with A.spinner(Ae):
			BM=x();A.session_state.image_links=AI(M);A.session_state.current_image_index=0
			if A.session_state.image_links:
				for BN in A.session_state.image_links:A.image(BN,use_column_width=C)
				A.write(f"Total Images: {O(A.session_state.image_links)}");AJ(A.session_state.image_links);Ab=M;AA=B.join([A for A in Ab if A.isdigit()]);BO=N(I(AA)+I(+1));BP=N(I(AA));BQ=N(Ab.replace(AA,BO));D,R=U(BQ);A.caption(Af+BP+Ag+D);G=f"\n                {D}\n                ";A.code(G,language=c);A.caption(v)
A.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=C)
A.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=C)

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
A_='daotrans'
Az='Loading, please be patient..'
Ay='series/'
Ax='mdthumb'
Aw='listupd'
Av='Searching..'
Au='Restart'
At='Continue'
As='<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>'
Ar='Loading text & audio..'
Aq='current_image_index'
Ap='image_links'
AN='.list-chapter .chapter-item a.btn-link'
AM='PANEL/'
AL='NOVEL/'
AK='TOP/'
AJ='\n\n:orange[Next Chapter:] '
AI=':green[Chapter Complete:] '
AH='.mp3'
AG=range
A2='h3'
A1='page-item-detail manga'
A0='en'
v='Copy Code'
u='always'
t='a'
s='"'
r='\n'
q=' '
p='img'
f='Read'
e='java'
b='html.parser'
W='href'
V='src'
R='div'
Q=Exception
O=len
K=str
J=False
I=int
F='class'
D=True
B=''
import os,io,base64,hashlib,random as AO,string,tempfile as AP,time,uuid
from io import BytesIO as AQ
import re,requests as L
from PIL import Image as X
import numpy as BZ,pandas as Ba,pickle
from paddleocr import PaddleOCR as B0
from gtts import gTTS as A3
from pydub import AudioSegment as AR
from pydub.effects import speedup as AS
import streamlit as A,streamlit_nested_layout,streamlit.components.v1 as Bb,streamlit_scrollable_textbox as B1,streamlit_extras
from bs4 import BeautifulSoup as Y
from selenium import webdriver as B2
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as B3
from webdriver_manager.chrome import ChromeDriverManager as B4
from webdriver_manager.core.os_manager import ChromeType as B5
import webbrowser
from utils import recommendations,read_object
def w():A=K(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def AT(file_path):
	with open(file_path,'rb')as B:C=B.read();E=base64.b64encode(C).decode();F=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{E}" type="audio/mp3">\n            </audio>\n            ';A.markdown(F,unsafe_allow_html=D)
def x():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',J);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return B2.Chrome(service=Service(B4(chrome_type=B5.CHROMIUM).install()),options=A)
def Bc(url):
	if Ap not in A.session_state:A.session_state.image_links=[]
	if Aq not in A.session_state:A.session_state.current_image_index=0
	try:BU.get(url)
	except:A.stop();pass
	with A.spinner(Ar):
		A.session_state.image_links=AU(url);A.session_state.current_image_index=0
		if A.session_state.image_links:
			for B in A.session_state.image_links:A.image(B,use_column_width=D)
			A.write(f"Total Images: {O(A.session_state.image_links)}");AV(A.session_state.image_links)
def AU(url):
	B=x()
	try:B.get(url)
	except B3 as M:
		if B.current_url==url:return[]
		else:A.stop();return[]
	C=[];G=B.find_elements(By.CSS_SELECTOR,p)
	for H in G:
		D=H.get_attribute(V)
		if D and A4(D):C.append(D)
	I=B.find_elements(By.CSS_SELECTOR,'img[id^="image-"]')
	for J in I:
		E=J.get_attribute(V)
		if E and A4(E):C.append(E)
	K=B.find_elements(By.CSS_SELECTOR,'img.wp-manga-chapter-img')
	for L in K:
		F=L.get_attribute(V)
		if F and A4(F):C.append(F)
	B.quit();return C
def AV(image_links):
	N='converted_img.jpg';G=[];O=B0(use_angle_cls=D,lang=A0);H=[]
	for(Y,E)in enumerate(image_links,start=1):
		if not B6(E):continue
		with A.spinner(' Getting image text '):
			try:P=L.get(E).content;R=io.BytesIO(P);S=X.open(R);T=S.convert('RGB');T.save(N,'JPEG')
			except Q as I:continue
			try:
				U=O.ocr(N,det=J,cls=D);V=U[0][0][0];C=B7(K(V));H.append(C);M=q.join(H);A.write('All Text:',M)
				if M:
					F=os.path.join('audio',os.path.splitext(os.path.basename(E))[0]+AH)
					if not os.path.exists(F):W=A3(text=C,lang=A0,slow=J);W.save(F)
					G.append(F)
					if AW:o.markdown(f":blue[Streaming: ]:green[*{C}*]")
				else:o.markdown(f":blue[Dao: ]:orange[No Text]")
			except Q as I:A.write(f"Error processing text: {I}");C=B
	return G
def B6(image_url):
	A=['.png','.jpg','.jpeg','.webp']
	for format in A:
		if image_url.lower().endswith(format):return D
	return J
def A4(link):
	A=['.png','.jpg','.jpeg','.webp']
	for B in A:
		if link.lower().endswith(B):return D
	return J
def B7(text):
	C=text
	try:
		if not isinstance(C,K):raise ValueError('Input must be a string')
		D='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';E=re.findall(D,C);F=q.join(E);C=F.lower()
	except Q as G:A.write(f"Error filtering English words: {G}");C=B
	return C
def g(url):
	T='file.mp3';E=url;H=x()
	try:H.get(E)
	except:pass
	if not E:o.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
	else:
		try:
			U=L.get(E)
			if U.status_code==200:
				c=Y(U.text,b);M=c.find(R,{F:'epcontent entry-content'})
				if M:
					y=B;d=O(M.findAll('p'));G=M.findAll('p');N=1;z=d//N;e=[G[A:A+N]for A in AG(0,O(G),N)];C=B
					for i in G:C+=i.text+r
					C=C.replace('<p>',B);C=C.replace(s,B);A.markdown(As,unsafe_allow_html=D)
					with A.expander(f):from annotated_text import annotated_text as j;G=C.split(r);k=[(A,B,'#fea')for A in G];j(*k);A.caption(f"{O(C)} characters in this chapter.");V=E;P=B.join([A for A in V if A.isdigit()]);W=K(I(P)+I(+1));l=K(I(P));m=K(V.replace(P,W));X,n=S(m);A.caption(AI+l+AJ+W);A.caption(X);E=h(X,n);A.button(At,on_click=g,args=[E],key=w())
					with AP.NamedTemporaryFile(suffix=AH,delete=J)as Z:C=C.replace(s,B);p=A3(text=C,lang=A0,slow=J);p.save(Z.name);q=AR.from_mp3(Z.name);t=AS(q,1.2,150);t.export(T,format='mp3');AT(T);A.download_button(T)
					for u in e:
						v=B
						for a in u:v+=a.text+r
						if AW:o.markdown(f":blue[Dao: ]:green[*{a.text}*]");time.sleep(5)
					H.quit()
				else:A.write(B)
			else:A.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
		except Q as A1:pass
	H.quit()
def B8(url):
	E=url;M=x()
	try:M.get(E)
	except:pass
	if not E:o.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
	else:
		try:
			U=L.get(E)
			if U.status_code==200:
				a=Y(U.text,b);N=a.find(R,{F:'entry-content'})
				if N:
					p=B;c=O(N.findAll('p'));G=N.findAll('p');P=1;q=c//P;t=[G[A:A+P]for A in AG(0,O(G),P)];C=B
					for d in G:C+=d.text+r
					C=C.replace('<p>',B);C=C.replace(s,B);A.markdown(As,unsafe_allow_html=D)
					with A.expander(f):
						from annotated_text import annotated_text as e;G=C.split(r);i=[(A,B,'#fea')for A in G];e(*i);A.caption(f"{O(C)} characters in this chapter.");V=E;T=B.join([A for A in V if A.isdigit()]);W=K(I(T)+I(+1));H=K(I(T));j=K(V.replace(T,W));X,k=S(j);A.caption(AI+H+AJ+W);A.caption(X);E=h(X,k);A.button(At,on_click=g,args=[E],key=w())
						with AP.NamedTemporaryFile(suffix=AH,delete=J)as Z:C=C.replace(s,B);l=A3(text=C,lang=A0,slow=J);l.save(Z.name);m=AR.from_mp3(Z.name);n=AS(m,1.2,150);n.export(f"Chapter{H}.mp3",format='mp3');AT(f"Chapter{H}.mp3");A.download_button(f"Chapter{H}.mp3")
					M.quit()
				else:A.write(B)
			else:A.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
		except Q as u:pass
	M.quit()
def S(text):
	C=text;D={}
	for E in AG(26):D[chr(65+E)]=chr((E+1)%26+65);D[chr(97+E)]=chr((E+1)%26+97)
	A=B.join(D.get(A,A)for A in C)
	if'nightcomic.com'in C:A=AK+A
	if'daotranslate'in C:A=AL+A
	if'manhuaaz.com'in C:A=AM+A
	return A,D
def h(obfuscated_text,mapping):
	A=obfuscated_text
	if A.startswith(AK):A=A[O(AK):]
	if A.startswith(AL):A=A[O(AL):]
	if A.startswith(AM):A=A[O(AM):]
	C={B:A for(A,B)in mapping.items()};D=B.join(C.get(A,A)for A in A);return D
Bd=[]
y=B
B9=X.open('static/-.ico')
Be=AO.randint(1,99999)
A.set_page_config(page_title='Manga Dōjutsu',page_icon=B9,layout='centered',initial_sidebar_state='expanded')
A.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}\n        [data-testid='stSidebarNav'] > ul {color: red;}\n        .language-java {color: black;}\n        .css-nps9tx, .e1m3hlzs0, .css-1p0bytv, .e1m3hlzs1 {\n        visibility: collapse;\n        height: 0px;\n        }\n\t .stException {\n\t    display: none;\n\t}\n    </style>\n",unsafe_allow_html=D)
BA=X.open('static/dojutsu.png')
BB=X.open('static/4.png')
A.sidebar.write('BlackDao: Manga Dōjutsu')
if Ap not in A.session_state:A.session_state.image_links=[]
if Aq not in A.session_state:A.session_state.current_image_index=0
Bf=None
with A.sidebar:
	if'value'not in A.session_state:A.session_state.value=B
	def BC():A.session_state.value=Au
	A.image(BB);A.caption('Manga Text or Image To Speach');AW=A.checkbox('Stream Story (Experimental)',value=J,disabled=J)
	with open('titles.txt','r')as BD:BE=BD.readlines()
	BF=BE;A.write(':orange[Popular Titles]');B1.scrollableTextbox(BF,height=300,border=None);A.divider();A.header('Google Play Store');A.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');A.header('Official PC Version');A.caption('Download from: https://blackbots.gumroad.com/l/manga');A.caption('Join Our Discord: https://discord.gg/HcVPaSpF');A.divider()
	with A.expander('Help'):A.caption('How to use BlackDao: Manga Dōjutsu');A.caption('- `Copy` a Code');A.caption('- `Paste` Code onto `Manga Code` field');A.caption('- `Press Read`')
	A.button(Au,on_click=BC,key='keyy')
def AX(img_url,scale_factor):A=scale_factor;C=L.get(img_url);B=X.open(AQ(C.content));D,E=B.size;F=I(D*A);G=I(E*A);H=B.resize((F,G),X.LANCZOS);return H
def z(img_url,scale_factor):B=scale_factor;D=L.get(img_url);C=X.open(AQ(D.content));E,F=C.size;G=I(E*B);H=I(F*B);J=C.resize((G,H),X.LANCZOS);A=io.BytesIO();J.save(A,format='PNG');A=A.getvalue();return A
P=A.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
AY=0
if P:
	P=P.replace(s,B);P=P.replace('-',q);P=P.replace(':',B)
	with A.spinner(Av):
		with A.expander(':mag: Search'):
			BG=f"https://daotranslate.net/?s={P}";AZ=L.get(BG);BH=f"https://www.mangaread.org/?s={P}&post_type=wp-manga";Aa=L.get(BH);BI=f"https://mangatx.to/?s={P}&post_type=wp-manga&post_type=wp-manga";Ab=L.get(BI)
			if AZ.status_code==200 and Aa.status_code==200 and Ab.status_code==200:
				BJ=Y(AZ.text,b);BK=Y(Aa.text,b);BL=Y(Ab.text,b);Ac=BJ.find(R,{F:Aw});Ad=BK.find_all(R,{F:A1});Ae=BL.find_all(R,{F:A1})
				if Ac:
					A5=Ac.find_all(R,{F:Ax})
					for i in A5:
						if AY>=20:break
						A6=i.a[W];j=A6.split(Ay)[1].replace('/',B).title();A7=j.replace('-',q);y=f"https://daotranslate.net/{j}-chapter-1/"
						with A.spinner(Av):
							Af,k,Ag=A.columns(3)
							with k:A.write(f"[{A7}]({y})")
							G=i.img[V];A8=y;E,T=S(A8)
							if G:
								try:
									A9=AX(G,scale_factor=4);Af,k,Ag=A.columns(3)
									with k:A.image(A9,use_column_width=None)
								except Q as l:A.error(f"Error loading image: {l}")
							if y:
								Af,k,Ag=A.columns(3)
								with k:H=f"\n                                    {E}\n                                    ";U=h(E,T);A.code(H,language=e);A.button(f,on_click=g,args=[U],key=w())
							A.divider();AY+=1
				if Ad:
					Ah=0
					for C in Ad:
						if Ah>=5:break
						c=C.find(A2,{F:'h5'}).text.strip();m=C.find(t,href=D)[W];Z=C.select(AN)
						if Z:M=Z[0][W]
						else:M=B
						A.write(f"[{c}]({M})");N=C.find(p,src=D)
						if N:
							G=N[V]
							try:d=z(G,scale_factor=4);A.image(d,use_column_width=u)
							except Q as l:pass
						E,T=S(M);H=f"{E}";A.code(H,language=e);A.caption(v);A.divider();Ah+=1
				if Ae:
					Ai=0
					for C in Ae:
						if Ai>=5:break
						c=C.find(A2,{F:'h4'}).text.strip();m=C.find(t,href=D)[W];N=C.find(p,src=D)
						if N:
							G=N[V]
							try:d=z(G,scale_factor=4);A.image(d,use_column_width=u)
							except Q as l:pass
						BM=C.find('span',{F:'chapter'}).text.strip();A.write(f"[{c}]({m})");A.write(f"Latest Chapter: {BM}");E,T=S(m);H=f"{E}";A.code(H,language=e);A.caption(v);A.divider();Ai+=1
AA,AB,AC=A.columns(3)
Bg=A.columns([1,2])
Aj=0
with AA:
	BN=AO.choice(string.ascii_uppercase)
	with A.expander(':loud_sound: Text & Audio '):
		a=L.get(f"https://daotranslate.net/?s={BN}")
		if a.status_code==200:
			n=Y(a.text,b);Ak=n.find(R,{F:Aw})
			if Ak:
				A5=Ak.find_all(R,{F:Ax})
				for i in A5:
					if Aj>=10:break
					A6=i.a[W];j=A6.split(Ay)[1].replace('/',B).title();A7=j.replace('-',q);AD=f"https://daotranslate.net/{j}-chapter-1/";A.write(f"[{A7}]({AD})");G=i.img[V];A8=AD;E,T=S(A8)
					if G:
						try:A9=AX(G,scale_factor=4);A.image(A9,use_column_width=u)
						except:pass
					if AD:H=f"\n                        {E}\n                        ";U=h(E,T);A.code(H,language=e);A.button(f,on_click=g,args=[U],key=w());A.divider();Aj+=1
Al=0
with AB:
	with A.expander(f":chart_with_upwards_trend: Top Rated"):
		a=L.get('https://mangatx.to/')
		if a.status_code==200:
			n=Y(a.text,b);AE=n.find_all(R,{F:A1})
			for C in AE:
				if Al>=10:break
				c=C.find(A2,{F:'h5'}).text.strip();m=C.find(t,href=D)[W];Z=C.select(AN)
				if Z:M=Z[0][W]
				else:M=B
				A.write(f"[{c}]({M})");N=C.find(p,src=D)
				if N:
					G=N[V]
					try:d=z(G,scale_factor=4);A.image(d,use_column_width=u)
					except Q as l:pass
				E,T=S(M);H=f"{E}";A.code(H,language=e);A.caption(v);A.divider();Al+=1
Am=0
with AC:
	with A.expander(f":frame_with_picture: Recently Updated"):
		a=L.get('https://www.mangaread.org/')
		if a.status_code==200:
			n=Y(a.text,b);AE=n.find_all(R,{F:A1})
			for C in AE:
				if Am>=10:break
				c=C.find(A2,{F:'h5'}).text.strip();m=C.find(t,href=D)[W];Z=C.select(AN)
				if Z:M=Z[0][W]
				else:M=B
				A.write(f"[{c}]({M})");N=C.find(p,src=D)
				if N:
					G=N[V]
					try:d=z(G,scale_factor=4);A.image(d,use_column_width=u)
					except Q as l:pass
				BO=C.select('.list-chapter .chapter-item')
				for An in BO:BP=An.find(t,class_='btn-link').text.strip();BQ=An.find('span',class_='post-on').text.strip()
				A.write(f"Chapter: {BP}");A.write(f"Released: {BQ}");E,T=S(M);H=f"{E}";A.code(H,language=e);A.caption(v);A.divider();Am+=1
A.image(BA)
o=A.empty()
U=h(A.text_input(':orange[Code:]',value=B,placeholder='iuuqt://ebhdrrghmbuf.vt/..',key='readfield',help='Enter Manga Code here'),T)
AA,AB,AC=A.columns(3)
with AA:BR=A.button(':green_book: Read',help=f,key='readbutton',use_container_width=J)
with AB:BS=A.text_input(':orange[URL:]',value=B,placeholder='https://asuralightnovel.com/novel/hi..',key='readfield2',help='Enter Novel URL here')
with AC:BT=A.button('Use URL',help=f,key='readbutton2',use_container_width=J)
if BT:
	with A.spinner(Az):B8(BS)
if BR:
	if A_ in U:
		with A.spinner(Az):g(U)
	if A_ not in U.lower():
		with A.spinner(Ar):
			BU=x();A.session_state.image_links=AU(U);A.session_state.current_image_index=0
			if A.session_state.image_links:
				for BV in A.session_state.image_links:A.image(BV,use_column_width=D)
				A.write(f"Total Images: {O(A.session_state.image_links)}");AV(A.session_state.image_links);Ao=U;AF=B.join([A for A in Ao if A.isdigit()]);BW=K(I(AF)+I(+1));BX=K(I(AF));BY=K(Ao.replace(AF,BW));E,T=S(BY);A.caption(AI+BX+AJ+E);H=f"\n                {E}\n                ";A.code(H,language=e);A.caption(v)
A.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=D)
A.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=D)

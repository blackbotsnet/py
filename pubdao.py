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
Ak='series/'
Aj='mdthumb'
Ai='listupd'
Ah='Searching..'
Ag='Restart'
Af='\n\n:orange[Next Chapter:] '
Ae=':green[Chapter Complete:] '
Ad='Loading text & audio..'
Ac='current_image_index'
Ab='image_links'
AD='.list-chapter .chapter-item a.btn-link'
AC='PANEL/'
AB='NOVEL/'
AA='TOP/'
y='h3'
x='page-item-detail manga'
w='Read'
v=chr
p='Copy Code'
o='always'
n='a'
m=' '
l='img'
e='java'
d='html.parser'
Z=len
U='href'
T='div'
S='src'
R=Exception
Q=str
N=False
M=int
F='class'
D=True
B=''
import os,io,base64,hashlib,random as AE,string,tempfile as Am,time,uuid
from io import BytesIO as AF
import re,requests as K
from PIL import Image as V
import numpy as BN,pandas as BO,pickle
from paddleocr import PaddleOCR as An
from gtts import gTTS
from pydub import AudioSegment as Ao
from pydub.effects import speedup
import streamlit as A,streamlit_nested_layout,streamlit.components.v1 as BP,streamlit_scrollable_textbox as Ap,streamlit_extras
from bs4 import BeautifulSoup as a
from selenium import webdriver as Aq
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as Ar
from webdriver_manager.chrome import ChromeDriverManager as As
from webdriver_manager.core.os_manager import ChromeType as At
import webbrowser
from utils import recommendations,read_object
def z():A=Q(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def Au(file_path):
	with open(file_path,'rb')as B:C=B.read();E=base64.b64encode(C).decode();F=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{E}" type="audio/mp3">\n            </audio>\n            ';A.markdown(F,unsafe_allow_html=D)
def A0():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',N);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return Aq.Chrome(service=Service(As(chrome_type=At.CHROMIUM).install()),options=A)
def BQ(url):
	if Ab not in A.session_state:A.session_state.image_links=[]
	if Ac not in A.session_state:A.session_state.current_image_index=0
	try:BI.get(url)
	except:A.stop();pass
	with A.spinner(Ad):
		A.session_state.image_links=AG(url);A.session_state.current_image_index=0
		if A.session_state.image_links:
			for B in A.session_state.image_links:A.image(B,use_column_width=D)
			A.write(f"Total Images: {Z(A.session_state.image_links)}");AH(A.session_state.image_links)
def AG(url):
	B=A0()
	try:B.get(url)
	except Ar as M:
		if B.current_url==url:return[]
		else:A.stop();return[]
	C=[];G=B.find_elements(By.CSS_SELECTOR,l)
	for H in G:
		D=H.get_attribute(S)
		if D and A1(D):C.append(D)
	I=B.find_elements(By.CSS_SELECTOR,'img[id^="image-"]')
	for J in I:
		E=J.get_attribute(S)
		if E and A1(E):C.append(E)
	K=B.find_elements(By.CSS_SELECTOR,'img.wp-manga-chapter-img')
	for L in K:
		F=L.get_attribute(S)
		if F and A1(F):C.append(F)
	B.quit();return C
def AH(image_links):
	L='converted_img.jpg';G=[];M=An(use_angle_cls=D,lang='en');H=[]
	for(Y,E)in enumerate(image_links,start=1):
		if not Av(E):continue
		with A.spinner(' Getting image text '):
			try:O=K.get(E).content;P=io.BytesIO(O);S=V.open(P);T=S.convert('RGB');T.save(L,'JPEG')
			except R as I:continue
			try:
				U=M.ocr(L,det=N,cls=D);W=U[0][0][0];C=Aw(Q(W));H.append(C);J=m.join(H);A.write('All Text:',J)
				if J:
					F=os.path.join('audio',os.path.splitext(os.path.basename(E))[0]+'.mp3')
					if not os.path.exists(F):X=gTTS(text=C,lang='en',slow=N);X.save(F)
					G.append(F)
					if AI:u.markdown(f":blue[Streaming: ]:green[*{C}*]")
				else:u.markdown(f":blue[Dao: ]:orange[No Text]")
			except R as I:A.write(f"Error processing text: {I}");C=B
	return G
def Av(image_url):
	A=['.png','.jpg','.jpeg','.webp']
	for format in A:
		if image_url.lower().endswith(format):return D
	return N
def A1(link):
	A=['.png','.jpg','.jpeg','.webp']
	for B in A:
		if link.lower().endswith(B):return D
	return N
def Aw(text):
	C=text
	try:
		if not isinstance(C,Q):raise ValueError('Input must be a string')
		D='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';E=re.findall(D,C);F=m.join(E);C=F.lower()
	except R as G:A.write(f"Error filtering English words: {G}");C=B
	return C
def q(url):
	b='file.mp3';O='\n';E=url;H=A0()
	try:H.get(E)
	except:pass
	if not E:u.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
	else:
		try:
			P=K.get(E)
			if P.status_code==200:
				c=a(P.text,d);I=c.find(T,{F:'epcontent entry-content'})
				if I:
					t=B;e=Z(I.findAll('p'));G=I.findAll('p');J=1;v=e//J;f=[G[A:A+J]for A in range(0,Z(G),J)];C=B
					for g in G:C+=g.text+O
					C=C.replace('<p>',B);C=C.replace('"',B);A.markdown('<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>',unsafe_allow_html=D)
					with A.expander(w):from annotated_text import annotated_text as h;G=C.split(O);i=[(A,B,'#fea')for A in G];h(*i);A.caption(f"{Z(C)} characters in this chapter.");S=E;L=B.join([A for A in S if A.isdigit()]);U=Q(M(L)+M(+1));j=Q(M(L));k=Q(S.replace(L,U));V,l=W(k);A.caption(Ae+j+Af+U);A.caption(V);E=r(V,l);A.button('Continue',on_click=q,args=[E],key=z())
					with Am.NamedTemporaryFile(suffix='.mp3',delete=N)as X:C=C.replace('"',B);m=gTTS(text=C,lang='en',slow=N);m.save(X.name);n=Ao.from_mp3(X.name);o=speedup(n,1.2,150);o.export(b,format='mp3');Au(b)
					for p in f:
						s=B
						for Y in p:s+=Y.text+O
						if AI:u.markdown(f":blue[Dao: ]:green[*{Y.text}*]");time.sleep(5)
					H.quit()
				else:A.write(B)
			else:A.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
		except R as x:pass
	H.quit()
def W(text):
	C=text;D={}
	for E in range(26):D[v(65+E)]=v((E+1)%26+65);D[v(97+E)]=v((E+1)%26+97)
	A=B.join(D.get(A,A)for A in C)
	if'nightcomic.com'in C:A=AA+A
	if'daotranslate'in C:A=AB+A
	if'manhuaaz.com'in C:A=AC+A
	return A,D
def r(obfuscated_text,mapping):
	A=obfuscated_text
	if A.startswith(AA):A=A[Z(AA):]
	if A.startswith(AB):A=A[Z(AB):]
	if A.startswith(AC):A=A[Z(AC):]
	C={B:A for(A,B)in mapping.items()};D=B.join(C.get(A,A)for A in A);return D
BR=[]
s=B
Ax=V.open('static/-.ico')
BS=AE.randint(1,99999)
A.set_page_config(page_title='Manga Dōjutsu',page_icon=Ax,layout='centered',initial_sidebar_state='expanded')
A.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}\n        [data-testid='stSidebarNav'] > ul {color: red;}\n        .language-java {color: black;}\n        .css-nps9tx, .e1m3hlzs0, .css-1p0bytv, .e1m3hlzs1 {\n        visibility: collapse;\n        height: 0px;\n        }\n\t .stException {\n\t    display: none;\n\t}\n    </style>\n",unsafe_allow_html=D)
Ay=V.open('static/dojutsu.png')
Az=V.open('static/4.png')
A.sidebar.write('BlackDao: Manga Dōjutsu')
if Ab not in A.session_state:A.session_state.image_links=[]
if Ac not in A.session_state:A.session_state.current_image_index=0
BT=None
with A.sidebar:
	if'value'not in A.session_state:A.session_state.value=B
	def A_():A.session_state.value=Ag
	A.image(Az);A.caption('Manga Text or Image To Speach');AI=A.checkbox('Stream Story (Experimental)',value=N,disabled=N)
	with open('titles.txt','r')as B0:B1=B0.readlines()
	B2=B1;A.write(':orange[Popular Titles]');Ap.scrollableTextbox(B2,height=300,border=None);A.divider();A.header('Google Play Store');A.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');A.header('Official PC Version');A.caption('Download from: https://blackbots.gumroad.com/l/manga');A.caption('Join Our Discord: https://discord.gg/HcVPaSpF');A.divider()
	with A.expander('Help'):A.caption('How to use BlackDao: Manga Dōjutsu');A.caption('- `Copy` a Code');A.caption('- `Paste` Code onto `Manga Code` field');A.caption('- `Press Read`')
	A.button(Ag,on_click=A_,key='keyy')
def AJ(img_url,scale_factor):A=scale_factor;C=K.get(img_url);B=V.open(AF(C.content));D,E=B.size;F=M(D*A);G=M(E*A);H=B.resize((F,G),V.LANCZOS);return H
def t(img_url,scale_factor):B=scale_factor;D=K.get(img_url);C=V.open(AF(D.content));E,F=C.size;G=M(E*B);H=M(F*B);I=C.resize((G,H),V.LANCZOS);A=io.BytesIO();I.save(A,format='PNG');A=A.getvalue();return A
L=A.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
AK=0
if L:
	L=L.replace('"',B);L=L.replace('-',m);L=L.replace(':',B)
	with A.spinner(Ah):
		with A.expander(':mag: Search'):
			B3=f"https://daotranslate.net/?s={L}";AL=K.get(B3);B4=f"https://www.mangaread.org/?s={L}&post_type=wp-manga";AM=K.get(B4);B5=f"https://mangatx.to/?s={L}&post_type=wp-manga&post_type=wp-manga";AN=K.get(B5)
			if AL.status_code==200 and AM.status_code==200 and AN.status_code==200:
				B6=a(AL.text,d);B7=a(AM.text,d);B8=a(AN.text,d);AO=B6.find(T,{F:Ai});AP=B7.find_all(T,{F:x});AQ=B8.find_all(T,{F:x})
				if AO:
					A2=AO.find_all(T,{F:Aj})
					for f in A2:
						if AK>=20:break
						A3=f.a[U];g=A3.split(Ak)[1].replace('/',B).title();A4=g.replace('-',m);s=f"https://daotranslate.net/{g}-chapter-1/"
						with A.spinner(Ah):
							AR,h,AS=A.columns(3)
							with h:A.write(f"[{A4}]({s})")
							G=f.img[S];A5=s;E,O=W(A5)
							if G:
								try:
									A6=AJ(G,scale_factor=4);AR,h,AS=A.columns(3)
									with h:A.image(A6,use_column_width=None)
								except R as i:A.error(f"Error loading image: {i}")
							if s:
								AR,h,AS=A.columns(3)
								with h:H=f"\n                                    {E}\n                                    ";P=r(E,O);A.code(H,language=e);A.button(w,on_click=q,args=[P],key=z())
							A.divider();AK+=1
				if AP:
					AT=0
					for C in AP:
						if AT>=5:break
						b=C.find(y,{F:'h5'}).text.strip();j=C.find(n,href=D)[U];X=C.select(AD)
						if X:I=X[0][U]
						else:I=B
						A.write(f"[{b}]({I})");J=C.find(l,src=D)
						if J:
							G=J[S]
							try:c=t(G,scale_factor=4);A.image(c,use_column_width=o)
							except R as i:pass
						E,O=W(I);H=f"{E}";A.code(H,language=e);A.caption(p);A.divider();AT+=1
				if AQ:
					AU=0
					for C in AQ:
						if AU>=5:break
						b=C.find(y,{F:'h4'}).text.strip();j=C.find(n,href=D)[U];J=C.find(l,src=D)
						if J:
							G=J[S]
							try:c=t(G,scale_factor=4);A.image(c,use_column_width=o)
							except R as i:pass
						B9=C.find('span',{F:'chapter'}).text.strip();A.write(f"[{b}]({j})");A.write(f"Latest Chapter: {B9}");E,O=W(j);H=f"{E}";A.code(H,language=e);A.caption(p);A.divider();AU+=1
BA,BB,BC=A.columns(3)
BU=A.columns([1,2])
AV=0
with BA:
	BD=AE.choice(string.ascii_uppercase)
	with A.expander(':loud_sound: Text & Audio '):
		Y=K.get(f"https://daotranslate.net/?s={BD}")
		if Y.status_code==200:
			k=a(Y.text,d);AW=k.find(T,{F:Ai})
			if AW:
				A2=AW.find_all(T,{F:Aj})
				for f in A2:
					if AV>=10:break
					A3=f.a[U];g=A3.split(Ak)[1].replace('/',B).title();A4=g.replace('-',m);A7=f"https://daotranslate.net/{g}-chapter-1/";A.write(f"[{A4}]({A7})");G=f.img[S];A5=A7;E,O=W(A5)
					if G:
						try:A6=AJ(G,scale_factor=4);A.image(A6,use_column_width=o)
						except:pass
					if A7:H=f"\n                        {E}\n                        ";P=r(E,O);A.code(H,language=e);A.button(w,on_click=q,args=[P],key=z());A.divider();AV+=1
AX=0
with BB:
	with A.expander(f":chart_with_upwards_trend: Top Rated"):
		Y=K.get('https://mangatx.to/')
		if Y.status_code==200:
			k=a(Y.text,d);A8=k.find_all(T,{F:x})
			for C in A8:
				if AX>=10:break
				b=C.find(y,{F:'h5'}).text.strip();j=C.find(n,href=D)[U];X=C.select(AD)
				if X:I=X[0][U]
				else:I=B
				A.write(f"[{b}]({I})");J=C.find(l,src=D)
				if J:
					G=J[S]
					try:c=t(G,scale_factor=4);A.image(c,use_column_width=o)
					except R as i:pass
				E,O=W(I);H=f"{E}";A.code(H,language=e);A.caption(p);A.divider();AX+=1
AY=0
with BC:
	with A.expander(f":frame_with_picture: Recently Updated"):
		Y=K.get('https://www.mangaread.org/')
		if Y.status_code==200:
			k=a(Y.text,d);A8=k.find_all(T,{F:x})
			for C in A8:
				if AY>=10:break
				b=C.find(y,{F:'h5'}).text.strip();j=C.find(n,href=D)[U];X=C.select(AD)
				if X:I=X[0][U]
				else:I=B
				A.write(f"[{b}]({I})");J=C.find(l,src=D)
				if J:
					G=J[S]
					try:c=t(G,scale_factor=4);A.image(c,use_column_width=o)
					except R as i:pass
				BE=C.select('.list-chapter .chapter-item')
				for AZ in BE:BF=AZ.find(n,class_='btn-link').text.strip();BG=AZ.find('span',class_='post-on').text.strip()
				A.write(f"Chapter: {BF}");A.write(f"Released: {BG}");E,O=W(I);H=f"{E}";A.code(H,language=e);A.caption(p);A.divider();AY+=1
A.image(Ay)
u=A.empty()
P=r(A.text_input(':orange[Manga Code:]',value=B,placeholder='iuuqt://ebhdrrghmbuf.vt/..',key='readfield',help='Enter Manga Code here'),O)
BH=A.button(':green_book: Read',help=w,key='readbutton',use_container_width=N)
if BH:
	if Al in P:
		with A.spinner('Loading, please be patient..'):q(P)
	if Al not in P.lower():
		with A.spinner(Ad):
			BI=A0();A.session_state.image_links=AG(P);A.session_state.current_image_index=0
			if A.session_state.image_links:
				for BJ in A.session_state.image_links:A.image(BJ,use_column_width=D)
				A.write(f"Total Images: {Z(A.session_state.image_links)}");AH(A.session_state.image_links);Aa=P;A9=B.join([A for A in Aa if A.isdigit()]);BK=Q(M(A9)+M(+1));BL=Q(M(A9));BM=Q(Aa.replace(A9,BK));E,O=W(BM);A.caption(Ae+BL+Af+E);H=f"\n                {E}\n                ";A.code(H,language=e);A.caption(p)
A.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=D)
A.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=D)

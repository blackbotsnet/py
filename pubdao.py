# ┌──────────────────────────────────┐
# │ BlackDao: Manga Dōjutsu v3.12.21 │
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
Ai='daotrans'
Ah='chapter'
Ag='series/'
Af='mdthumb'
Ae='listupd'
Ad='Searching..'
Ac='Restart'
Ab='nightcomic.com'
Aa='\n\n:orange[Next Chapter:] '
AZ=':green[Chapter Complete:] '
AY='Loading text & audio..'
AX='current_image_index'
AW='image_links'
AV=Exception
AA='always'
A9='data-src'
A8='PANEL/'
A7='NOVEL/'
A6='TOP/'
A5=range
v='Copy Code'
u='https://manhuaaz.com/manga/'
t='Read'
s=' '
r='src'
q='img'
p=chr
l='href'
k='class'
d='java'
c='div'
b='html.parser'
V=False
U=int
T=str
O=len
J=True
B=''
import os,io,base64,hashlib,random as AB,string,tempfile as Aj,time,uuid
from io import BytesIO
import re,requests as P
from PIL import Image as e
import numpy as BI,pandas as BJ,pickle,easyocr as Ak
from easyocr import Reader
from gtts import gTTS
from pydub import AudioSegment as Al
from pydub.effects import speedup
import streamlit as A,streamlit_nested_layout,streamlit.components.v1 as BK,streamlit_extras
from bs4 import BeautifulSoup as Z
from selenium import webdriver as Am
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as AC
from webdriver_manager.chrome import ChromeDriverManager as An
from webdriver_manager.core.os_manager import ChromeType as Ao
import webbrowser
from utils import recommendations,read_object
def w():A=T(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def Ap(file_path):
	with open(file_path,'rb')as B:C=B.read();D=base64.b64encode(C).decode();E=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{D}" type="audio/mp3">\n            </audio>\n            ';A.markdown(E,unsafe_allow_html=J)
def AD():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',V);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return Am.Chrome(service=Service(An(chrome_type=Ao.CHROMIUM).install()),options=A)
def BL(url):
	if AW not in A.session_state:A.session_state.image_links=[]
	if AX not in A.session_state:A.session_state.current_image_index=0
	try:N.get(url)
	except:pass
	with A.spinner(AY):
		A.session_state.image_links=AE(url);A.session_state.current_image_index=0
		if A.session_state.image_links:
			for B in A.session_state.image_links:A.image(B,use_column_width=J)
			A.write(f"Total Images: {O(A.session_state.image_links)}");AF(A.session_state.image_links)
def AE(url):
	try:N.get(url)
	except AC as D:
		if N.current_url==url:return[]
		else:A.write(f"Error loading URL: {D}");return[]
	C=[];E=N.find_elements(By.CSS_SELECTOR,q)
	for F in E:
		B=F.get_attribute(r)
		if B and AG(B):C.append(B)
	N.quit();return C
def Aq(url):
	try:N.get(url)
	except AC as D:
		if N.current_url==url:return[]
		else:A.write(f"Error loading URL: {D}");return[]
	C=[];E=N.find_elements(By.CSS_SELECTOR,'img[id^="image-"]')
	for F in E:
		B=F.get_attribute(r)
		if B and AG(B):C.append(B)
	N.quit();return C
def AF(image_links):
	E=[];F=As()
	for(K,B)in enumerate(image_links,start=1):
		if not Ar(B):continue
		with A.spinner(' Getting image text '):G=P.get(B).content;H=F.readtext(G);I=[A[1].strip()for A in H]
		C=At(I)
		if C:
			D=os.path.join('audio',os.path.splitext(os.path.basename(B))[0]+'.mp3')
			if not os.path.exists(D):J=gTTS(text=C,lang='en',slow=V);J.save(D)
			E.append(D)
			if Ay:A3.markdown(f":blue[RAWR: ]:green[*{C}*]")
		else:A3.markdown(f":blue[Dao: ]:orange[No Text]")
	return E
def Ar(image_url):
	A=['.png','.jpg','.jpeg']
	for format in A:
		if image_url.lower().endswith(format):return J
	return V
def AG(link):
	A=['.png','.jpg','.jpeg']
	for B in A:
		if link.lower().endswith(B):return J
	return V
def As():return Ak.Reader(['en'],model_storage_directory='.')
def At(text):
	C=text
	try:
		if not isinstance(C,T):raise ValueError('Input must be a string')
		D='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';E=re.findall(D,C);F=s.join(E);C=F.lower()
	except AV as G:A.write(f"Error filtering English words: {G}");C=B
	return C
def m(url):
	S='file.mp3';K='\n';D=url;F=AD()
	try:F.get(D)
	except:pass
	if not D:A3.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
	else:
		try:
			L=P.get(D)
			if L.status_code==200:
				X=Z(L.text,b);G=X.find(c,{k:'epcontent entry-content'})
				if G:
					u=B;Y=O(G.findAll('p'));E=G.findAll('p');H=1;v=Y//H;d=[E[A:A+H]for A in A5(0,O(E),H)];C=B
					for e in E:C+=e.text+K
					C=C.replace('<p>',B);C=C.replace('"',B);A.markdown('<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>',unsafe_allow_html=J)
					with A.expander(t):from annotated_text import annotated_text as f;E=C.split(K);g=[(A,B,'#fea')for A in E];f(*g);A.caption(f"{O(C)} characters in this chapter.");M=D;I=B.join([A for A in M if A.isdigit()]);N=T(U(I)+U(+1));h=T(U(I));i=T(M.replace(I,N));Q,j=W(i);A.caption(AZ+h+Aa+N);A.caption(Q);D=a(Q,j);A.button('Continue',on_click=m,args=[D],key=w())
					with Aj.NamedTemporaryFile(suffix='.mp3',delete=V)as R:C=C.replace('"',B);l=gTTS(text=C,lang='en',slow=V);l.save(R.name);n=Al.from_mp3(R.name);o=speedup(n,1.2,150);o.export(S,format='mp3');Ap(S)
					for p in d:
						q=B
						for r in p:q+=r.text+K
					F.quit()
				else:A.write(B)
			else:A.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
		except AV as s:A.write(f":blue[Dao: ]:green[*Error occurred: {s}*]")
	F.quit()
def W(text):
	C=text;D={}
	for E in A5(26):D[p(65+E)]=p((E+1)%26+65);D[p(97+E)]=p((E+1)%26+97)
	A=B.join(D.get(A,A)for A in C)
	if Ab in C:A=A6+A
	if'daotranslate'in C:A=A7+A
	if'manhuaaz.com'in C:A=A8+A
	return A,D
def a(obfuscated_text,mapping):
	A=obfuscated_text
	if A.startswith(A6):A=A[O(A6):]
	if A.startswith(A7):A=A[O(A7):]
	if A.startswith(A8):A=A[O(A8):]
	C={B:A for(A,B)in mapping.items()};D=B.join(C.get(A,A)for A in A);return D
BM=[]
n=B
Au=e.open('static/-.ico')
BN=AB.randint(1,99999)
A.set_page_config(page_title='Manga Dōjutsu',page_icon=Au,layout='centered',initial_sidebar_state='expanded')
A.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}\n        [data-testid='stSidebarNav'] > ul {color: red;}\n        .language-java {color: black;}\n    </style>\n",unsafe_allow_html=J)
Av=e.open('static/dojutsu.png')
Aw=e.open('static/4.png')
A.sidebar.write('BlackDao: Manga Dōjutsu')
if AW not in A.session_state:A.session_state.image_links=[]
if AX not in A.session_state:A.session_state.current_image_index=0
BO=None
with A.sidebar:
	if'value'not in A.session_state:A.session_state.value=B
	def Ax():A.session_state.value=Ac
	A.image(Aw);A.caption('Manga Text or Image To Speach');Ay=A.checkbox('Stream Story (Disabled)',value=V,disabled=J)
	with open('titles.txt','r')as Az:AH=Az.readlines()
	AI=O(AH);A_=(AI-1)//10+1;AJ=A.slider('Popular Titles',1,A_,1);B0=(AJ-1)*10;B1=min(AJ*10,AI)
	for B2 in A5(B0,B1):A.write(AH[B2])
	A.divider();A.header('Google Play Store');A.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');A.header('Official PC Version');A.caption('Download from: https://blackbots.gumroad.com/l/manga');A.caption('Join Our Discord: https://discord.gg/HcVPaSpF');A.divider()
	with A.expander('Help'):A.caption('How to use BlackDao: Manga Dōjutsu');A.caption('- `Copy` a Code');A.caption('- `Paste` Code onto `Manga Code` field');A.caption('- `Press Read`')
	A.button(Ac,on_click=Ax,key='keyy')
def f(img_url,scale_factor):A=scale_factor;C=P.get(img_url);B=e.open(BytesIO(C.content));D,E=B.size;F=U(D*A);G=U(E*A);H=B.resize((F,G),e.LANCZOS);return H
K=A.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
AK=0
AL=0
if K:
	K=K.replace('"',B);K=K.replace('-',s);K=K.replace(':',B)
	with A.spinner(Ad):
		with A.expander(':mag: Search'):
			B3=f"https://daotranslate.net/?s={K}";AM=P.get(B3);B4=f"https://manhuaaz.com/?s={K}&post_type=wp-manga&op=&author=&artist=&release=&adult=";AN=P.get(B4)
			if AM.status_code==200 and AN.status_code==200:
				B5=Z(AM.text,b);B6=Z(AN.text,b);AO=B5.find(c,{k:Ae});AP=B6.find_all('a',href=lambda href:href and href.startswith(u))
				if AO and AP:
					x=AO.find_all(c,{k:Af});y=iter(AP)
					for X in x:
						if AK>=10:break
						z=X.a[l];g=z.split(Ag)[1].replace('/',B).title();A0=g.replace('-',s);n=f"https://daotranslate.net/{g}-chapter-1/"
						with A.spinner(Ad):
							h,F,i=A.columns(3)
							with F:A.write(f"[{A0}]({n})")
							G=X.img[r];L=n;C,I=W(L)
							if G:
								try:
									M=f(G,scale_factor=4);h,F,i=A.columns(3)
									with F:A.image(M,use_column_width=None)
								except:pass
							if n:
								h,F,i=A.columns(3)
								with F:H=f"\n                                    {C}\n                                    ";D=a(C,I);A.code(H,language=d);A.button(t,on_click=m,args=[D],key=w())
							A.divider();AK+=1
							try:
								Q=next(y);E=Q.get(l)
								if Ah not in E:Y=f"{E}chapter-1/"
								else:Y=E
								A1=E.split(u)[1];R=Q.find(q);L=Y;C,I=W(L)
								if R:
									if AL>=10:break
									h,F,i=A.columns(3)
									with F:A.write(f"[{A1}]({Y})")
									G=R.get(A9)
									try:
										M=f(G,scale_factor=4);h,F,i=A.columns(3)
										with F:A.image(M,use_column_width=None)
									except:pass
									h,F,i=A.columns(3)
									with F:H=f"\n                                    \t{C}\n                                    \t";A.code(H,language=d);A.caption(v);A.divider();AL+=1
							except StopIteration:break
B7,B8,B9=A.columns(3)
BP=A.columns([1,2])
AQ=0
with B7:
	BA=AB.choice(string.ascii_uppercase)
	with A.expander(':books: Novels'):
		S=P.get(f"https://daotranslate.net/?s={BA}")
		if S.status_code==200:
			j=Z(S.text,b);AR=j.find(c,{k:Ae})
			if AR:
				x=AR.find_all(c,{k:Af})
				for X in x:
					if AQ>=10:break
					z=X.a[l];g=z.split(Ag)[1].replace('/',B).title();A0=g.replace('-',s);A2=f"https://daotranslate.net/{g}-chapter-1/";A.write(f"[{A0}]({A2})");G=X.img[r];L=A2;C,I=W(L)
					if G:
						try:M=f(G,scale_factor=4);A.image(M,use_column_width=AA)
						except:pass
					if A2:H=f"\n                        {C}\n                        ";D=a(C,I);A.code(H,language=d);A.button(t,on_click=m,args=[D],key=w())
					A.divider();AQ+=1
AS=0
with B8:
	with A.expander(f":chart_with_upwards_trend: Top Rated"):
		S=P.get('https://nightcomic.com/')
		if S.status_code==200:
			j=Z(S.text,b);BB=j.find_all(c,class_='page-item-detail manga')
			for o in BB:
				Q=o.find('a',class_='btn-link');R=o.find(q);X=o.find('h3',class_='h5').text.strip();BC=o.find('span',class_='score').text.strip()
				if Q and R:
					if AS>=10:break
					E=Q.get(l);G=R.get(A9);L=E;C,I=W(L);D=a(C,I);A.write(f"[{X}]({E}) - Rating: {BC}")
					try:M=f(G,scale_factor=4);A.image(M,use_column_width=AA)
					except:pass
					H=f"\n                    {C}\n                    ";A.code(H,language=d);A.caption(v);A.divider();AS+=1
AT=0
with B9:
	with A.expander(f":frame_with_picture: Panels"):
		S=P.get('https://manhuaaz.com/')
		if S.status_code==200:
			j=Z(S.text,b);y=j.find_all('a',href=lambda href:href and href.startswith(u))
			for Q in y:
				E=Q.get(l)
				if Ah not in E:Y=f"{E}chapter-1/"
				else:Y=E
				A1=E.split(u)[1];R=Q.find(q);L=Y;C,I=W(L)
				if R:
					if AT>=10:break
					A.write(f"[{A1}]({Y})");G=R.get(A9)
					try:M=f(G,scale_factor=4);A.image(M,use_column_width=AA)
					except:pass
					D=a(C,I);H=f"\n                    {C}\n                    ";A.code(H,language=d);A.caption(v);A.divider();AT+=1
A.image(Av)
A3=A.empty()
D=a(A.text_input(':orange[Manga Code:]',value=B,placeholder='iuuqt://ebhdrrghmbuf.vt/..',key='readfield',help='Enter Manga Code here'),I)
BD=A.button(':green_book: Read',help=t,key='readbutton',use_container_width=V)
if BD:
	if Ai in D:
		with A.spinner('Loading, please be patient..'):m(D)
	if Ai not in D.lower():
		with A.spinner(AY):
			N=AD()
			if Ab in D.lower():A.session_state.image_links=Aq(D)
			else:A.session_state.image_links=AE(D)
			A.session_state.current_image_index=0
			if A.session_state.image_links:
				for BE in A.session_state.image_links:A.image(BE,use_column_width=J)
				A.write(f"Total Images: {O(A.session_state.image_links)}");AF(A.session_state.image_links);AU=D;A4=B.join([A for A in AU if A.isdigit()]);BF=T(U(A4)+U(+1));BG=T(U(A4));BH=T(AU.replace(A4,BF));C,I=W(BH);A.caption(AZ+BG+Aa+C);H=f"\n                {C}\n                ";A.code(H,language=d);A.caption(v)
A.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=J)
A.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=J)

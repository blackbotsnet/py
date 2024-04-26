# ┌──────────────────────────────────┐
# │ BlackDao: Manga Dōjutsu v2.12.21 │
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
AY='daotrans'
AX='data-src'
AW='series/'
AV='mdthumb'
AU='https://manhuaaz.com/manga/'
AT='listupd'
AS='Searching..'
AR='Restart'
AQ='nightcomic.com'
AP='\n\n:orange[Next Chapter:] '
AO=':green[Chapter Complete:] '
AN='Loading text & audio..'
AM='current_image_index'
AL='image_links'
AK=Exception
AJ=enumerate
A0='Copy Code'
z=None
y='PANEL/'
x='NOVEL/'
w='TOP/'
v='"'
u='en'
t='img'
s=range
h='always'
g='href'
f='Read'
e=' '
d='src'
c=chr
X='java'
W='class'
V='html.parser'
Q='div'
P=int
I=False
H=str
G=len
F=True
B=''
import os,io,asyncio,httpx,aiohttp as J,base64,hashlib,random as A1,string,tempfile as AZ,time,uuid
from io import BytesIO
import re,requests as Y
from PIL import Image as i
import numpy as BB,pandas as BC,pickle,easyocr as Aa
from easyocr import Reader
from gtts import gTTS
from pydub import AudioSegment as Ab
from pydub.effects import speedup
import streamlit as A,streamlit_nested_layout,streamlit.components.v1 as BD,streamlit_extras
from bs4 import BeautifulSoup as R
from selenium import webdriver as Ac
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager as Ad
from webdriver_manager.core.os_manager import ChromeType as Ae
import webbrowser
def j():A=H(uuid.uuid4());B=hashlib.sha256(A.encode()).hexdigest();return B
def Af(file_path):
	with open(file_path,'rb')as B:C=B.read();D=base64.b64encode(C).decode();E=f'\n            <audio controls autoplay="true">\n            <source src="data:audio/mp3;base64,{D}" type="audio/mp3">\n            </audio>\n            ';A.markdown(E,unsafe_allow_html=F)
def k():A=Options();A.add_argument('--disable-gpu');A.add_argument('--headless');A.add_argument('--disable-blink-features=AutomationControlled');A.add_experimental_option('useAutomationExtension',I);A.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36');A.add_argument('--dns-prefetch-disable');A.add_argument('--no-sandbox');A.add_argument('--lang=en-US');A.add_argument('--disable-setuid-sandbox');A.add_argument('--ignore-certificate-errors');return Ac.Chrome(service=Service(Ad(chrome_type=Ae.CHROMIUM).install()),options=A)
async def BE(url):
	if AL not in A.session_state:A.session_state.image_links=[]
	if AM not in A.session_state:A.session_state.current_image_index=0
	try:
		async with J.ClientSession()as B:
			async with B.get(url)as C:E=await C.text()
	except:pass
	with A.spinner(AN):
		A.session_state.image_links=await A2(url);A.session_state.current_image_index=0
		if A.session_state.image_links:
			for D in A.session_state.image_links:A.image(D,use_column_width=F)
			A.write(f"Total Images: {G(A.session_state.image_links)}");await A3(A.session_state.image_links)
async def A2(url):
	try:
		async with J.ClientSession()as D:
			async with D.get(url)as E:I=await E.text()
	except J.ClientConnectionError as F:A.write(f"Error loading URL: {F}");return[]
	C=[];G=AH.find_elements(By.CSS_SELECTOR,t)
	for H in G:
		B=H.get_attribute(d)
		if B and A4(B):C.append(B)
	AH.quit();return C
async def Ag(url):
	C=k()
	try:
		async with J.ClientSession()as E:
			async with E.get(url)as F:K=await F.text()
	except J.ClientConnectionError as G:A.write(f"Error loading URL: {G}");return[]
	D=[];H=C.find_elements(By.CSS_SELECTOR,'img[id^="image-"]')
	for I in H:
		B=I.get_attribute(d)
		if B and A4(B):D.append(B)
	C.quit();return D
async def A3(image_links):
	E=[];F=Ai()
	for(O,B)in AJ(image_links,start=1):
		if not Ah(B):continue
		with A.spinner(' Getting image text '):
			async with J.ClientSession()as G:
				async with G.get(B)as H:K=await H.read()
			L=F.readtext(K);M=[A[1].strip()for A in L]
		C=Aj(M)
		if C:
			D=os.path.join('audio',os.path.splitext(os.path.basename(B))[0]+'.mp3')
			if not os.path.exists(D):N=gTTS(text=C,lang=u,slow=I);N.save(D)
			E.append(D)
			if Ao:q.markdown(f":blue[RAWR: ]:green[*{C}*]")
		else:q.markdown(f":blue[Dao: ]:orange[No Text]")
	return E
def Ah(image_url):
	A=['.png','.jpg','.jpeg']
	for format in A:
		if image_url.lower().endswith(format):return F
	return I
def A4(link):
	A=['.png','.jpg','.jpeg']
	for B in A:
		if link.lower().endswith(B):return F
	return I
def Ai():return Aa.Reader([u],model_storage_directory='.')
def Aj(text):
	C=text
	try:
		if not isinstance(C,H):raise ValueError('Input must be a string')
		D='\\b[a-zA-Z]+(?:\\\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\\\'":;\\[\\]()*&^%$#@`~\\\\/]|\\.\\.\\.)?\\b';E=re.findall(D,C);F=e.join(E);C=F.lower()
	except AK as G:A.write(f"Error filtering English words: {G}");C=B
	return C
def Z(url):
	c='file.mp3';O='\n';D=url;J=k()
	try:J.get(D)
	except:pass
	if not D:q.markdown(f":blue[Dao: ]:green[*Enter a valid URL before running.*]")
	else:
		try:
			T=Y.get(D)
			if T.status_code==200:
				d=R(T.text,V);L=d.find(Q,{W:'epcontent entry-content'})
				if L:
					A0=B;e=G(L.findAll('p'));E=L.findAll('p');M=1;A1=e//M;g=[E[A:A+M]for A in s(0,G(E),M)];C=B
					for h in E:C+=h.text+O
					C=C.replace('<p>',B);C=C.replace(v,B);A.markdown('<style>\n                          .stMarkdown{color: black;}\n                          .st-c8:hover{color:orange;}\n                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}\n                          </style>',unsafe_allow_html=F)
					with A.expander(f):from annotated_text import annotated_text as i;E=C.split(O);l=[(A,B,'#fea')for A in E];i(*l);A.caption(f"{G(C)} characters in this chapter.");U=D;N=B.join([A for A in U if A.isdigit()]);X=H(P(N)+P(+1));m=H(P(N));n=H(U.replace(N,X));a,o=K(n);A.caption(AO+m+AP+X);A.caption(a);D=S(a,o);A.button('Continue',on_click=Z,args=[D],key=j())
					with AZ.NamedTemporaryFile(suffix='.mp3',delete=I)as b:C=C.replace(v,B);p=gTTS(text=C,lang=u,slow=I);p.save(b.name);r=Ab.from_mp3(b.name);t=speedup(r,1.2,150);t.export(c,format='mp3');Af(c)
					for w in g:
						x=B
						for y in w:x+=y.text+O
					J.quit()
				else:A.write(B)
			else:A.write(f":blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]")
		except AK as z:A.write(f":blue[Dao: ]:green[*Error occurred: {z}*]")
	J.quit()
def K(text):
	C=text;D={}
	for E in s(26):D[c(65+E)]=c((E+1)%26+65);D[c(97+E)]=c((E+1)%26+97)
	A=B.join(D.get(A,A)for A in C)
	if AQ in C:A=w+A
	if'daotranslate'in C:A=x+A
	if'manhuaaz.com'in C:A=y+A
	return A,D
def S(obfuscated_text,mapping):
	A=obfuscated_text
	if A.startswith(w):A=A[G(w):]
	if A.startswith(x):A=A[G(x):]
	if A.startswith(y):A=A[G(y):]
	C={B:A for(A,B)in mapping.items()};D=B.join(C.get(A,A)for A in A);return D
BF=[]
a=B
Ak=i.open('static/-.ico')
BG=A1.randint(1,99999)
A.set_page_config(page_title='Manga Dōjutsu',page_icon=Ak,layout='centered',initial_sidebar_state='expanded')
A.markdown("\n    <style>\n        <br><hr><center>\n        .reportview-container {background: black;}\n        .sidebar .siderbar-content {background: black;}\n        .st-ck:hover {\n        color: #gold;\n        }\n        color: lime;\n        cursor: pointer;\n        }\n        img {\n        width:75%;\n        }\n        width:578px;\n        vertical-align: middle;\n        horizontal-align: middle;\n        max-width: 300px;\n        margin: auto;\n        }\n        .css-yhwc6k{\n        text-align: center;\n        }\n        #audio{autoplay:true;}\n        #MainMenu{visibility: hidden;}\n        footer{visibility: hidden;}\n        .css-14xtw13 e8zbici0{visibility: hidden;}\n        .css-m70y {display:none}\n        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}\n        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}\n        .styles_terminalButton__JBj5T{visibility: hidden;}\n        .styles_terminalButton__JBj5T{display:none}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}\n        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}\n        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}\n        [data-testid='stSidebarNav'] > ul {color: red;}\n        .language-java {color: black;}\n    </style>\n",unsafe_allow_html=F)
Al=i.open('static/dojutsu.png')
Am=i.open('static/4.png')
A.sidebar.write('BlackDao: Manga Dōjutsu')
if AL not in A.session_state:A.session_state.image_links=[]
if AM not in A.session_state:A.session_state.current_image_index=0
BH=z
with A.sidebar:
	if'value'not in A.session_state:A.session_state.value=B
	def An():A.session_state.value=AR
	A.image(Am);A.caption('Manga Text or Image To Speach');Ao=A.checkbox('Stream Story (Disabled)',value=I,disabled=F)
	with open('titles.txt','r')as Ap:A5=Ap.readlines()
	A6=G(A5);Aq=(A6-1)//10+1;A7=A.slider('Popular Titles',1,Aq,1);Ar=(A7-1)*10;As=min(A7*10,A6)
	for At in s(Ar,As):A.write(A5[At])
	A.divider();A.header('Google Play Store');A.caption('Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao');A.header('Official PC Version');A.caption('Download from: https://blackbots.gumroad.com/l/manga');A.caption('Join Our Discord: https://discord.gg/HcVPaSpF');A.divider()
	with A.expander('Help'):A.caption('How to use BlackDao: Manga Dōjutsu');A.caption('- `Copy` a Code');A.caption('- `Paste` Code onto `Manga Code` field');A.caption('- `Press Read`')
	A.button(AR,on_click=An,key='keyy')
D=A.text_input(':orange[Search:]',placeholder='Search..',key='search',help='Enter a title here to search for')
if D:
	D=D.replace(v,B);D=D.replace('!',B);D=D.replace('-',e);D=D.replace('?',B)
	with A.spinner(AS):
		with A.expander(':mag: Search'):
			Au=f"https://daotranslate.net/?s={D}";A8=Y.get(Au);Av=f"https://manhuaaz.com/?s={D}&post_type=wp-manga&op=&author=&artist=&release=&adult=";A9=Y.get(Av)
			if A8.status_code==200 and A9.status_code==200:
				Aw=R(A8.text,V);Ax=R(A9.text,V);AA=Aw.find(Q,{W:AT});AB=Ax.find_all('a',href=lambda href:href and href.startswith(AU))
				if AA and AB:
					l=AA.find_all(Q,{W:AV});Ay=iter(AB)
					for T in l:
						m=T.a[g];U=m.split(AW)[1].replace('/',B).title();n=U.replace('-',e);a=f"https://daotranslate.net/{U}-chapter-1/"
						with A.spinner(AS):
							A.write(f"[{n}]({a})");L=T.img[d];M=a;C,N=K(M)
							if L:A.image(L,use_column_width=h)
							if a:O=f"\n                                {C}\n                                ";E=S(C,N);A.code(O,language=X);A.button(f,on_click=Z,args=[E],key=j())
							A.divider()
							try:
								AC=next(Ay);b=AC.get(g)
								if'chapter'not in b:o=f"{b}chapter-1/"
								else:o=b
								Az=b.split(AU)[1];AD=AC.find(t);M=o;C,N=K(M)
								if AD:A.write(f"[{Az}]({o})");L=AD.get(AX);A.image(L,caption=C,use_column_width=h);O=f"\n                                    {C}\n                                    ";A.code(O,language=X);A.caption(A0);A.divider()
							except StopIteration:break
A_,B0,B1=A.columns(3)
BI=A.columns([1,2])
M='random'
C,N=K(M)
with A_:
	B2=A1.choice(string.ascii_uppercase)
	with A.expander(':books: Novels'):
		AE=Y.get(f"https://daotranslate.us/?s={B2}")
		if AE.status_code==200:
			B3=R(AE.text,V);AF=B3.find(Q,{W:AT})
			if AF:
				l=AF.find_all(Q,{W:AV})
				for T in l:
					m=T.a[g];U=m.split(AW)[1].replace('/',B).title();n=U.replace('-',e);p=f"https://daotranslate.us/{U}-chapter-1/";A.write(f"[{n}]({p})");L=T.img[d];M=p;C,N=K(M)
					if L:A.image(L,use_column_width=h)
					if p:O=f"\n                        {C}\n                        ";E=S(C,N);A.code(O,language=X);A.button(f,on_click=Z,args=[E],key=j())
					A.divider()
async def B4(url):
	async with J.ClientSession()as B:
		async with B.get(url)as A:
			if A.status==200:return await A.text()
			else:return
async def AG(url,mapping=z):
	C=mapping;D=await B4(url)
	if D:
		I=R(D,V);J=I.find_all(Q,class_='page-item-detail manga')
		for B in J:
			E=B.find('a',class_='btn-link');F=B.find(t);L=B.find('h3',class_='h5').text.strip()
			if E and F:
				G=E.get(g);M=F.get(AX);A.write(f"[{L}]({G})");A.image(M,use_column_width=h);A.caption(A0);A.divider();N=G;H,P=K(N);O=f"\n                {H}\n                "
				if C is not z:url=S(H,C)
				A.code(O,language=X)
async def B5():
	D={'Top Rated':'https://nightcomic.com/','Panels':'https://manhuaaz.com/'}
	for(E,(B,C))in AJ(D.items()):
		if E==0:
			with B0:
				with A.expander(f"{B}"):await AG(C)
		else:
			with B1:
				with A.expander(f"{B}"):await AG(C)
asyncio.run(B5())
A.image(Al)
q=A.empty()
E=S(A.text_input(':orange[Manga Code:]',value=B,placeholder='iuuqt://ebhdrrghmbuf.vt/..',key='readfield',help='Enter Manga Code here'),N)
B6=A.button(':green_book: Read',help=f,key='readbutton',use_container_width=I)
if B6:
	if AY in E:
		with A.spinner('Loading, please be patient..'):Z(E)
	if AY not in E.lower():
		with A.spinner(AN):
			AH=k()
			if AQ in E.lower():A.session_state.image_links=Ag(E)
			else:A.session_state.image_links=A2(E)
			A.session_state.current_image_index=0
			if A.session_state.image_links:
				for B7 in A.session_state.image_links:A.image(B7,use_column_width=F)
				A.write(f"Total Images: {G(A.session_state.image_links)}");A3(A.session_state.image_links);AI=E;r=B.join([A for A in AI if A.isdigit()]);B8=H(P(r)+P(+1));B9=H(P(r));BA=H(AI.replace(r,B8));C,N=K(BA);A.caption(AO+B9+AP+C);O=f"\n                {C}\n                ";A.code(O,language=X);A.caption(A0)
A.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>",unsafe_allow_html=F)
A.markdown('<style> footer {visibility: hidden;} </style>',unsafe_allow_html=F)
 

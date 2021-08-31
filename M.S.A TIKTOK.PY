import random
import requests
from colorama import *
import webbrowser
import time
import sys

def kata(s):
	for c in s + "\n":
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(10./1000)
		
kata("""
\033[1;31m<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<

	\033[1;30m	______   _      _____     _
	\033[1;31m	|_   _(_) | __ |_   _|__ | | __
	\033[1;30m	  | | | | |/ /   | |/ _ \| |/ /
	\033[1;31m	  | | | |   <    | | (_) |   <
	\033[1;30m	  |_| |_|_|\_\   |_|\___/|_|\_\



\033[1;31m<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<\<

\033[1;31mAouthr            \033[1;30m : \033[1;31mM.S.A
\033[1;31mTeleGram Channel  \033[1;30m : \033[1;31m@SQ21C
          \033[1;30m  \033[1;31m

""")


chart = '.qwertyuio.pa.sd_fghj_klzx.cv_bnm1234567890_'
rq = requests.session()
f = Fore.MAGENTA
r = Fore.GREEN
w = Fore.RED

webbrowser.open("")
webbrowser.open("")
print(""
      )
print(""
      )
print(""
      )
tknb = input(f + "[+] Token: ")
id = input(f + "[+] ID: ")
print("===========================================(M.S.A)=====================")
btn = input(r + "Click Enter ! ")
if btn == "" \
          :
    while True:
        lst = str("".join(random.choice(chart) for _ in range(4)))
        trl = f"https://www.tiktok.com/@{lst}?"
        hdr = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Connection": "close",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"
        }
        rqs = rq.get(trl, headers=hdr).status_code
        if rqs == 404:
            print(f'{f}[{r}Y{f}]{f} Available: {f}[{w}{lst}{f}]')

            bot = f'https://api.telegram.org/bot{tknb}/sendMessage?chat_id={id}&text= UZER TikTok✅: {lst}\nBy : @SQ21C'
            rq.get(bot)
            with open("Hunts @SQ21C.txt", "a") as gre:
                gre.write(lst + "\n")
        else:
            print(f'{f}[{r}N{f}]{r} UnAvailable: {f}[{w}{lst}{f}]')

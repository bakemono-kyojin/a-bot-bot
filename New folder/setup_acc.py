#!/bin/env python3
from tgbot.services.api_sqlite import *
"""
*
you can re run setup.py 
if you have added some wrong value

"""
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

import os, sys
import time

def banner():
    print(f"""
´´´´¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶
´´¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶
´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ´¶¶¶¶¶´
´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶
´´´´´´´´´¶¶¶¶¶¶¶¶
´´´´´´´´´´´¶¶¶¶
{re}

by rikudo
        """)
        
def requirements():
    def csv_lib():
        banner()
        print(f'{gr}[{cy}+{gr}]{cy} this may take some time ...')
        os.system("""
			pip3 install cython numpy pandas
			python3 -m pip install cython numpy pandas
			""")

    banner()
    print(f'{gr}[{cy}+{gr}]{cy} it will take upto 10 min to install csv merge.')
    input_csv = input(
        f'{gr}[{cy}+{gr}]{cy} do you want to enable csv merge (y/n): '
    ).lower()
    if input_csv == "y":
        csv_lib()
    print(f"{gr}[+] Installing requierments ...")
    os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch config.data
		""")
    banner()
    print(gr+"[+] requierments Installed.\n")


def config_setup():
    import configparser
    banner()
    cpass = configparser.RawConfigParser()
    cpass.add_section('cred')
    xid = input("[+] enter api ID : " )
    cpass.set('cred', 'id', xid)
    xhash = input("[+] enter hash ID : " )
    cpass.set('cred', 'hash', xhash)
    xphone = input("[+] enter phone number : " )
    cpass.set('cred', 'phone', xphone)
    with open('config.data', 'w') as setup:
        cpass.write(setup)
        invited24 = 0
        add_account_todb(xid, xhash, xphone, 0,'available')
    print(f"{gr}[+] setup complete !")

def merge_csv():
    import pandas as pd
    import sys
    banner()
    file1 = pd.read_csv(sys.argv[2])
    file2 = pd.read_csv(sys.argv[3])
    print(f'{gr}[{cy}+{gr}]{cy} merging {sys.argv[2]} & {sys.argv[3]} ...')
    print(f'{gr}[{cy}+{gr}]{cy} big files can take some time ... ')
    merge = file1.merge(file2, on='username')
    merge.to_csv("output.csv", index=False)
    print(f'{gr}[{cy}+{gr}]{cy}' + ' saved file as "output.csv"\n')

def update_tool():
	import requests as r
	banner()
	source = r.get("https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/.image/.version")
	if source.text == '3':
		print(gr+'['+cy+'+'+gr+']'+cy+' alredy latest version')
	else:
		print(gr+'['+cy+'+'+gr+']'+cy+' removing old files ...')
		os.system('rm *.py');time.sleep(3)
		print(gr+'['+cy+'+'+gr+']'+cy+' getting latest files ...')
		os.system("""
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/add2group.py
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/scraper.py
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/setup.py
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/smsbot.py
			chmod 777 *.py
			""");time.sleep(3)
		print(gr+'\n['+cy+'+'+gr+']'+cy+' update compled.\n')

try:
    if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
        print(f'{gr}[{cy}+{gr}]{cy} selected module : {re}{sys.argv[1]}')
        config_setup()
    elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
        print(f'{gr}[{cy}+{gr}]{cy} selected module : {re}{sys.argv[1]}')
        merge_csv()
    elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
        print(f'{gr}[{cy}+{gr}]{cy} selected module : {re}{sys.argv[1]}')
        update_tool()
    elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
    	requirements()
    elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
    	banner()
    	print("""$ python3 setup.py -m file1.csv file2.csv
			
	( --config  / -c ) setup api configration
	( --merge   / -m ) merge 2 .csv files in one 
	( --update  / -u ) update tool to latest version
	( --install / -i ) install requirements
	( --help    / -h ) show this msg 
			""")
    else:
        print('\n'+gr+'['+re+'!'+gr+']'+cy+' unknown argument : '+ sys.argv[1])
        print(f'{gr}[{re}!{gr}]{cy} for help use : ')
        print(f'{gr}$ python3 setup.py -h' + '\n')
except IndexError:
    print('\n'+gr+'['+re+'!'+gr+']'+cy+' no argument given : '+ sys.argv[1])
    print(f'{gr}[{re}!{gr}]{cy} for help use : ')
    print(
        f'{gr}[{re}!{gr}]{cy} https://github.com/th3unkn0n/TeleGram-Scraper#-how-to-install-and-use'
    )
    print(f'{gr}$ python3 setup.py -h' + '\n')

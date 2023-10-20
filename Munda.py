from urllib import response
import mechanize
import os
import datetime
import sys
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)

logo =  """\033[1;37;1m     

\033[1;37;1m  
\033[1;37;1m
\033[1;37;1m   ██╗    ██╗ █████╗ ██╗     ██╗
\033[1;3;1m   ██║    ██║██╔══██╗██║     ██║
\033[1;37;1m   ██║ █╗ ██║███████║██║     ██║
\033[1;37;1m   ██║███╗██║██╔══██║██║     ██║
\033[1;31;1m  ╚███╔███╔╝██║  ██║███████╗██║
\033[1;37;1m  ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝
\033[1;37;1m-----------------------------------------------
\033[1;37;1m  Author   : W9LI DON HERE RUSHTAM+USMA KI B3H3N KO CH0DK3 K0M9 M3 PAGUCH9 N3 BWLA W9LI H3R3
\033[1;37;1m  Facebook : https://www.facebook.com/karna.chenaih?mibextid=ZbWKwL
\033[1;37;1m  Whatsapp : 8882567807
\033[1;37;1m  Virson   : 6.1.3
\033[1;37;1m-----------------------------------------------"""

def menu():
	os.system('clear')
	print(logo)
	print('[1] Random Uid Crack')
	print('[2] Contact To Owner')
	print('[0] Exit')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		md()
	elif opt =='2':
		Contact()
	elif opt =='0':
		exit()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()

def login():
    browser.open(url)
    browser.select_form(nr = 0)
    coki = input(' [🩵] Inter Cookies : ')
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    exit(1)
    
print(47*'\033[1;37;1m-')
sp("\033[1;37;1m[?] Enter Chat Group/inbox Link\n")
print(47*'\033[1;37;1m-')
cid = str(input('\033[1;37;1m[?] Enter Link : '))
curl = 'https://m.facebook.com/messages/t/' + str(cid)

print("\033[1;34;40m", end = "")
print(47*'\033[1;37;1m-')
sp("\033[1;37;1m[?] Enter Notepad Loder/gali File Name\n")
print(47*'\033[1;37;1m-')
np = str(input('\033[1;37;1m[?] Enter File Name : '))
f = open(np, 'r')
lines = f.readlines()
f.close()
print("\033[1;33;40m", end = "")
sp("\033[1;37;1m[?] Enter The Time Delay In Seconds\n")
print(47*'\033[1;37;1m-')
t = int(input('\033[1;37;1m[?] Enter Time : '))

os.system('clear')
print(logo)

count = 0
while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(t)
            findtextchat(curl)
            sendtextconvo(line)
            count += 1
            if count % 10 == 0:
                sleep(1)
                clear()
                print("\033[0;37;41m\n")
               
                

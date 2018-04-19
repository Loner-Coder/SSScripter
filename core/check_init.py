#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

import time
import subprocess
import socket
from colors import *

def check_init(web):

	if 'http' in web:
		web = web.replace('http://','')
		web = web.replace('https://','')
	else:
		pass

	print O+" [*] Peek-a-boo'ing the server..."
	time.sleep(0.5)
	try:
		socket.gethostbyname(web)
	except:
		print R+' [-] Site appears to be down!'
	print GR+' [*] Peforming basic check for the vulnerability...'
	time.sleep(1)
	local_web = 'localhost.' + web
	print GR+' [!] Step (1) detecting webaddress...'
	try:
		ip = socket.gethostbyname(local_web)
		print G+' [+] Site seems to have potential Same Site Scripting...'
		if (str(ip) == '127.0.0.1' or '0.0.0.0'):
			print G+' [+] Heuristics reveal that site may be vulnerable...'
			time.sleep(0.5)
			print GR+' [*] Passing on to module (2)...'
			init1 = subprocess.Popen(['ping','-c 4',local_web], stdout=subprocess.PIPE)
			mp = init1.communicate()[0]
			if (('failure' not in mp) and ('not known' not in mp)):
			    if (('127.0.0.1' in mp) or ('0.0.0.0' in mp)):
				print G+' [+] Module (2) reveals potential vulnerability...'
				time.sleep(0.4)
				print GR+' [*] Confirming vulnerability...'
				init2 = subprocess.Popen(['nslookup',local_web], stdout=subprocess.PIPE)
				fm = init2.communicate()[0]
				if '127.0.0.1' or '0.0.0.0' in str(fm):
					time.sleep(0.5)
					print G+' [+] '+O+local_web+G+' is vulnerable to Same Site Scripting!\n'
					wo = raw_input(C+' [#] Same site scripting vulnerability has been detected!\n [#] Do you want to continue looking for vulnerabilities? (y/N) :> '+B)
					if wo == 'y':
						pass
					elif wo == 'n':
						print GR+'\n [!] Report this bug :)'
						print B+' [!] Goodbye mate... See ya!\n'
						sys.exit(0)
					elif wo == 'N':
						print GR+'\n [!] Report this bug :)'
						print B+' [!] Goodbye mate... See ya!\n'
						sys.exit(0)
					elif wo == 'Y':
						pass
					else:
						print R+' [-] Wrong input!'
						print G+' [+] Moving on...'
						pass
			    else:
				print R+' [-] '+R+'Module (2) reveals that '+O+web+R+' is immune to Same-Site Scripting!\n'
			else:
			    print R+' [-] You have unstable internet connection!'
		else:
			print R+' [-] Heuristics reveal that '+O+web+R+' is immune to Same-Site Scripting!\n'
	except:
		print R+' [-] Heuristics reveal that '+O+web+R+' is immune to Same-Site Scripting!\n'

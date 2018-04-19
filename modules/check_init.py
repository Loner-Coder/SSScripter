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
from colors import *

def check_init(web):

	if 'http' in web:
		web = web.replace('http://','')
		web = web.replace('https://','')
	else:
		pass

	print GR+' [*] Peforming basic check for the vulnerability...'
	local_web = 'localhost.' + web
	init1 = subprocess.Popen(['ping','-c 4',local_web], stdout=subprocess.PIPE)
	mp = init1.communicate()[0]
	if 'failure' and 'not known' not in mp:
	    if '127.0.0.1' or '0.0.0.0' in mp:
		print G+' [+] Heuristics reveal potential vulnerability...'
		time.sleep(0.4)
		print GR+' [*] Confirming vulnerability...'
		init2 = subprocess.Popen(['nslookup',local_web], stdout=subprocess.PIPE)
		fm = init2.communicate()[0]
		if '127.0.0.1' or '0.0.0.0' in fm:
			time.sleep(0.5)
			print G+' [+] '+O+local_web+G+' is vulnerable to Same Site Scripting!\n'
	    else:
		print R+' [-] '+R+'Heuristics reveal that '+O+web+R+' is immune to Same-Site Scripting!\n'
	else:
	    print R+' [-] You have unstable internet connection!'

#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

from impo import *
global vuln
vuln = []
novuln = []

def sss_main(web):

	print R+'\n    S - S - S   T E S T E R'
	print R+'   =========================\n'

	global fileo
	fileo = 'tmp/'+web+'_subdom_paths.txt'
	with open(fileo,'r') as dom:
	    for m in dom:

		m = m.replace('\n','')
		print O+' [*] Testing '+GR+m+O+' for Same-Site Scripting...'
		try:
			print C+' [*] Checking '+B+m+'...'
			s = subprocess.Popen(['ping','-c 4',m], stdout=subprocess.PIPE)
			mp = s.communicate()[0]
			if (('failure' not in mp) and ('not known' not in mp)):
			    if (('127.0.0.1' in mp) or ('0.0.0.0' in mp)):
				print G+' [+] '+O+m+G+' is vulnerable to Same Site Scripting!\n'
				vuln.append(m)
			    else:
				print R+' [-] '+O+m+R+' is immune to Same-Site Scripting!\n'
				novuln.append(m)
			else:
			    print R+' [-] You have unstable internet connection!'

		except KeyError:
			print R+' [-] Error!'

	print B+' [+] Vulnerable subdomains : '+C+str(len(vuln))
	print O+' [+] Non-vulnerable : '+C+str(len(novuln))+'\n'
	print G+' [+] Done !'
	time.sleep(0.5)
	print C+' [*] See ya mate!\n'
	time.sleep(0.4)
	sys.exit(0)

#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

from impo import *

def subdom_brute(web):

	global inputFile
	inputFile = raw_input(C+' [!] Enter the wordlist path for subdomain bruteforce.\n [!] Default (files/subdomains.lst) [Press Enter if default].\n [#] Your input :> ')
	if inputFile == '':
	    inputFile = 'files/subdomains.lst'
	    pass
	else:
	    inputFile = check_input_file(inputFile)

	try:
	    print GR+' [*] Importing wordlist path to be bruteforced...'
	    with open(inputFile,'r') as lol:
		for path in lol:
		    a = path.replace("\n","")
		    sublist.append(a)
	except IOError:
	    print R+' [-] Wordlist not found!'

	global found
	web = check_Http(web)
	tld0 = get_tld(web, as_object=True)

	if len(sublist) > 0:
	    for m in sublist: 
		furl = str(m) + '.' + str(tld0)
		flist.append(furl)

        if flist:
	    time.sleep(0.5)
	    print R+'\n      B R U T E F O R C E R'
	    print R+'     =======================\n'
	    print GR+' [*] Bruteforcing for possible subdomains...'
	    for url in flist:
	        if 'http://' in url:
		    url = url.replace('http://','')
	        elif 'https://' in url:
		    url = url.replace('https://','')
	        else:
		    pass
		try:
		    ip = socket.gethostbyname(url)
		    print G+'\n [!] Subdomain Found : '+O+url+P+' ['+str(ip)+']'
		    found.append(url)
		except:
		    sys.stdout.write(B+'\r [*] Checking : '+C+url)
		    sys.stdout.flush()
	else:
		print R+' [-] Could not resolve TLD...'

	return found


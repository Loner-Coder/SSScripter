#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

import time
from colors import *
from impo import *
from subdom_main import *

def sss_init(web):

	vuln = []
	novuln = []
	dom = []
	time.sleep(0.5)
	print O+' [*] Hold on... Gathering subdomains...'
	time.sleep(0.5)
	print GR+' [*] Initializing subdomain gathering...'
	time.sleep(0.5)
	print C+' [*] Finding subdomains path file...'
	fileo = 'tmp/'+web+'_subdom_paths.txt'
	if os.path.isfile(fileo):
	    print G+' [+] Subdomains path file found!'
	    pass

	else:
	    print R+' [-] Subdomain path file not found...'
	    time.sleep(0.5)
	    print O+' [*] Gathering subdomains...'
	    subdom_main(web)

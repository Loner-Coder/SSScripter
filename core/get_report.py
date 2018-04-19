#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

from colors import *

global total
total = []

def get_report(web, found, final):

	print R+'\n   R E P O R T'
	print R+'  =============\n'
	if ((len(found) > 0) or (len(final) > 0)):
	    print O+' [!] Subdomains found for '+G+web
	    print C+'  |'
	    for m in found:
		print C+ '  +-- ' +GR+ m
		total.append(m)
	    for p in final:
		if p not in found:
		    print C+ '  +-- '+GR+p
		    total.append(p)
	
	else:
	    print R+' [-] No Subdomains found for ' + O+web
	print '\n'
	return total

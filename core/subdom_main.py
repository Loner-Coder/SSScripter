#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

def subdom_main(web):

	from impo import *
	global fileo
	fileo = 'tmp/'+web+'_subdom_paths.txt'
	open(fileo,'w+')
	print R+'\n    S U B D O M A I N   G A T H E R E R'
	print R+'   =====================================\n'
	time.sleep(0.7)
	print B+' [*] Initializing Step [1]...'
	subdom_brute(web)
	print G+'\n [+] Module [1] Bruteforce Completed!\n'
	print B+' [*] Initializing Step [2]...'
	API_Retriever(web)
	print G+' [+] Module [2] API Retriever Completed!\n'
	acc = get_report(web, found, final)
	print O+' [*] Writing found subdomains to a file...'
	if acc:
	    for pwn in acc:
		vul = str(pwn) + '\n'
		miv = open(fileo,'a')
		miv.write(vul)
		miv.close()
	print G+' [+] Done!'

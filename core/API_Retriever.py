#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

from colors import *
import requests
import time

def API_Retriever(web):

    global final
    final = []
    wew = []
    time.sleep(0.4)
    print R+'\n    A P I   R E T R I E V E R  '
    print R+'   ==========================='

    print(GR + color.BOLD + ' [!] Retriving subdomains...')
    time.sleep(0.4)
    print(""+ GR + color.BOLD + " [~] Result: "+ color.END)
    dom = web
    text = requests.get('http://api.hackertarget.com/hostsearch/?q=' + dom).text
    result = str(text)
    print G + result
    mopo = result.splitlines()
    for mo in mopo:
	ro = mo.partition(',')[0]
	final.append(str(ro))

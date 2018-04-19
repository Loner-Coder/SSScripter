#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

def check_Http(web):

	if 'http://' in web:
		web = web.replace('http://','')
	elif 'https://' in web:
		web = web.replace('https://','')
	else:
		pass

	web = 'http://' + web 
	return web 

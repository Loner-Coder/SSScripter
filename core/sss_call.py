#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

from impo import *

def sss_call():

	banner_main()
	banner_sub()
	web = web_input()
	check_init(web)
	sss_init(web)
	sss_main(web)

#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    SSScripter     #
#-:-:-:-:-:-:-::-:-:#

#Author: Pinaxx (@_tID)
#This module requires SSScripter
#https://github.com/the-Infected-Drake/SSScripter

import os
from colors import *

def check_input_file(inputFile):
	while(True):
		print GR+' [*] Importing wordlist...'
		if(inputFile[0] == '\''): 
			inputFile = inputFile[1:]
		if(inputFile[len(inputFile)-1] == '\''): 
			inputFile = inputFile[:-1]
		if(os.path.exists(inputFile)):
			return inputFile
		print R+" [-] Cannot find '%s'!" % inputFile
		inputFile = raw_input(O+' [*] Enter a valid path of file [press Enter for default] :> ')
		return inputFile

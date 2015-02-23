#!/usr/bin/env python
#
# Parser for Websites by using Regex
# History:
# changed into a module - 09.Feb 2015 @neo_hac0x
# written - 12.Jul 2014 @neo_hac0x

import urllib
import sys
import re

def dbg(var):
	return "DEBUG: " + var 

def log(file, data):
	with open(file, "a+") as f:
		f.write(data + "\n")

def csRegex(regex, filename):
	pattern = re.compile(regex)
	data = re.findall(pattern, filename)
	return data

# function to parse any Data with a regex
def help ():
	return "Usage: parse.fromUrl(url, regex), parse.fromFile(filename, regex)"

def fromUrl(url, regex):
	url = "http://" + url
	dbg(url)
	dbg(regex)
	
	# get the website
	try:
		htmlfile = urllib.urlopen(url)
		htmltext = htmlfile.read()
	except IOError:
		return "ERROR: Change Url format"
	
	data = csRegex(regex, htmltext)
	
	for x in data:
		return x	

def fromFile(filename, regex):
	dbg(filename)
	dbg(regex)
	try:
		with open(filename) as f:
			return csRegex(regex, f)
	except:
		return "ERROR: Some shit happend"

#!/usr/bin/env python
#
# Parser for Websites by using Regex
# written 12.JUL 2014 @neo_hac0x

import urllib
import sys
import re

def dbg(var):
	print "DEBUG: " + var 

def log(file, data):
	with open(file, "a+") as f:
		f.write(data + "\n")

# function to parse any Data with a regex on any page
def getData (url, regex, filepath):
	url = "http://" + url
	dbg(url)
	dbg(regex)
	
	# get the website
	try:
		htmlfile = urllib.urlopen(url)
		htmltext = htmlfile.read()
	except IOError:
		print "ERROR: Connection Failure"
		sys.exit(1)
	
	pattern = re.compile(regex)
	data = re.findall(pattern, htmltext)
	
	for x in data:
		log(filepath, x)	

# Example for usage:
getData('www.amazon.de/gp/product/B004S7Q8CA', '<b class="priceLarge">(.+?)</b>', "/Users/neo/foobar.txt")

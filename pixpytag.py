#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pixivpy3 import *
import urllib
import urllib3
import sys
import os
import time
import errno
import requests
import shutil
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def PixivLogin():
	r = PixivAPI()
	r.login("yuumiinorin", "paozie1234")
	return r

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
			
def getWorkTag(loc,idnum):
	with open("{0}/taglist.txt".format(loc), 'r', encoding='utf-8') as f:
		lines = f.read().splitlines()
		cur_tag = lines[idnum]
		print(cur_tag)
	return cur_tag

def getWorkTagCount(loc,idnum):
	with open("{0}/taglist.txt".format(loc), 'r', encoding='utf-8') as f:
		lines = f.read().splitlines()
		idnum_count = len(lines)
	return idnum_count

def runBot(r):
	idnum = 0
	currentdir = os.path.dirname(os.path.abspath(__file__))
	work_tag = "天江衣"
	
	while current_total_image != total_images:
		while current_page != pages:
			while current_image != images:
				
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
if __name__ == "__main__":
	runBot(PixivLogin())
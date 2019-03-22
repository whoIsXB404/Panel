#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Web Injek Tion \n(ex : xnxx.com or www.xnxx.com : ")
	print "\n\nSiap Ndan : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "\033[0;1m NIH OK => ",req_link

def Credit():
	Space(9); print "\033[97;1m[]===P=A=N=E=L=A=D=M=I=N[+]>"
	Space(9); print "\033[94;1m-=|CODEX BY Tn./Low_gL2|=-"
	Space(9); print "\033[93;1m   Friends : whoIsXB404|=-"
	Space(9); print "\033[92;1mThnk : 2e4h-Friendshit-|=-"
	Space(9); print "\033[92;1m       LiT-Mci-Mca iTa-|=-"
	Space(9); print "\033[97;1m[]===P=A=N=E=L=A=D=M=I=N[+]>"
	Space(9); print "\033[91;1m"

Credit()
findAdmin()

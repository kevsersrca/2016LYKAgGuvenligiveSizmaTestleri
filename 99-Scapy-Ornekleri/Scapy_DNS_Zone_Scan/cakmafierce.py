#! /usr/bin/python

import scapy
import sys
import os
from scapy.all import *

def main(argv):
	domain = sys.argv[1]
	wd = sys.argv[2]
	
	wd_file =open(os.path.join(wd), 'r')
	wd_list = wd_file.readlines()
	wd_file.close()
	
	for i in wd_list:
		host = i.rstrip('\n')+"."+domain
		answer = sr1(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=str(host))),verbose=0)
		
		if not len(answer[DNS].summary().rstrip("DNS Ans")) == 0:
			print host + " ---> " + answer[DNS].summary().rstrip("DNS Ans")
		


if __name__ == "__main__":
   	main(sys.argv[1:])

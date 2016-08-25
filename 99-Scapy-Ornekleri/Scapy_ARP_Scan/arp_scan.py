#! /usr/bin/python
import sys
from scapy.all import *

def main(argv):
	try:
		interface = raw_input("Interface: ")
		ips = raw_input("IP Range: ")
	except KeyboardInterrupt:
		print "QUITTING..."
		sys.exit(1)
	conf.verb = 0
	ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ips),timeout=1,iface=interface,inter=0.05)

	print "MAC - IP:"
	for snd,rcv in ans:
		print rcv.sprintf(r"%Ether.src% - %ARP.psrc%")

if __name__ == "__main__":
	main(sys.argv[1:])

#! /usr/bin/python

import sys
from scapy.all import *

def main(argv):
	ip = raw_input("Enter Destination IP: ")
	pdu_type = raw_input("Enter PDU Type (set or get): ")
	com_string = raw_input("Enter Community String: ")
	ver = raw_input("Enten Version of SNMP: ")
	oid = raw_input("Enten OID: ")

	if  pdu_type == "get":
		p = IP(dst=ip)/UDP(dport=161)/SNMP(version=int(ver),community=com_string, PDU=SNMPget(varbindlist=[SNMPvarbind(oid=ASN1_OID(oid))]))
	elif pdu_type == "set":
                p = IP(dst=ip)/UDP(dport=161)/SNMP(version=int(ver),community=com_string, PDU=SNMPset(varbindlist=[SNMPvarbind(oid=ASN1_OID(oid),value=ip+".config")]))
	else:
		print "This script is only used for get or set pdu types.  QUITTING!"
		exit(1)
	sr(p)

if __name__ == "__main__":
	main(sys.argv[1:])

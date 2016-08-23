## Scapy 

- Scapy, özelleştirilmiş paketler üretmemizi sağlayan, Python ile yazılmış açık kaynak kodlu bir yazılımdır.

## Temel Komutlar

Komut | Açıklama
----- | -------
ls() | desteklenen protokolleri listeleyen metod
ls(protokol) | @protokol: desteklenen protokol listesinden herhangi bir protokol
send() | paket gönderme metodu (layer 3)
sendp() | paket gönderme metodu (layer 2)

## Örnekler:

**- ICMP Paketi:**

    => scapy
    
    => ip_header=IP(ttl=10, dst="127.0.0.11", src="127.14.11.1")
  
    => icmp_header=ICMP(type=8, code=0)
    
    => paket=ip_header/icmp_header
    
    => send(paket)
    
**- ICMP Paketi (Ethernet ile):**

    => scapy
    
    => ether_header=Ether(src="00:00:00:00:00:00", dst="00:00:00:00:00:00")
    
    => ip_header=IP(ttl=10, dst="127.0.0.11", src="127.14.11.1")
  
    => icmp_header=ICMP(type=8, code=0)
    
    => paket=ether_header/ip_header/icmp_header
    
    => sendp(paket)
    
**- TCP Paketi (SYN):**
    
    => scapy
    
    => tcp=TCP(sport=8080, dport=22, flags="S")
    
    => ip3=IP(src="127.0.0.1",dst="127.0.0.1")
    
    => paket3=ip3/tcp
    
    => send(paket3)
    
**- DNS Paketi:**

    => scapy

    => ip=IP(dest="8.8.8.8")
    
    => udp=UDP(dport=53)
    
    => dns=DNS(rd=1,qd=DNSQR(qname="www.facebook.com"))
    
    => dns_pack=ip/udp/dns
    
    => send(dns_pack)
    
**- DHCP Paketi:**

    => scapy
    
    => ip_d=IP(src="0.0.0.0", dst="255.255.255.255")
    
    => udp_d=UDP(sport=68, dport=67)
    
    => dhcp=DHCP(options=[("lease_time", 70000)])
    
    => dhcp_pack=ip_d/udp_d/dhcp
    
    => send(dhcp_pack)

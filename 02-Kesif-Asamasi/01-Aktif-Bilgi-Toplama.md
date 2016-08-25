## Aktif Bilgi Toplama

**İç Ağdaki Aktif Makinaların Tespiti:**
  
  => netdiscover -i eth0 <IP Range>
  => nmap -sP <IP Range>  --> ping sweep yöntemi ile
  => nmap -PR <IP Range>
  => arp-scan --interface=eth0 --localnet

**- NMAP:** Hedef hangi zafiyetlere sahip, açık portlar hangileri vs. analizler yapan tool. Sürekli istek yapmak bir anomalidir. Karşı taraf bunu fark edip bizi engelleyebilir.

**- Örnekler:**

  => nmap -sS -sV 10.0.2.7 -vv (syn paketi gönderir) synack döndüren portları listeler. (her portu açık gösterirse) 

  => nmap -sT -sV 10.0.2.7 -vv (açık olan portların versiyon taramasını yapar)

  => nmap -sT -sV -p80,8000-8100 10.0.2.7 -vv (spesifik olarak bir port veya port aralığını taramak)

  => nmap -sT -sV -p- 10.0.2.7 -vv (tüm portları tarar)

  => nmap -sT -sV 10.0.2.7 -O -vv (tüm portları tarar) (işletim sistemi tarar. en az bir açık bir de kapalı porta ihtiyacı var)

  => nmap -sT -sV 10.0.2.7 -O -vv -T4 -A (belirli süre kalıplarıyla arama yapar, A daha agresifleştirir)

  => nmap -f -f -sT -sV 10.0.2.7 -O -vv -T4 -A  (firewall varsa nasıl aşarız? paketi parçalara bölerek)

  => nmap --spoof-mac=IBM (atlatma yollarından biri, kendimizi IBM olarak gösteriyoruz)

  => nmap -D 192.168.1.1,192.168.1.2,10.0.2.7,192.168.1.3 (paketleri 4'e böldük ve 4 tane IP'den gönderilmiş olarak gösterip araya kendimizi de sıkıştırdık. sızma yöntemi)
    
  **- Parametreler:**  
  
  @sC = Script kullanımını sağlayan parametre
  
  @f = Gönderdiğimiz paketleri parçalar ve gönderildiği yerde birleşirler bu sayede güvenlik sistemi atlatılabilir.
  
  @system-dns = İşletim sisteminin DNS servisini kullanır.
  
  @sS = Syn paketi yollar
  
  @sA = Ack paketi yollar
  
  @sT = Bağlanma komutu
  
  @sV = Port versiyon taraması yapar
  
  @v = Verbose (gereksiz detayları gösterme)
  
  @vv = More verbose
  
  @T<0-5> = Zaman şablonlarıyla tarama yapar. Değer yükseldikçe daha hızlı tarar ama yavaş tarama daha sağlıklı sonuç verir.
  
  @A = Enable OS detection, version detection, script scanning, and traceroute (daha derin tarama)
  
**- En sık kullanılan 500 port:**
    
    => nmap 10.0.2.7 --top-ports 500
    
    => nmap -sV 10.0.2.7 
      
**- Scriptler(NSE):**

    => ls /usr/share/nmap/scripts/ (scriptleri listeler)

    => nmap -sT -sV -p 25 --script=ftp-vsftpd-backdoor.nse 10.0.2.7 (çalışmadı)
    
**- NMAP sonuçlarını rapor halinde alma:**

    => nmap 10.0.2.4 -oA rapor (root dizininin altında rapor.xml isminde bir çıktı üretir.)
    
**- NMAP'in gizlilik için sunduğu seçenekler:**

  **1. Decoy Scan:** Sahte IP'lerden paket üreterek kalabalık yaratıyor. Kalabalığın arasına 1 ya da 2 kendi IP'mizi ekleyince bizim yolladığımız paketler göze batmayacak şekilde kalıyor.
    
  **2. IDLE Scan:** Gerekenler: saldırgan, hedef, kurban(zombi). Uygulayabilmek için iki şart var. 
  
  * **Bir:** Bulacağınız kurbanın network trafiğinin az olması lazım. Güzel kurbanlar: boşta olan makineleler. 
  
  * **İki:**
    
  * **İşleyiş:** Kurbana paket gönderilir. Kurban geri cevap verir. Kurbana bu sefer hedeften gidiyormuş gibi bir paket daha gönderilir. Kurban geri cevabını hedefe döner. Hedefte kurbana eğer port kapalı veya arada firewall varsa reset+ack döner. Bu sefer kendimizden kurbana paket yollarız (x+1). Bize cevabı döner. Bu sayede hedef portun kapalı olup olmadığını veya arada firewall olup olmadığını öğrenebilme imkanımız olabilir. Bize dönen cevap x+1 ise port kapalı/firewall, x+2 ise port açık demektir.
      
      
**- unicornscan:** NMAP aracına alternatif, daha basit bir araç.

    => unicornscan IP:port (syntax)
    => unicornscan 10.0.2.7:25 (25.portu tara)

**- TOR:** Bizi Mass Network'e sokar ve IP adresimizi bu Mass Network'deki başka birinin IP adresiyle değiştirerek ulaşmak istediğimiz yere ulaştırır. Bunun riski bir başkası da bizim IP'mizi alarak başkasına saldırabilir ve saldıran olarak bizim IP'miz görünür.

    - Örnek kendini gizleme: saldırgan -> vpn -> vpn -> TOR -> vpn -> Kurban (hız pert, gizlilik OP)
    
    - NMAP ve Firefox Örneği: 
    
      => cat /etc/proxychains.conf (proxychains konfigürasyonlarını gösterir)
      
      => tor (tor servisini başlatır)
      
      => proxychains nmap 10.0.2.7 (tor'dan bir IP alarak nmap ile scan yapar)
      
      => firefox(advanced settings -> network -> settings -> manuel proxy -> socksv_4 host: 127.0.0.1 port:9050)
      
      => proxychains firefox (firefox'u tor'da açar) (bunu yaptıktan sonra IP'ni kontrol et)
    
**- DNS üzerinden bilgi toplama:** DNS sunucusu eğer sorgunun cevabını başka DNS sunucularından getirmeye çalışıyorsa buna recursive denir. DNS sunucusuna recursive olmayan sorgular gönderdiğimizde DNS sunucusunun cache'inde bu bilgi varsa geri döner, yoksa cevap gelmez. Bu sayede o DNS sunucusunda istediğimiz bilginin daha önce istenip istenmediğini öğrenebiliriz. Yani birisi bulmak istediğimiz siteye daha önce girmiş mi sorusunun cevabını alabiliriz.

  - Cache bilgileri sonsuza kadar saklamaz. belli bir süre sonra DNS sunucusu bilgileri kendisi tekrar almak için gider. bunun bilgisine de şuradan ulaşılabilir:
  
      => dig www.ibu.edu.tr 
      
      www.ibu.edu.tr. ///saniye (6673) IN A 194.27.225.124 (**Sonuç**)

**- DNS üzerinden toplanabilecek bilgiler:**

    - SOA kaydına bakılarak e-mail adresi alınabilir.
    
    - Zone Transfer yapılabilir.

    - Brute Force yapılabilir.

**- SOA kaydı sorgulama:**

    => nslookup -type=SOA ibu.edu.tr 
    
    => dig SOA ibu.edu.tr

**- DNS sunucusunu öğrenme:**

    => nslookup -type=NS ibu.edu.tr 
    
    => dig NS ibu.edu.tr

**- Zone Transfer:**

- İlk etapta yapmamız gereken şey hedefle ilgili sorumlu dns sunucularını bulmak. Bu yöntem maksimum kapsamı tespit edebilmek için kullanılır.

    => dig ns ibu.edu.tr
    
        => dig axfr ns2.ibu.edu.tr @ibu.edu.tr (başarılı olana kadar bütün dns sunucularını dene)

  - Başka örnek:

    => dig zonetransfer.me NS
      
        => dig axfr nsztm2.digi.ninja @zonetransfer.me (dns2)
      
        => dig axfr nsztm1.digi.ninja @zonetransfer.me (dns1)


**- Mail üzerinden bilgi toplama:** Mail header arasından bilgi toplanabilir. Bir e-mail grubuna e-mail yollandığında eğer o gruptan mail'i alamayacak bir kişi varsa, e-mail servisi bize bu kişinin yolladığımız e-maili alamayacağının bilgisini verirken kişiyi ifşa etmiş oluruz. 

  **- Kaynak header'e ulaşmak:** Gmail'e gir. Kaynak header'ini öğrenmek istediğin mail'i aç. Sağ üstteki reply'ın yanındaki oka bas. Show original'i seç.

  **- Kaynak header'in analizi için:** B> http://mxtoolbox.com/EmailHeaders.aspx
  
  - Örnek:
  
    => dig ns barkin.info (dns sunucusunu öğreniyoruz)
    
      => dig ns barkin.info @ns1.cloudns.net (e-posta'yı öğreniyoruz)
    
      => nc eposta.kilic.xyz 25 -v

**- ehlo localhost:** Aynı ağdaki makinelerin birbirlerine verdikleri selam. (GoT'daki valar morghulis gibi)

**- Routing:** Networkler arası bağlantının sağlanabilmesi için gönderilecek paketlerin  gönderilmesi işi için aracılık yapılması.

  - Üç makinenin arasındaki route işlemini yapma uygulaması (ortadaki router olarak çalışan makine linux) .

    => arp -a (arp tablosunu görüntülemek için)
      
    => route (routing tablosu)
      
    => route add -net 10.0.1.0/24 gw 10.0.2.1 (subnet'inde olmayan bir yere gitmeye çalışan makineye nasıl gideceğini söylememiz gerekiyor. bu komut ile söylüyoruz.)
      
    => echo 1 > /proc/sys/net/ipv4/ip_forward (aynı işlem karşı taraf için de yapılmamışsa işlem yapılan taraf paketi yollayabilir ama route işlemi yapılmamış taraf cevap gönderemez. route tablosu eklendikten sonra yönlendiriciyi de açmamız gerekir.)
      
    => route add -net 10.0.2.0/24 gw 10.0.1.1 (yönlendiriciye de nasıl gideceğini route add ile göstermemiz gerekiyor.)

**- NAT:**

    => iptables -t nat -L -vn (tabloyu gösterir)
    
    => iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

**- Firewall:** Firewall dediğimiz şey sadece hangi paketin hangi portlara gidip gidemeyeceğine karar verir. Yerine gidemeyen paketler düşer. Sistemde olmaması gereken bir bozukluk tespit edilerek atlatılır. 

**- Gateway:** Hiçbir şeyi bilmediğiniz, geri kalan her şey için yönlendirilmenizin yapıldığı yer. Örnek: Fransızca bilmiyorsun. Fransızca bilen tercüman kullanıyorsun. O tercüman işte gateway.

**- Cloudflare By pass:** Site DNS sunucularını cloudflare'a teslim edip onun süzgeçten geçirdiği trafiği alıyor. 

    => amap (İnternetin tamamını tarar.)

## Soru-Cevap

- Ağda bulunan ayakta bulunan bütün cihazların IP'lerini nasıl öğreniriz?
  
  * => ifconfig eth0 (ethernet ile bağlıysak, kendi IP adresimizi öğreniyoruz)
  
  * => netdiscover -i eth0 -r 10.0.2.0/24
  
  * => nmap -sP 10.0.2.0/24 -vv veya nmap -sP 10.0.2.0-150 -vv
  
- Crosscable ile bağlı ama farklı subnet'deki iki makine birbirleriyle nasıl iletişim kurar?

  * ARP ile. Aynı subnet'de olmayan makineler ARP ile iletişim kuramaz ancak gidilmek istenen IP'ye nasıl gidileceğini route add ile gösterirsek ağa ulaşacaktır.

- Neden ICMP değil de ARP ile bilgi topluyoruz?

  * Eğer ping engellenmişse ICMP ile hedef açık olsa bile kapalı gibi görürüz. ARP'ta böyle bir şey söz konusu değildir.


###### Notlar

  - Direk ack paketi yollayıp cevap alırsak firewall yok demektir.
  
  - Scapy ile çalışırken DNS(rd=1) değerini rd=0 ile değiştirirsek paket non-recursive olur.
  
  - dig için recurse parametresi ile non-recursive sorgu yollanılabilir.
  
  - fierce default wordlist -> /usr/share/fierce/hosts.txt
  
  - DNS: IP'yi domain'e, domain'i IP'ye çeviren servistir. reverse who.is -> IP ile sorgulattığımızda sınır içerisinde başka hedefler de elde etme ihtimalimiz vardır. O yüzden dns sorgusu yaptığında, reverse dns de yap.
  
  - ARP: Her makinenin arp tablosu vardır. IP adresi broadcast yapılır. Kime aitse onun MAC adresi öğrenilir. 2.katmanda çalışır. Makinelerin aynı subnet'de olması gerek.
  
  - ARP'ın herhangi bir doğrulama kabiliyeti yoktur. Yerel ağdaki makineleri keşfetmek için ARP protokolü kullanılabilir.
  
  - Örnek ARP keşfi: 
  
    => iptables -t filter -L -vn
    
    => nc 192.168.0.2 22 -v
    
    => arping 192.168.0.2 
    
    => (ağı izleme) tcpdump -i eth0 -nnv arp
    
    => arp-scan -l -I eth0 (yerel ağdaki bütün makineleri tarayarak sonuç alma işlemi yapar)
    
  - [Scapy ile DNS Zone Scan ödevi](DNS_Zone_Scan/cakmafierce.py)
  
  - [Scapy ile ARP taraması ödevi](ARP_Taraması/arp_scan.py)

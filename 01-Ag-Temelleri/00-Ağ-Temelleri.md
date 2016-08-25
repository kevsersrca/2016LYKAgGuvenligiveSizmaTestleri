## Ağ Temelleri

## OSI Katmanları

**1. Physical Layer (Fiziksel Katman):** Elektrik akımlarını 1 ve 0 olarak yorumlar.

**2. Data/Link Layer (Veri Katmanı):** Veriyi nasıl transfer edeceğinizi yorumlayan katman. (MAC)(ARP,RARP)

**3. Network Layer (Ağ Katmanı):** Adresleme işleminin yapıldığı katman. (IP)

**4. Transportation Layer (Taşıma Katmanı):** Paketlerin gönderilip alındığı katman. (TCP/UDP)

**5. Session Layer (Oturum Katmanı):** Bağlantıdaki oturumların takibinin yapıldığı katman.

**6. Presentation Layer (Sunum Katmanı):** Veri uygulama katmanında kullanıcıya gösterilmeden önce dosyada yapılacak olan format değişikliklerinin yapıldığı katman. (SSL)

**7. Application Layer (Uygulama Katmanı):** Verinin en son halinin kullanıcıya gösterildiği katman.

## Genel Kavramlar

**- MAC Adresi:** Kullanılan donanımın adresi. 48bit. AA:BB:CC:DD:EE:FF formatında gösterilir. AA:BB:CC kısmı üretici kimliğinin yer aldığı kısımdır ve unique(eşsiz)dir. DD:EE:FF kısmı ürün kimliğinin yer aldığı kısımdır.

**- ARP:** IP adresi bilgisi kullanılarak sistemin fiziksel (MAC) adresini tespit eden protokol. ARP protokolünün hiçbir kontrol mekanizması yoktur.

  * Sınıf içerisinde Mehmet ile ulaşılmak isteniyor. Mehmet kim bilmiyoruz. Ne yaparız? Sınıfa gideriz. Mehmet kim diye bağırırız. Mehmet elini kaldırır ve elini kaldıran kişiyle konuşuruz.

**- RARP:** Fiziksel (MAC) adresi bilinen sistemin IP adresini öğrenmemizi sağlayan protokoldür.

  * Sınıfta 3.kümeden 5.sıradaki kişiyle konuşmam gerekiyor. Sınıfa gidip o kişinin kim olduğunu öğrenip o kişiyle konuşuruz.
  
- Mektubu adresine teslim edebilmek için 1)Kime yolladığımız 2)Nerede olduğu bilgisine ihtiyacımız var. ARP protokolünde 1 var, bunla 2'yi elde ediyoruz. RARP protokolünde 2 var, bunla 1'i elde ediyoruz.

**- TCP (Three-way handshake):** Bir bilgisayarla haberleşmek istediğiniz zaman bu haberleşme isteğini karşı tarafa bildirilip karşı taraftan da onay alırsa iletişimin kurulduğu ve bu iletişimin sonlandırılana kadar geçer zaman içerisinde herhang bir kayıp veya sorun yaşanmamasını garanti etmeye çalışan protokoldür.
 ```
 A              B
 | ----SYN----> |
 | <--SYN+ACK-- |  Three-way Handshake
 | ----ACK----> |
 ```

**- UDP:** TCP'den farklı olarak dosyanın ulaşıp ulaşmadığını kontrol etmez. Daha hızlıdır. (shoot and forget) TCP'de veri 4.pakette yollanmaya başlanırken UDP'de veri 1.paketten itibaren yollanır. Yani UDP TCP'den 4 kat daha hızlıdır.

  - UDP, açık olan portu ve servisi bilip bunlara paket yolladığınızda, ancak o zaman cevap alacağınız bir protokoldür. Eğer buna rağmen cevap gelmiyorsa 2 ihtimal vardır. Ya servis yolladığınız paketi anlamadı, ya da arada firewall var.
  
  - UDP ile veri yolladığımız port kapalıysa ve firewall yoksa; ICMP port kapalı mesajı döndürür.

**- Port:** Bir makinenin üzerinde kendinden başka makinelerin ulaşabilmesi için açılan bir kapı olarak düşünülebilir. Birden fazla servise erişmek için bu kapılardan hangisi uygunsa oradan girip ordan konuşmaya sağlayan açık kapılardır. Kaç port vardır? 2^16 (Source-Port 16bit olduğu için)
  
**- DNS:** Domainlerin eşleşen IP'lerini bulmamızı sağlayan sunuculardır. Eğer DNS sunucusu, sorduğumuz domain'in IP'sine sahip değilse, içerisinde statik olarak kazılı olan ROOT DNS sunucularına sorar. DNS IP'yi elde ettiğinde bir daha aramamak için IP adresini cache içerisinde istediği domainden sorumlu sunucunun belirlediği süre boyunca saklar.

  * DNS Kayıt Türleri: A, mx, cname, ns, Ptr, SOA, txt
    
    * **A kaydı:** İstenilen domain'in IP adresini kaydeder.
    
    * **mx kaydı:** Her DNS sunucusu bir ya da birden fazla zone(alan)'dan sorumludur. O alan adından sorumlu mail sunucuların bulunduğu kayıt.
    
    * **cname kaydı:** Alias. Ağ kayıtlarına işaret eden takma ad.
    
    * **ns kaydı:** Alan adına ait authoritative DNS sunucusunun kaydının tutulduğu türdür.
    
    * **Ptr kaydı:** IP adresi verip domain sorduğumuzda geri dönen kayıt türü. (Reverse DNS)
    
    * **SOA kaydı:** Zone'un kendisine dair ve master dns sunucusuna dair bilgilerin bulunduğu kayıt.
    
    * **txt kaydı:** Opsiyonel olarak bilgi tutulmak istendiğinde kullanılan kayıtlar.
    
  * DNS kayıtlarını sorgulama örnekleri:
    
    * => dig www.linux.org.tr veya dig www.linux.org.tr A (önceden benim dns sunucum olarak kaydedilen kişi kimse ona sorgu gidecek)
    
    * ns kaydı sormak için: 
    
      => dig linux.org.tr NS (www'ları çıkarma sebebimiz host'tan sorumlu ns kaydının olmaması)
    
    * SOA kaydı için: 
    
      => dig linux.org.tr SOA
    
    * Bilinen DNS sunucularına sormak 
    
      => dig www.linux.org.tr @frig.linux.org.tr 
    
      => dig www.linux.org.tr @8.8.8.8
      
    * Reverse DNS sorgusu 
      
      => dig -x 139.179.139.181
      
      - Reverse DNS sorgusu ile IP adresine sahip olduğumuz adresin domainini bulabililiriz.
      
    * Tüm bilgileri sorgulamak için
    
      => dig linux.org.tr any
      
**- DHCP (Dynamic Host Control Protocol):** Makineye IP, Gateway, DNS, NetMask, Proxy verilebilir.

  - Eğer DHCP'deki IP havuzları dolduysa, boşa çıkan IP olmadığı sürece yanıt vermez. Makine kendisine apipas sınıfındaki reserve edilmiş IP'lerden bir IP alır.
  
  - MAC adresi değiştirildiğinde DHCP bize yeni bir IP verir. Çünkü bizi MAC adresimizden tanır. Eğer kira süresi yeterince yüksekse, bu işlem yeterince tekrar edilerek DHCP sunucusunun havuzu doldurulabilir.

  - Eğer birden fazla DHCP sunucusu varsa, en önce yanıt verene gidilir. Saldırgan kendi DHCP sunucusunu kurarak bilgileri manipüle edebilir.

**- Lease Time(Kira süresi):** Makinelere verilen IP sürelerinin son kullanma tarihi.

**- Router:** Ağa bağlanabilme kapasitesi olan makinelerin ilgili ağlara yönlendirmesini yapan makinedir.

**- Gateway:** Kargo firmaları örneği. Nasıl gideceğinizi bilmediğiniz yerlere verilerinizi gönderebilmeniz için aracılık yapan router'lara gateway denir.

 * Bir ağda IP havuzu dolarsa, o ağa yeni gelen client IP alamaz. O client'a Apipa IP verilir. DHCP hiçbir zaman broadcast'e kira süresi dolan var mı diye sormaz.
 * Bir ağda IP avuzları dolu olmayan iki DHCP server varsa; Client, IP isterse en hızlı IP veren DHCP sunucusuna kaydolur. Bu DHCP sunucusu bir saldırgan da olabilir.
 * Bir Client(saldırgan) sürekli MAC adresi değiştirerek DHCP sunucusundan IP isterse bu DHCP sunucusuna yönelik bir DoS saldırısı olur.
 * Bir ağda bulunan DHCP sunucusunun verdiği IP'lerin lease (kira) süreleri dolmak üzereyken, yeni bir DHCP sunucusu (saldırgan) ağa dahil olursa, clientlar IP adreslerini yeni DHCP sunucusundan alırlar. Böylece yeni DHCP sunucusunun vereceği gateway adresi üzerinden ağ iletişim kuracağı için saldırgan tüm ağı dinleyebilir. (MiTM- Man in The Middle Attack)

**- IP(Internet Protocol):** Her bir makinanın kendine ait eşsiz bir adresi olsun diye geliştirilmiş bir protokol. Kullanılan iki versiyonu vardır. IPv4 => 32bit IPv6 => 128bit 

  * IPv4: 192.168.1.1 => IIIIIIII.IIIIIIII.IIIIIIII.IIIIIIII (10'luk sistemdeki sayıyı 2'lik sisteme dönüştürmek) Mümkün aralık: 0.0.0.0 - 255.255.255.255
  
  * -IPv4 havuzu kendi içinde class'lara bölünmüştür:
  
    -A, B, C, D(multicast için reserve), E(komple reserve)

**- Alt ağ maskesi:** İkilik sayı sisteminde belli bir noktanın solu tamamen 1, sağı tamamen 0 yapılır. Onluk sisteme geri döndürüldüğünde elde ettiğimiz sayı alt ağ maskesidir. 1'lenen kısım Network IP'sine, 0'lanan kısım Broadcast IP'sine eşittir.

**- ICMP (Internet Control Message Protocol):** TCP/IP'nin düzgün çalışıp çalışmadığını kontrol eden protokoldür. 

  * Örnek: ICMP echo request, echo reply (ping atmak). Karşı tarafın ayakta olup olmadığını öğrenmek.

**- RFC 1918:**

**- Public IP:** İnternete bağlanılırken kullanılan IP adresidir. Eşsizdir(unique).

**- Private IP:** Public içerisindeki yerel ağdaki makinelere verilen IP, diğer private ağlarda da aynı IP kullanılabilir. Unique değildir.

- Private'deki bir makina internete erişmek istediğinde public'e dönüşmesi gerekir. Bu işlem NAT ile gerçekleşir.

- Şu adresler private olarak kullanılmak üzere ayrılmıştır:

  * 10.0.0.0        -   10.255.255.255  (10/8 prefix)
  
    172.16.0.0      -   172.31.255.255  (172.16/12 prefix)
    
    192.168.0.0     -   192.168.255.255 (192.168/16 prefix)

- Eğer birisi 172.18 ip adresinden saldırı alıyorum diyorsa, ya yerel ağdan saldırı geliyordur, ya da ip adresi değiştirilmiştir.

**- Multicast:** grup mesajı

**- Unicast:** birebir mesaj

**- Broadcast:** toplu mesaj 

## Public veya Private Olarak Kullanılmayan IP Grupları

**- 127.0.0.0/8** => Bir network olmasa dahi makinelerin birbirlerine bağlanabilmesi için ayrılmış grup.

**- 169.254.0.0/16 (Apipa)** => IP adresi manuel veya otomatik olarak verilmeyen makineler için ayrılmış grup. Bu gruptan IP'yi almadan önce o ağda broadcast yapar ve eğer o IP alınmamışsa kendisine reserve eder.

## Soru-Cevap

- Ethernet networkleri için Data/Link katmanına denk gelen protokellerin isimleri nedir?

  * ARP/RARP. ARP: MAC bilgisi kullanılarak sistemin fiziksel lokasyonunu tespit eden protokol. RARP: Fiziksel konumu bilinen sistemle iletişim kurmayı sağlayan protokol.
  
- 192.168.10.0/24 ip adresinin bir makinaya verilebilmesi için subnet mask ne olmalıdır?

  * 192.168.10.0 => 11000000.10101000.00001010.00000000
  * 
    Normalde(Subnet mask): 11000000.10101000.00001010**|**.00000000

    1 sola kaydırırsak: 11000000.10101000.0000101**|**0.00000000 => hala network ip'sidir makinaya verilemez.
    
    2 sola kaydırırsak: 11000000.10101000.000010**|**10.00000000 => sağ tarafta bir tane 1 olduğu için artık bu ip'yi bir makinaya verebiliriz.

  * 192.168.10.255/24 IP'sini bir makinaya verebilmek için ise çentiği normal konumdan bir kere sola kaydırmak yeterli.
  
- Açık olan bir TCP portuna SYN paketi yollarsak SYNACK cevabı alırız. Peki açık olan bir porta ACK paketi yollarsak ne olur?

  * Reset döner. Düzgün başlatmadığınızda veya herhangi bir problemle karşılaşıldığında o protokol sonlandırılır.

- Kapalı bir porta SYN yollarsak ne olur?

  * Reset döner. Reset'in ne için döndüğünü(port başından beri mi kapalı yoksa bize mi kapatıldı(?)), hangi aşamada reset döndüğünü gözlemleyerek anlayabiliriz.

- Port kesin açık. Güvenlik duvarı var. SYN gönderdik. Ne olur?

  * Belli olmaz. Reset dönebilir. Cevap dönmeyebilir.

- Port açık mı kapalı mı bilmiyoruz. SYN gönderdik. Cevap gelmedi? Ne oldu?

  * Kesin olan şey: firewall.

- Arada firewall var. ACK paketi gönderiyoruz. Reset dönüyor. Firewall'dan mı yoksa host'tan mı reset dönmüştür?

  * Bir de SYN paketi yollayarak anlaşılabilir. Eğer tekrar Reset dönüyorsa firewall'dan dönüyor demektir.

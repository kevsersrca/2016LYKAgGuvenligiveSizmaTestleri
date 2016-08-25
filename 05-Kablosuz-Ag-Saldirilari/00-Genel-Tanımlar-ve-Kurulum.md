## Wireless Network Attacks

- Kablosuz ağ sinyalleri eskiden herkese açık bir şekilde yayınlandığı için (radyo gibi) herkes tarafından takip edilebiliyordu.

**- BSSID:** Erişim noktasının (Access Point) MAC adresi.

**- ESSID:** Erişim noktasının ismi.

**- Uygulama:**

  => ifconfig
    
  => airmon-ng check kill (bize engel olabilecek servisleri kapatır)
    
  => airmon-ng start wlan0(wireless destekli kartlarımızı monitör modda kullanabilmemizi sağlayan araç)
    
  => airodump-ng wlan0mon (monitör moddaki sistemlerin yakaladığı bilgileri ekrana aktarır)
    
  **- CH:** Radyo mantığı; nasıl aynı anda birden fazla kanalı dinleyemiyorsak, wireless'da da 13 kanaldan birini aracın kanallar arası zap yapmasıyla dinleriz.
    
  **- Elapsed:** Geçen süre.
    
  **- PWD:** Erişim noktasının sinyal gücü hakkında bilgi verir. - değer alır, değer yüksekse erişim daha güçlüdür.

  **- Beacons:** Wireless'daki kontrol paketlerinin sayısını belirten kısım.

**- Data:** Bilgi alış-verişinin yapıldığı paket sayısı.

**- MB:** AP'in maksimum kablosuz ağ hızı. QoS destekli ise "e" harfi bulunur.

**- ENC:** Kullanılan şifreleme hakkında bilgi verir.

**- CIPHER:** Kullanılan şifrelemenin kullandığı algoritma bilgisini verir.

**- ATH:** Doğrulama için kullanılan protokolün bilgisini verir.

**- Sanal Interface Oluşturma:**

    => ifconfig wlp2s0:1 192.168.0.2 (sanal bir IP interface'i oluşturur)
    
    => ifconfig wlp2s0:1 down (sanal interface'i kaldırır)

**- Airodump menüsü iki bölüme ayrılır. İlk bölüm AP(erişim noktaları) ile alakalı olan bölümdür. İkinci bölüm erişim noktalarıyla alakalı istemciler ile ilgili olan bölümdür.**

**- İkinci kısım:** BSSID (Erişim noktalarının MAC adresleri, eğer bu alan boşsa client sadece tarama yapıyor demektir).

**- STATION:** Erişim noktasına bağlanan makinelerin MAC adresleri.

**- Rate:** AP ile Client - Client ile AP arası Mbps cinsinden veri iletim hızı.

**- Lost:** Kayıp paketler.

**- Frame:** Gelen paketler.

**- Probe:** ESSID değeri alır, daha önceden bağlanmış olduğu erişim noktaları varsa onları civarda tekrar aratmak için kullanır.

**- Eğer ESSID gizlenirse sadece kablosuz yayının ismini bilen kişiler bu kablosuz ağa bağlanabilir. (Probe işlemi)**

  => iwconfig wlp2s0 essid "Lyk-2016" (Interface ile erişim noktalarını birbirine bağlar(?))
  
  => dhclient wlp2s0

  => airodump-ng wlan0mon -c 1 --bssid C0:4A:00:E9:08:2C (filtreleme)

**- ESSID'i gözükmeyen <length: 0> bağlantıları izlemeye alırsak, o ağa biri tekrar bağlandığı zaman ESSID'ini öğrenebiliriz.**

**- MAC Filtreleme:** Sadece kaydedilen MAC adreslerine bağlantı izni verir veya bağlantıya kabul etmez.

**- MAC filtrelemeyi atlatma:** Ağa bağlı bir MAC adresini alıp kendi MAC adresi olarak gösterir.

**-Uygulama:**

    => ifconfig interface down
    
    => ifconfig interface hw ether hedef-MAC (airodump'dan buluyoruz)
    
    => ifconfig interface up

  - Eski haline döndürmek için:

    => ifconfig interface down
    
    => ifconfig interface hw ether kendi-MAC-adresimiz
    
    => ifconfig interface up

**- Wireshark raporu için:**

    => airodump-ng wlan0mon -c 6 --bssid C0:4A:00:E9:08:2C -w isim.pcap (Yayın yakalarsa isim.pcap içerisine kaydeder.) 

###### Notlar

  * Ağ Adaptörü Önerileri: Tp-Link WN722N, Alpha Chipset (051, 036), 
  
  * Kitap önerisi: Kali Linux Wireless Pen. Testing | Link: http://www.k4linux.com/2016/08/kali-linux-ebook-wireless-hack-pdf.html

  * Film Önerisi: Enigma
  
  * Wireless "full duplex" teknolojisini hala desteklememektedir. (Aynı anda hem veri yollayıp veri alma)

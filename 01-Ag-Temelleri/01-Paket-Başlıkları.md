## IP Header

![alt tag](http://www.cisco.com/c/dam/en_us/about/ac123/ac147/images/ipj/ipj_10-4/104_ip-spoof_fig1_sm.jpg)

**- Version:** (4bit) Gelen paketin IPv4 veya IPv6 olduğunun yorumlandığı kısım.

**- IHL:** (4bit) Yollanan pakete nasıl davranılacağını bildiren kısım. Acil mi veya bekleyecek mi vs.

**- Total Length:** (16bit) 2^16 = 65535byte (Maksimum Toplam Uzunluk) Paketin uzunluk bilgisinin olduğu kısımdır.

**- Identification:** (16bit) Kimlik bilgisi olarak eklenilen kısım. Host tarafından random oluşturulur.

**- Flags:** (3bits) Yollanan IP paketinin sağlıklı bir şekilde geçirilip geçirilmemesi için yeri geldiğinde parçalanıp parçalanmaması hakkında bilgi veren kısımdır.

**- Fragment Offset:** (13bits) Paket parçalandıysa parça sırasını belirten kısım.

**- Time to Live:** (8bit) Pakete verilen yaşam süresi. Eğer paket sonsuz döngüye girerse paketin kendini yok etmesi için verilen zamanı belirten kısım. (Kaç kere, saniye vs. değil)

**- Header Checksum:** (16bit) Paketteki bilgiler bir fonksiyona sokulup elde edilen değer burada belirtilir. Paketi alan kişi buradaki bilgiyi alır ve paketi fonksiyona sokup tekrar aynı değeri alıp almadığını kontrol ederek paketin bozulup bozulmadığını anlar. 

**- Source IP Address:** (32bit) Paketi gönderenin ip adresi.

**- Destination IP Address:** (32bit) Paketi alacak makinenin ip adresi.

## ICMP Header

![alt tag](http://3.bp.blogspot.com/-BJMT6npLBbw/UtYYLT95q4I/AAAAAAAAAeU/8xU9YD2HTn0/s1600/ICMP_Header.png)

**- Type:** (8bit) Hangi tipteki kontrol mesajının gönderildiğini belirten kısım.

**- Code:** (8bit) Tipleri alt dallara ayırıp daha detaylı bilgi veren kısım.

**- Checksum:** (16bit) Paketteki bilgiler bir fonksiyona sokulup elde edilen değer burada belirtilir. Paketi alan kişi buradaki bilgiyi alır ve paketi fonksiyona sokup tekrar aynı değeri alıp almadığını kontrol ederek paketin bozulup bozulmadığını anlar.

## TCP Header

![alt tag](http://intronetworks.cs.luc.edu/1/html/_images/tcp_header.png)

**- Sequence Number ve Acknowledgment Number:** (32bit) Three-way handshake esnasında iletişim kurarken hangi mesajlara cevap verildiğini takip etmek için kullanılan sayılar. Cevap +1 yapılarak ve yeni bir sayı verilerek geri yollanır. Yeni sayı sequence number'a eklenir. +1 yapılan sayı ancknowledgment number kısmına eklenir.

**- Header Length:** (4bit) Tcp header'in uzunluğunun belirtildiği kısım.

**- Code Bits:** (6bit) Gönderilen paketlerin cinsini belirttiğimiz kısım. örnek (istek yollama paketi, cevap paketi, acil vs.)

**- Window Size:** (16bit) Makinelerin karşı tarafa kapasitesini belirtmek için kullandıkları kısım.

  * Three-way Handshake Örneği: 
  
    A => syn + x(sequence)
    
    B => syn + ack(x+1) + y(sequence)
    
    A => ack(y+1) + z(sequence)

###### Notlar

**- Wireshark:** OSI katmanlarındaki veri 2.katmandan direk wiresharka yönlendirilerek veriyi katmanlardan geçmeden önce izlemeyi sağlayan program. Bu sayede gönderdiğimiz ve aldığımız paketleri detaylıca gözlemleyebiliyoruz.

- ->Ethernet / Layer 2 => IP / Layer 3 => ICMP 

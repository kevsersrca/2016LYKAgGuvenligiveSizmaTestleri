#Tcpdump

Tcpdump Linux/UNIX sistemlerde  paket yakalama ve analiz aracıdır. Tcpdump pcap paket yakalama kütüphanesini(libpcap) kullanır
 ve ağ arabiriminden geçen paketleri (TCP/IP protokollerini) kaydedip, pcap destekli herhangi bir araç kullanarak kaydedilmiş paketleri  okuma işine yarar.  


Özellikle ağ üzerinden yakaladığı paketleri pcap formatındaki sniffer araçlarının 
okuyabileceği formatta kaydetme özelliği, yoğun trafiğe sahip ağlarda sorunsuz paket 
yakalama becerisi tcpdump’ı ağ güvenliği yöneticilerinin vazgeçilmezi kılmaktadır. 

##Komut örnekleri

                   tcpdump


Ağ trafiğini analiz eder.  


                   tcpdump -D

Ağ üzerinde dinlenebilecek bütün arayüzleri listeler. 


                   tcpdump -i +arayüz adı+

Belirtilen arayüzü dinler ve analiz eder.

                    tcpdump –c  +sayı+


Belirtilen sayıda paket içeriğini listeler. 

                    tcpdump –n port +port numarası+


Hedef veya kaynak portu belirtilen port olan paketleri listeler. 

                    tcpdump –v icmp  
                 
                 
ICMP paketlerini listeler. 

                    tcpdump –w  “dosya ismi”
                    
Listelenen paketleri bir dosya halinde kaydeder. Bu kaydettiğimiz dosyayı ‘Wireshark’ gibi programlarla da açarak inceleyebiliriz.


                    tcpdump –r   “dosya ismi”    
                    
                    
Dosya halinde olan bir paket listesini açar.







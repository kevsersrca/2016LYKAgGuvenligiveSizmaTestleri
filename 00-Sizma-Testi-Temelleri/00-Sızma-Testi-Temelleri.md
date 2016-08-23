## Sızma testi nedir?

- Bir saldırgan profilinin en yakın haliyle sistemin zafiyetlerini tespit edip, bu zafiyetlerin risk haritasını çıkararak çözüm önerilerinde bulunulması hizmetine sızma testi denir.
- Bir saldırgan ile bir pen. tester arasında üç temel fark vardır. Bunlar: kapsam, motivasyon ve zamandır.
- Saldırgan herhangi bir kapsam(sınır) tanımazken pen. tester hedef ile anlaştığı kapsamlar içerisinde çalışır. 
- Her ikisinin de motivasyonları farklıdır. 
- Saldırgan zaman konusunda sıkıntı yaşamaz. Pen. tester ise belirli bir süre içerisinde vereceği hizmeti tamamlar. Bu zaman dilimini müşteri ve pen. tester ortak belirler.
- Müşteri günün sonunda zafiyetlerinin raporlanmasını bekler. Ayrıca bir saldırgan için tek bir zafiyet yeterli olabilir ancak pen. tester sistemi tamamen taramalıdır.
- Her sızma testi sonucunda ortaya illa çok kritik zafiyatlar çıkacak diye bir kural yok. Bu pen. tester için işin handikapıdır.


## Sızma Testi Çeşitleri

**1. Black Box:** Test edilen kurumun size hiçbir bilgi vermediği test türüdür. Kapsam size aittir. Dışarıdan bir saldırganın verebileceği hasar simüle edilir.

**2. White Box:** Kurumun bize gerekli bilgileri sağladığı test türüdür. Yüksek yetkilere sahip birisinin verebileceği hasar simüle edilir.

**3. Gray Box:** White Box ve Black Box arası bir test türüdür. Bazı bilgiler verilir. Black Box'a kıyasla maliyet azalır. Düşük yetkilere sahip birisinin verebileceği hasar simüle edilir.


## Genel Kavramlar
**- Zafiyet:** Bir sistemin ihtiyacı karşılamak üzere yapılmış tasarımının dışında işleri yapabilmenizi sağlayan aksaklıklıklara zafiyet denir. Her zafiyet 1-5 arasında derecelendirilir. Bu derecelendirme zafiyetin size olası etkileri baz alınarak belirlenir.

**- Tehdit:** Zarar verebilecek kişi, şahıs veya bot(?)

**- Risk:** Tehdit ve zafiyetin kesiştiği noktadır.

**- Exploit:** Sömürme. Zafiyeti sömürmek için gönderdiğin kod. 

**- Payload:** Exploit ile kontrolü elde edilen şeylerin kontrolü ele alındıktan sonra yapılan ve yapılabilecek işlemlere denir.

**- Penetration test:** Hacking işleminin teknik aşamalarını kapsayan sürecin genel adıdır.

**- Vulnerability/Security Assessment:** Sızma testinin bir aşamasıdır.

**- Security Audit:** Hedefin güvenlik seviyesinin olması gereken seviyede olup olmadığını değerlendirmektir.

**- Hacking:** Bir sistemi doğası dışında çalıştırabilme kabiliyetine hacking denir.

**- Ethical Hacking:** Tespit edilen zafiyetin sistemi geliştirmek için kullanılmasına Ethical Hacking denir.


## Penetrasyon Testi Türleri 

1. Network Pen. Test
2. Mobile Pen. Test
3. Web Pen. Test
4. Scada Pen. Test (Embedded(Gömülü) Systems)
5. Wireless Pen. Test
6. Social Engineering
7. Dos/DDos/Loadtest


## Soru-Cevap

- Wireless neden Network'e dahil değil?

  * Wireless ortamında network olmak zorunda mı? Bluetooth?

- SQL Injection hangisine dahil?

  * Web geliştirme için kullanılan bir araç olduğundan web pen. test kategorisine girer.


###### Notlar

- Bazen istemciler e-mail yolladıkları zaman, e-maili yollayan makinenin lokal IP adresini de, e-maili yollayan hakkındaki bilgiler kısmına eklerler.

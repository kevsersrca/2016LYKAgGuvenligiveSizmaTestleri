## Metadolojiler

- İzlenilecek olan yöntemleri belirli bir standarta oturtmak için oluşturulmuş tanımlama sistemi.


## Pen. test sürecinde kullanılan bazı metadolojiler

**1. OSSTMM**

**2. Nist 800-115(National Institute of Standards)**

**3. OWASP testing guide**

**4. Penetration Testing Framework**

**5. ISSAF (Information System Security Assessment Framework)**

**6. PTES (Penetration Testing Execution Standart)**

**7. PCI(Payment Card Industry) Penetration Testing Guide**


## Pen. test rapor formatı

**1. Executive Summary(Yönetici Özeti):** Teknik anlamda bilgi vermeyip, riskin geneliyle ilgili bilgilerin yer aldığı kısım.

**2. Introduction(Giriş):** Anlaşmanın kimler arasında yapıldığı, ne zaman başlandığı, kapsam, raporlama süresi vs. bilgilerin bulunduğı kısım.

**3. Methodology(Metodoloji):** Testin hangi yöntemler kullanılarak gerçekleştiğini anlatan kısım.

**4. Findings(Bulgular):** Tehdit seviyeleri belirtilir.
-Critical
-High
-Medium
-Low
-Info

**5. Conclusion(Sonuç):** Özet.

**6. Appendings(Ekler):** Bazı bulguların açıklamasına referans verdiğiniz kısımdır.


## Soru-Cevap

- Scope(kapsam) nasıl belirlenir?

  * Test yapılacak hedef hakkında bazı bilgiler öğrenildikten sonra çalışılan ortam, sistemin türleri, kullanılan teknolojiler öğrenilip belli bir profil çıkartılır. (Blog, e-ticaret sitesi, banka sitesi).Scope'da bu profile göre çizilir.

- Pen. test iş süreci?

  * Kurumla anlaşırken NDA(Bilgi gizliliği anlaşması) imzalanır. Sonrasında testin kapsamının ortaya çıkarılması için test edilecek ortam hakkında bilgi alış-verişi yapılır. Ardından maliyet ve süre hesaplanır ve teklif yapılır. Kapsam(scope) belirlenir. İzin kağıdı alınır(hapse girmenizi önleyecek olan kağıt).
  
- Raporlama süreci nasıl işler?

  * Bulunan zafiyetler hedefe raporlanır. Ardından hedef bu zafiyetleri kapattığını belirttikten sonra aynı zafiyetler kullanılarak tekrar hackleme işlemi denenir. Eğer kapanmamışsa kapanana kadar zafiyet tekrar raporlanarak bu süreç devam eder. Zafiyetler kapandıktan sonra iş biter.
  

###### Notlar

- Parolalar hakkında yapılan tablo rapor aşamalarından 1,2 veya 6.aşamaya dahil edilir.

- Rapor teslim edildikten sonra karşı tarafın aksiyon alması için 10-15 gün beklenir.

- Rapor çat diye yollanmaz. Rapor şifrelenir. Şifrelendikten sonra yollanır. Şifre de ayrı bir kanaldan yollanır. (NDA anlaşması gereği gizlilik kurallarını ihlal etmemek için) Ayrıca rapor belli bir süre(anlaşmada belirlenen) sonra silinir.

- Testler tek seferlik değil, belli süre aralığında tekrar tekrar yapılıyorsa rapor her test için ayrı ayrı yollanmak yerine süreç bittiğinde toplu olarak yollanabilir. Ayrıca tam tersi olarak, eğer çok kritik bir zafiyet bulunduysa sadece o zafiyeti özetleyen tek sayfalık bir rapor da acil olarak yollanabilir.

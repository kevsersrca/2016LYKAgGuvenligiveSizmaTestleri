## Kriptoloji

**- Kriptoloji:** Şifre bilimidir. Bir veriyi güvensiz bir ortamda bir uçtan diğer uca şifrelenerek iletilmesi ve iletilmiş verinin alıcı tarafından deşifre edilmesini inceler.

 * **- Plain-Text:** Açık (şifrelenmemiş) metin.
 * **- Cipher-Text:** Kapalı (şifrelenmiş) metin.
 * **- Secret Key:** Şifrelenme işleminin kurallarını belirten anahtar. 

**- Ceasar Chiper:** Kaydırmalı şifrelemedir. Mesela "Deneme" kelimesi 3 sağa kaydırılarak "Dhqhph" olarak şifrelenir.

  * Mono Alphabetic Substitution Ciphers ailesinde bulunur.

  * Ceasar'ın Zafiyetleri:
    * Verilen Kelimenin uzunluğu belli
    * Tekrar eden harfler. "deneme" kelimesi için bütün "e" harfleri "h" olarak şifrelenmiştir.
    * Büyük-Küçük harfler belli
  
  * Ceasar Chiper frekans analizi ile çözülür. 
  
**- Frekans Analizi:** Şifrede en sık geçen karakter bulunur. En sık kullanılan harfler olarak denenir. Daha sonra ikili frekans analizine bakılır. Örnek: İngilizce TH yi çok sık kullanır (the, those, there...). Mono Alpha. Subs. Chipers algoritmaları ile şifrelenen metinlerin çözümlemesinde kullanılır.

  ***Frekans Analizi Aracı:*** http://quipqiup.com/

**- XOR Şifreleme:** Plain Text metin ile aynı boyutta bir secret key ile XOR'lanması ile gerçekleştirilir. Alıcı tarafında tekrar çözümlenirken aynı secret key ile tekrar XOR işleminden geçirilir.
  
  S ⊕ P ⊕ S = P => S ⊕ P = C ----> C ⊕ S = P
  
  * XOR Şifrelemenin Problemi: Aynı Secret Key'in birden fazla Plain Text mesaja uygulanması.
  
    P2 ⊕ S = C2 (aynı Secret key ile şifrelenmiş P2 metni)
    P7 ⊕ S = C7 (aynı Secret key ile şifrelenmiş P7 metni)
    Eğer ortaki adam şifrelenmiş C2 ve C7 metinlerini ele geçirirse ve birbiri ile XOR işlemi yaparsa;
     C2 ⊕ C7 = (P2 ⊕ S) ⊕ (P7 ⊕ S) = (P2 ⊕ S ⊕ S) ⊕ P7 = (P2 ⊕ 0) ⊕ P7 = **P2 ⊕ P7** --> P2 ve P7 metinlerinin üst üste gelmiş halini tespit etmiş olur.

**- Symmetric Encryption:** Tek anahtarlı şifrelemeye dayanır. Sadece secret key'i vardır.

 * DES (Data Encryption Standard)
 * 3DES (Triple DES)
 * AES (Advanced Encryption Standard)

  ***-Known Plain-text Attack:*** Plain-text'in bir kısmının çözülmesi halinde bütün plain-text'i çözen saldırı. Alan Turing (Film: The Imitation Game, Başrol: Benedict Cumberbatch)
 
 

**- Asymmetric Encryption:** Çift anahtarlı şifrelemeye dayanır. Public ve Private Key olarak iki anahtar kullanılır. Private key'in hiçbir zaman iletimi yapılmaz.

 * **Diffie & Hellman Key Exchange Algorithm**
 * DSA (Digital Signature Algorithm)
 * RSA (Ron **R**ivest, Adi **S**hamir,Leonard **A**dleman Encryption Algorithm)
 * ECDSA (Elliptic Curve Digital Signature Algorithm)


**- HASHING:** Verinin geri dönülemez biçimde özetinin alınmasıdır. Dosya doğrulama, şifre saklamada kullanılır.

 **Bazı Hash Fonksiyonları:**

  * ***MD5:*** 32 bit uzunluğundadır. 0-9 ve a-f arası 16 karakterle özetleme işlemi yapılır. 
    16^32 farklı MD5 hashi bulunur, bu da bir MD5 hashinin 1/16^32 olasılıkla tahmin edilebileceğini gösterir.

  * ***SHA-1:*** 40 bit uzunluğundadır. 16 karakter kullanılarak oluşturulur.
    Bir SHA-1 hashi 1/16^40 olasılıkla tahmin edilebilir.
  * ***SHA-256:*** 256 bit uzunluğundadır. 16 karakter kullanılarak oluşturulur.
    Bir SHA-256 hashi 1/16^256 olasılıkla tahmin edilebilir.
  * ***SHA-512:*** 512 bit uzunluğundadır. 16 karakter kullanılarak oluşturulur.
    Bir SHA-512 hashi 1/16^512 olasılıkla tahmin edilebilir.

   ***MD5 Collusion Attack:*** Sonsuz veri uzayı içerisinde 16^32 MD5 hashi kullanılıyor. İki farklı verinin hashleri aynı olabilir.
  
   ***Hash'lerin uzunlukları arttıkca kırılması o kadar zorlaşır. MD5 fonksiyonu çok hızlı olduğu için kırılması daha kolaydır.***

  **Rainbow Attack:** Hacklenen kurumlardan elde edilen parolalar Rainbow table adı verilen yönlemle internet üzerinde hash veritabanlarında yayınlanır (DUMP) . Bu Rainbow Table'larda parolalar ve o parolaya ait tüm hashleriyle birlikte tutulur. Bu rainbow table'lar kullanılarak bir hashin parola karşılığına çok çabuk ulaşılabilir.
  
  ***Bazı Hash Veritabanları:***
   * https://crackstation.net/
   * http://project-rainbowcrack.com/table.htm
   * http://www.pwcrack.com/rainbowtables.shtml
   * https://hashkiller.co.uk/
   * http://www.md5online.org/
   * https://hashtoolkit.com/
   * http://www.cmd5.org/
   



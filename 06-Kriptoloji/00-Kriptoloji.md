## Kriptoloji

**- Kriptoloji:** Şifre bilimidir. Bir veriyi güvensiz bir ortamda bir uçtan diğer uca şifrelenerek iletilmesi ve iletilmiş verinin alıcı tarafından deşifre edilmesini inceler.

 * **-Plain-Text:** Açık (şifrelenmemiş) metin.
 * **-Cipher-Text:** Kapalı (şifrelenmiş) metin.
 * **-Secret Key:** Şifrelenme işleminin kurallarını belirten anahtar. 

**- Ceasar Chiper:** Kaydırmalı şifrelemedir. Mesela "Deneme" kelimesi 3 sağa kaydırılarak "Dhqhph" olarak şifrelenir.

  * Mono Alphabetic Substitution Ciphers ailesinde bulunur.

  * Ceasar'ın Zafiyetleri:
    * Verilen Kelimenin uzunluğu belli
    * Tekrar eden harfler. "deneme" kelimesi için bütün "e" harfleri "h" olarak şifrelenmiştir.
    * Büyük-Küçük harfler belli
  
  * Ceasar Chiper frekans analizi ile çözülür. 
  
**- Frekans Analizi:** Şifrede en sık geçen karakter bulunur. En sık kullanılan harfler olarak denenir. Daha sonra ikili frekans analizine bakılır. Örnek: İngilizce TH yi çok sık kullanır (the, those, there...). Mono Alpha. Subs. Chipers algoritmaları ile şifrelenen metinlerin çözümlemesinde kullanılır.

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







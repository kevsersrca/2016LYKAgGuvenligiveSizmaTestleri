## Zafiyet Tespitleri

**- Tools:** Nessus, OpenVAS(open-source)

## Nessus

  => /etc/init.d/nessusd start (nessus'u başlatır)

  => netstat -lntup (8834 port'unun ayakta olup olmadığını kontrol ederek nessus'un çalışıp çalışmadığını kontrol edebiliriz)

  B> https://localhost:8834/ adresinden Nessus'a girebiliriz.

**- Nessus Kullanımı:**

**- Politika (Policy):** Taramalar için politikaların oluşturulduğu kısımdır. Politikayı kendimiz oluşturabilmek için Advanced Scan'ı seçmemiz gerekir.

**- Tarama (Scan):** Hedeflerin belirlendiği ve taramanın başlatıldığı kısımdır.

**- Nessus Remediations:** Basit çözüm önerilerinin bulunduğu sekme.

**- Nessus Vuln.s/Vuln. Info:** Bulunan zafiyetle ilgili exploit bilgilerinin bulunduğu kısım.

## OpenVAS

  B> https://localhost:9392/  (username: admin, password: kurulum bittiğinde terminal'de veriyor.)

###### Notlar

* Nessus'un kurulu olduğu dizin => /opt/nessus/

* Tool'lar zafiyetleri her ne kadar güzelce raporlasada, rapordaki zafiyetleri tek tek incelemek gerek. Info olarak gösterilen bir zafiyet aslında kritik olabilir.

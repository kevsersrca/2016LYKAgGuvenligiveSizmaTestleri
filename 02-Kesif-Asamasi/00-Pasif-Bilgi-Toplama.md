## Reconnaissance (Bilgi Toplama)

## Pasif Bilgi Toplama (OSINT) (Açık Kaynak İstihbaratı)

**- Senaryo:** Black Box pen.test isteniyor:

**- Yapacağımız ilk iş:** Hedefin IP adresini öğrenmek. Bazı yöntemler:

    => ping ankara.edu.tr

    => nslookup

      => server 8.8.8.8

      => www.ankara.edu.tr

**- ICANN:** Bütün dünyadaki IP adreslerinin dağıtılmasını organize eden kurumdur. 

**- RIPE:** Avrupadaki IP adreslerini aratabileceğimiz servis.

  - www.ankara.edu.tr için elde ettiğimiz IP adresini RIPE içerisinde aratıyoruz. Elde ettiğimiz net-name'i tekrar RIPE'de aratarak başka bilgilere de ulaşabiliriz.

**- Başka yöntemler:**

    B> www.who.is ankara.edu.tr (tr uzantılarda çalışmıyor?)
    
    B> ipinfo.io (arama servisi)

**- Subdomain tespiti:** 

    B> Google üzerinden site:*.ankara.edu.tr şeklinde arama yaparsak subdomainlere ulaşabiliriz.
    
    Ayrıca bazı araçlar da bize subdomainleri listeler.
    
      => fierce -dns ankara.edu.tr
      => theharvester -d ankara.edu.tr -b all
      => dnsmap ankara.edu.tr

**- Hedefe ait virtualhost'ların tespiti:** 

    B> bing.com arama motorundan IP:x.y.z.a şeklinde arama yaptığımızda virtualhost'lara ulaşabiliriz.
    
    Ayrıca bazı araçlar da bize subdomainleri listeler.
        => dig -x <IP>
        => nslookup <IP>

**- Hedefe ait e-mailler:** 

    => theharvester -d ankara.edu.tr -b bing
    Bu mail adresleri kullanılarak çeşitli sosyal mühendislik saldırıları yapılabilir.

**- Hedefe ait indirilebilir dosyalar:** 

    B> google B> filetype:pdf ankara.edu.tr
    
    B> = FOCA
    
    => metagoofil (stabil değil)

**- Lokasyon tespiti:** 

    B> ipinfo.io, ip2location.com, whois.domaintools.com (IP adresini aratarak)

**- Reverse whois:** IP adresi veriyoruz. Bu IP adresine ait bilgilere ulaşıyoruz. Kullanılabilir siteler: whois.com (sansürlü, güncel), viewdns.info (sansürsüz, eski)

**- Netcraft:** B> www.netcraft.com : Hedefin kullandığı işletim sistemini öğrenebiliriz. Örnek: eğer eski bir apache serveri kullanılıyorsa versiyonuna ait bazı zafiyetlere sahip olabilir. Bu zafiyetler kullanılabilir. Veya B> http://whois.domaintools.com/ sitesinden de öğrenilebilir.

**- Shodan:** B> www.shodan.io : Bilgi toplamak için gelişmiş bir arama motoru. Parametreler: hostname:ankara.edu.tr, country:tr Alternatif siteler: zoomeye, censys.io(lokasyon + port bilgisi de var)

**- FOCA:** Hedefe ait indirilebilir bütün veya bazı dosyaları düzenli bir şekilde indirip analiz edebilmemizi sağlayan tool. Metadata analizleri sayesinde bir çok bilgi elde edilebilir. Sadece windows'da çalışıyor :(

**- Robtex:** B> www.robtex.com : Sorgulanan sitenin DNS network'ünü şema halinde gösteren servis.

**- Google üzerinden keşif işlemleri:** Google filtreleri hakkında detaylı bilgiler 

    B> https://www.exploit-db.com/google-hacking-database/ 
    
    B> www.google.com
    
      B> site:*.ankara.edu.tr

**- Hedefe ait giriş panellerinin tespiti:** 
    
    B> www.google.com 
    
      B> inurl:login site:*.ankara.edu.tr

**- Dump:** Kötü niyetli kişiler tarafından bir database'in patlatılarak bilgilerin internette herkese açık olarak yayınlanması.

**- Hedef domaine benzer domainlerin tespiti:** Kullanıcı yazım hatası yapıp fark etmeyerek, hedef domaine benzer bizim aldığımız domain'e girebilir.

    => urlcrazy -r ankara.edu.tr

**- Alexa analizi:** B> www.alexa.com : Domain'ler hakkında istatiksel bilgiler tutan bir servis.

**- İş ilanları analizi:** Bazen araştırılan hedef, kendisi hakkında donanım/yazılım bilgilerini iş ilanlarında paylaşmış olabilir.

**- Archive.org analizi:** B> archive.org : İnternet sitelerinin eski belgelerinin yer alıyor olabileceği bir servis. Bağımsız ve kar amacı gütmüyor.

**- Sosyal medya hesaplarının analizi:** Facebook'da paylaştığı fotoğraf bir çok bilgi verebilir. Örnek: Bilgisayarın ekran görüntüsü atmış olabilir. Kritik bir bilgi elde edebiliriz. (veriden veri üretme) (fotoğraftan parmak izi çıkartan adam örneği)

**- Kaynak kod ve geliştirici firma analizi:** Bir websitesinin kaynak kodları incelenerek bilgi elde edilebilir.

**- Çalışanların geliştirici siteleri analizi:** Hedef kurumdaki çalışanların github hesaplarından bilgi elde edilebilir.

**- Pastebin üzerinden bilgi toplama:** B> www.pastebin.com : Dump'ların vs. paylaşıldığı bir site. 
    
    B> www.google.com 
    
      B> site:pastebin.com intext:"password"

**- Finans araştırması:** Hedefe göre değişir. 

**- Cloudflare:** Firewall servisi. Websitelerine IP değiştirme, bilgileri gizleme, ddos savunmaları gibi hizmetler veriyor. Örnek: www.osman.com bu adresi cloudflare koruyor. Ama subdomainler açıkta kalır.

###### Notlar

  - Saldırmadan önce bulabildiğimiz her şeyi toplamaya çalışacağız.
  - OSINT için güzel bir örnek :) : https://eksisozluk.com/entry/47201385

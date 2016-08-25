#Tünelleme:

-ip | icmp | ip | tcp (örnek paket)

-Tünelleme ICMP, DNS, SSH, SSL üzerinden yapılabilir.

-ICMP paketlerini firewall'dan ve internetten bir sunucuya geçirip sunucunun cevap verdiği ICMP paketlerini belirleyip bu paketleri kullanarak o sunucuyla aramızda bir köprü kurma işlemidir.

-DNS ile tünelleme işlemi genellikle daha başarılıdır. Bir web sitesi kendisine gelen isteklere döndüğünde firewall buna izin verir ancak isteği kendisi yolladığında bu istekleri firewall engeller.

-Socket proxy: 

-Re (?) te proxy:

-Local proxy:

    => ssh -D8080 209.208.110.70 -l barkink
    => password
    => netstat -lntup
    => mozilla proxy => socket proxy

    => ssh 209.208.110.70 -l barkink -R 8080:192.168.0.1:80 (remote)

    => ssh 209.208.110.70 -l barkink -L 8080:192.168.0.1:80 (local)

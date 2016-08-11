print "\n|----------Lyk 2016 | aktif bilgi yok cınıms-------------|\n"
import urllib, urllib2, re, sys
host = raw_input("Host : ")
print "\n|---------------------aktif tarama da bizi gorecek mi?-------------------------------|\n"
start = 1
pageCount = 5
checkDomains = []
_s1 = None

header = {'User-Agent':'Mozilla/5.0'}

for i in range(pageCount) :

	url = "https://www.google.com/search?q=site:"+host+"&start="+str(i*10)
	req = urllib2.Request(url, headers=header)
	_r = urllib2.urlopen(req).read()

	domains = re.findall('<cite>(.*?)</cite>', _r)

	for j in range(len(domains)) :
		_c = 0
		isSubDom = re.findall('(.*?)'+host, domains[j])

		if len(checkDomains) == 0 :
			checkDomains.append(domains[j])

		if isSubDom[0] != "www" :
			for k in range(len(checkDomains)) :
				_s1 = re.search(isSubDom[0], checkDomains[k])

				if _s1 != None :
					_c = 1
					break

			if _c == 0 :
				print domains[j]
				checkDomains.append(domains[j])

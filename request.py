import bs4 as bs
import urllib.request

souce = urllib.request.urlopen("https://en.wikipedia.org/wiki/Article_(grammar)").read()
soup = bs.BeautifulSoup(souce,"lxml")

for paragraph in soup.find_all("p"):
    print (paragraph.text)
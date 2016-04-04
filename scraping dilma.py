import requests
import bs4
from BeautifulSoup import BeautifulSoup
import urllib

url = "http://www2.planalto.gov.br/acompanhe-o-planalto/discursos/discursos-da-presidenta/discurso-da-presidenta-da-republica-dilma-rousseff-durante-cerimonia-de-posse-da-ministra-chefe-da-casa-civil-da-presidencia-da-republica-gleisi-hoffmann"

web = urllib.urlopen(url)
html = web.read()
soup = BeautifulSoup(html)
discurso = soup.find(id="parent-fieldname-text")

print discurso

#for i in soup.select('parent-fieldname-text'):
    #print(i.string)

#with open("discursodilma.txt","wb") as arquivo:
    #arquivo.write(discurso)
    #arquivo.close()
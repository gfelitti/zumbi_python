from BeautifulSoup import BeautifulSoup
import urllib

url = "http://www2.planalto.gov.br/acompanhe-o-planalto/discursos/discursos-da-presidenta?b_start:int=0"
web = urllib.urlopen(url).read()
soup = BeautifulSoup(web)
soup.prettify()

for discurso in soup.findAll("a", href=True):
    print discurso['href']

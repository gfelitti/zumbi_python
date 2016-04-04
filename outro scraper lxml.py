#coding = utf-8
import urllib
import lxml.html
import csv
import unicodedata

discurso = open("discurso.csv", "wb")
writer = csv.writer(discurso)
data =[]
titulo = []
link = []
connection = urllib.urlopen('http://www2.planalto.gov.br/acompanhe-o-planalto/discursos/discursos-da-presidenta?b_start:int=900')
dom = lxml.html.fromstring(connection.read())

acentos = ",./:;,\/[]~`'"
#data
for c in dom.xpath('//span[@class="summary-view-icon"]/text()'):
    data.append(c)

#for row in data: # select the url in href for all a tags(links)
    #row[0] = data
    #writer.writerow(data)

#titulo
for d in dom.xpath('//a[@class="summary url"]/text()'):# select the url in href for all a tags(links)
    titulo.append(d)
#for row1 in titulo:
    #row1[1]= titulo
    #writer.writerow(titulo)

titulo = unicodedata.normalize('NFKD', titulo).encode('ascii', 'ignore')
#links
for e in dom.xpath('//h2[@class="tileHeadline"]//a/@href'):# select the url in href for all a tags(links)
    link.append(e)
#for row2 in link:
    #row[2] = link
    #writer.writerow(link)

#for c in ",./?:;,\/[]{}":
    #titulo = titulo.replace(c, " ")

#f = csv.reader(open('discurso.csv'))
#titulo, link = zip(*f)

#bla = data + titulo + link
#writer.writerow(bla)
#discurso.close()

#for row in f:
  #data.append(row[0])
  #titulo.append(row[1])
  #link.append(row[2])

print titulo
print link
#csv.close()
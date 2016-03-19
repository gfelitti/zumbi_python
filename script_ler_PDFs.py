import sys
import PyPDF2
import os

content = ""
pdf = PyPDF2.PdfFileReader(file("delcidio.pdf", "rb"))
for i in range(0, pdf.getNumPages()):
    content += pdf.getPage(i).extractText() + " \n"
content = u" ".join(content.replace(u"\xa0", u" ").strip().split())

print(content)
#f= open("a.txt","w+")

#f.write(content).encode("ascii","xmlcharrefreplace")
#os.system(("ps2ascii %s %s") %( pdf, f))
#f.close()
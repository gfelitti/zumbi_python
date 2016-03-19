import PyPDF2
PDFobj = open("delcidio.pdf", "rb")
PDFreader = PyPDF2.PdfFileReader(PDFobj)
print(PDFreader.numPages)
pageObj = PDFreader.getPage(4)
print(pageObj.extractText())

#print("amor")
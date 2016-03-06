import string
import sys

if (len(sys.argv) > 1):
   bookname = sys.argv[1]
else:
   bookname = 'ulysses'

file = open('lemann.rtf','r')
txt = file.read()
file.close()

include = set(string.punctuation)

def getPunctuation(s):
   return ''.join(ch for ch in s if ch in include)

punct = getPunctuation(txt);

# file = open('blood-punct.txt','w')
file = open('lemann-punct.txt','w')
file.write(punct)
file.close()

print(len(punct))
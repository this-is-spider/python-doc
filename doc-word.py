from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
# print(xml_content.decode('utf-8'))
wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'lxml')
# print(wordObj)
textStrings = wordObj.find('w:t')
print(textStrings)
for textElem in textStrings:
    print(textElem)

# find可以找到，find_all方法就找不到，不知道为什么
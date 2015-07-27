
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getPics(html):
    reg = r'src="(.+?\.jpg)"  ' 
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

html = getHtml("http://tieba.baidu.com/p/3921138400")
html = html.decode('utf-8')
data=getPics(html)
count=0
for a in data:
    count+=1
    path="c:/test/"+str(count)+".jpg"
    urllib.request.urlretrieve(a, path)


print (data)
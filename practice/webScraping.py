import requests
from bs4 import BeautifulSoup
r = requests.get('https://studio-onto.com/')
print(r)
soup = BeautifulSoup(r.content, 'html.parser')
code=soup.prettify()
f=open(r"D:\BEBO-tech\Selenium\Selenium\practice\onto.html",'w', encoding="utf-8")
f.write(code)
f.close()
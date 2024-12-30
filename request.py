# from requests import requests
import requests

# import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serviceObj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr = webdriver.Chrome(service=serviceObj)
dr.get("http://www.deadlinkcity.com/")
allLnks=dr.find_elements(By.TAG_NAME,"a")
f1=open("linkData.txt",'a')
c=0
a=0
for i in allLnks:
    url=i.get_attribute("href")
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        # print("link is broken")
        c+=1
        f1.write(f"broken:{c} code is : {res.status_code}\n")
    else:
        a+=1
        f1.write(f"active:{a} code is : {res.status_code}\n")
        # print("link is working")

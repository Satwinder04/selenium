import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("http://www.automationpractice.pl/index.php")
# signup

h1=dr.find_element(By.TAG_NAME,"h3").text
print(h1)
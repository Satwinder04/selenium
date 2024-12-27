import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("http://www.automationpractice.pl/index.php")
# signup
dr.find_element(By.LINK_TEXT,"Contact us").click()
time.sleep(5)
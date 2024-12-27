import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr = webdriver.Chrome(service=serviceObj)
dr.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(4)
act=dr.find_element(By.XPATH,"//*[@id='content']/div/p").text
ext="Congratulations! You must have the proper credentials."

if act==ext:
    print("test pass")
else:
    print("failed")
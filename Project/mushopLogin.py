import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
time.sleep(5)

lEmail=dr.find_element(By.ID,"email")
lEmail.send_keys("satwinder@gmail.com")
time.sleep(5)

lpass=dr.find_element(By.ID,"passwd")
lpass.send_keys("test1")
time.sleep(5)
dr.find_element(By.ID,"SubmitLogin").click()
time.sleep(10)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
# signup

sEmail=dr.find_element(By.CLASS_NAME,"is_required")
sEmail.send_keys("satwinder@gmail.com")
time.sleep(3)

dr.find_element(By.ID,"SubmitCreate").click()
time.sleep(3)
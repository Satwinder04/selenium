import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("https://www.facebook.com/")
time.sleep(2)

lEmail=dr.find_element(By.XPATH,"//*[@name='email'and@id='email']")
lEmail.send_keys("satwinder@gmail.com")
time.sleep(2)

lpass=dr.find_element(By.XPATH,"//*[@name='pass'or@id='pass']")
# lpass=dr.find_element(By.ID,"pass")
lpass.send_keys("test1")
time.sleep(2)
# dr.find_element(By.CSS_SELECTOR,"a[role=button]").click()
# time.sleep(2)
# dr.find_element(By.XPATH,"//button[text()='Log in']").click()
# time.sleep(3)
dr.find_element(By.XPATH,"//a[starts-with(text(),'Forgotten')]").click()
time.sleep(5)

print("test pass")


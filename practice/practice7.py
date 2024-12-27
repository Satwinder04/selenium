import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr = webdriver.Chrome(service=serviceObj)
dr.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)
chks=dr.find_elements(By.XPATH,"//*[@type='checkbox']")

for i in chks:
    if i.is_selected():
        i.click()
time.sleep(3)
for j in chks:
    j.click()
time.sleep(3)

for j in chks:
    j.click()
time.sleep(3)

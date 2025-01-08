import time

from selenium import webdriver
from selenium.webdriver.common.by import By

dr=webdriver.Chrome()
dr.get("https://www.rapidtables.com/tools/click-test.html")

testtime=dr.find_element(By.XPATH,"//input[@id='timer']").text

strt=time.time()

while time.time()-strt<5:
    # dr.find_element(By.XPATH,"//button[@id='addbtn']").click()
    dr.find_element(By.XPATH,'//*[@id="addbtn"]').click()
clickPerSec=dr.find_element(By.XPATH,"//input[@id='cps']").text
print(clickPerSec)
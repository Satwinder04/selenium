import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serviceObj)
driver.get("http://www.automationpractice.pl/index.php?controller=contact")
driver.find_element(By.ID, "id_contact").click()
option=driver.find_elements(By.TAG_NAME,"option")
option[2].click()
time.sleep(2)

cEmail=driver.find_element(By.ID,"email")
cEmail.send_keys("satwinder@gmail.com")
time.sleep(2)

orderReference=driver.find_element(By.ID,"id_order")
orderReference.send_keys("12345")
time.sleep(2)

cMessage=driver.find_element(By.ID,"message")
cMessage.send_keys("hello this is test case one")
time.sleep(2)

cSend=driver.find_element(By.ID,"submitMessage")
cSend.click()
time.sleep(2)



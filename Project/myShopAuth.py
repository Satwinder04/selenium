import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
# signup

sEmail=dr.find_element(By.ID,"email_create")
sEmail.send_keys("satwinder@gmail.com")
time.sleep(3)

dr.find_element(By.ID,"SubmitCreate").click()
time.sleep(3)

# --------------------
sGender=dr.find_elements(By.NAME,"id_gender")
sGender[0].click()
time.sleep(3)

sName=dr.find_element(By.ID,"customer_firstname")
sName.send_keys("Satwinder")
time.sleep(3)

lName=dr.find_element(By.ID,"customer_lastname")
lName.send_keys("Singh")
time.sleep(3)

ssEmail=dr.find_element(By.ID,"email")
ssEmail.send_keys("satwinder@gmail.com")
time.sleep(3)

ssPassword=dr.find_element(By.ID,"passwd")
ssPassword.send_keys("test1")
time.sleep(3)

# days=dr.find_element(By.ID,"days")


Register=dr.find_element(By.ID,"submitAccount")
Register.click()

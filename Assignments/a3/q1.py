import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

dr=webdriver.Chrome()
dr.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
s=time.time()
dr.find_element(By.ID,"name").send_keys("Satwinder Singh")
dr.find_element(By.ID,"email").send_keys("abc@gmail.com")
dr.find_element(By.ID,"gender").click()
dr.find_element(By.ID,"mobile").send_keys("123456789")
dr.find_element(By.ID,"subjects").send_keys("python")
dr.find_element(By.ID,"dob").send_keys("04112001")
dr.find_element(By.ID,"subjects").send_keys("python")
dr.find_element(By.ID,"hobbies").click()
# dr.find_element(By.XPATH,'//*[@id="picture"]').send_keys("2134567 st no.123")
dr.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[9]/div/textarea").send_keys("2134567 st no.123")
state=Select(dr.find_element(By.ID,"state"))
op=state.options
for i in op:
    if i.text=="NCR":
        i.click()

city=Select(dr.find_element(By.ID,"city"))
opc=city.options
for j in opc:
    if j.text=="Agra":
        j.click()
e=time.time()
t=e-s
print(f"exicution time is : {t}")

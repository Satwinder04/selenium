import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=sobj)
driver.get("http://www.automationpractice.pl/index.php")
driver.find_element(By.XPATH,"//*[@class='_blank']").click()
time.sleep(2)

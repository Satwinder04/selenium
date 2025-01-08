import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.filemail.com/")
fileUpload=driver.find_element(By.XPATH,'/html/body/div[2]/div/main/div/section[2]/div/div[1]/div/div/input')
filPath=r"D:\BEBO-tech\Selenium\Selenium\download\pexels-tessa-m-2148132609-29935806.jpg"
time.sleep(3)
fileUpload.send_keys(filPath)
time.sleep(3)
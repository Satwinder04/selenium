import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# ops=webdriver.ChromeOptions()
# ops.add_argument("--disable--notification--")
dr=webdriver.Chrome()
dr.get("https://whatmylocation.com/")
dr.find_element(By.XPATH,'//*[@id="copy_loc"]').click()
time.sleep(10)
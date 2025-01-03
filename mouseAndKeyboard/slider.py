import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
action=ActionChains(driver)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")

mn=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
mx=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
print("before",mn.location)
print("before",mx.location)

action.drag_and_drop_by_offset(mn,100,0).perform()
action.drag_and_drop_by_offset(mx,-34,0).perform()
print("after",mn.location)
print("after",mx.location)

time.sleep(4)
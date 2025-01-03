import os
# import time

from selenium import webdriver
# from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.get_screenshot_as_file(os.getcwd()+"//home.png")
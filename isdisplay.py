# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# # img=dr.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[1]/a/img").is_displayed()
# # print(img)
# male=dr.find_element(By.ID,"gender-male")
# print(male.is_selected())
# male.click()
# print(male.is_selected())
# print(male.is_enabled())
# dr.close()

#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
#
#
# service_obj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.google.com/")
#
# textbox = driver.find_element(By.NAME, "q")
# textbox.send_keys("flipkart.com")
#
#
# textbox.send_keys(Keys.RETURN)  # Simulate pressing Enter
# driver.find_element(By.XPATH,"//*[@id='ixcYae']/div/div/div/div/div/div/div[1]/div/span/a").click()
# driver.back()
# driver.forward()
# time.sleep(6)
# # Close the browser
# driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# img=dr.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[1]/a/img").is_displayed()
# print(img)
male=dr.find_element(By.ID,"gender-male")
print(male.is_selected())
male.click()
print(male.is_selected())
print(male.is_enabled())
dr.close()
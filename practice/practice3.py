# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://python.org/")
# # sz=dr.get_window_size()
# # print(sz)
# # dr.fullscreen_window()
# t=dr.title
# sp=t.split()
# print(sp)
# # print(t)
# # print(dr.current_url)
# # print(dr.page_source)
# keyword='Welcome'
# if keyword in t:
#     print("present")
#

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("https://www.w3schools.com/html/html_forms.asp")
# btn=dr.find_element(By.XPATH,"//*[@id='main']/div[2]/a[2]")
ch=dr.find_element(By.ID,"vehicle2")
# display=dr.find_element(By.ID,"html").is_displayed()
# h=dr.find_element(By.XPATH,"//*[@id='main']/h1").text
# exp="HTML Forms"
# if h==exp:
#     print(True,"coreect")
# print(display)
print(ch.is_selected())
# print(btn.is_enabled())
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(5)
# btn=dr.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[1]")
# btn.click()
# time.sleep(5)
# dr.close()
# time.sleep(5)

# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(5)
# btn=dr.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[1]")
# btn.click()
# time.sleep(5)
# dr.quit()
# time.sleep(5)
#
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://www.selenium.dev/")
# time.sleep(5)
#
# btn=dr.find_elements(By.CLASS_NAME,'selenium-button')
# btn[1].click()
# time.sleep(2)
# dr.back()
# time.sleep(2)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("https://money.rediff.com/gainers")
time.sleep(2)

td=dr.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[8]/td[1]/a/parent::td").text
# print(td)
tdF=dr.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[8]/td[1]/a/parent::td/following::td").text
# print(tdF)
tdfollowing=dr.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[8]/td[1]/a/ancestor::tr[1]/following::tr[1]/td[1]/a").text
print(tdfollowing)

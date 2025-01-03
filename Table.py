# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# dr=webdriver.Chrome()
# dr.get('https://testautomationpractice.blogspot.com/')
# rows=dr.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr')
# cols=dr.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th')
# for r in range(2,len(rows)+1):
#     auth=dr.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[2]').text
#     if auth=="Amit":
#         price=dr.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[4]').text
#         print(price)
# import time

from selenium import webdriver
from selenium.webdriver.common.by import By

dr=webdriver.Chrome()
dr.get('https://testautomationpractice.blogspot.com/')
rows=dr.find_elements(By.XPATH,'//*[@id="taskTable"]/tbody/tr')
cols=dr.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/td')
for r in range(2,len(rows)+1):
    auth=dr.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[2]').text
    if auth=="Amit":
        price=dr.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[4]').text
        print(price)

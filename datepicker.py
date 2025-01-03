# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# dr=webdriver.Chrome()
# dr.get('https://jqueryui.com/datepicker/')
# frm=dr.find_element(By.XPATH,'//*[@id="content"]/iframe')
# dr.switch_to.frame(frm)
# dr.find_element(By.ID,"datepicker").click()
#
# year="2024"
# month="December"
# date="31"
# time.sleep(3)
#
# while True:
#     m=dr.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[1]').text
#     y=dr.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[2]').text
#     if m==month and y==year:
#         break
#     else:
#         nxt=dr.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[2]')
#         nxt.click()
#         # previous=dr.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[1]')
#
# datetable=dr.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr/td')
# time.sleep(3)
#
# for i in datetable:
#     if i.text==date:
#         i.click()
#
# time.sleep(3)
# print(dr.find_element(By.ID,"datepicker").text)
# ================================================================================
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

dr=webdriver.Chrome()
dr.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
dr.find_element(By.XPATH,"//input[@id='departon']").click()
time.sleep(5)
year="2025"
month="Oct"
date="31"
# dr.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[2]').click()
years=Select(dr.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
years.select_by_visible_text(year)
# yop=years.options
# for y in yop:
#     if y.text==year:
#         y.click()
# time.sleep(3)

months=Select(dr.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))
months.select_by_visible_text(month)
# mop=months.options
# for m in mop:
#     if m.text==month:
#         m.click()
time.sleep(3)

tb=dr.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr/td')
for i in tb:
    if i.text==date:
        i.click()
time.sleep(3)



# import time
#
# # from select import select
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://testautomationpractice.blogspot.com/")
# drpdwn=Select(dr.find_element(By.ID,"country"))
# op=drpdwn.options
# for i in op:
#     # print(i.text)
#     if i.text=="India":
#         i.click()
#         break
# time.sleep(5)
#
# chk=dr.find_elements(By.XPATH,"//*[@class='form-check-input' and @type='checkbox']")
#
# # for i in range(len(chk)):
# #     chk[i].click()
# # time.sleep(2)
#
# chk[3].click()
# chk[6].click()
# time.sleep(4)
#
# for i in range(len(chk)):
#     if chk[i].is_selected():
#         chk[i].click()
#         print(chk[i])
# time.sleep(6)



import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


service_obj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.google.com/")

textbox = driver.find_element(By.NAME, "q")
textbox.send_keys("selenium")
c=driver.find_elements(By.CLASS_NAME,"wM6W7d")
for i in c:
    print(i.text)
# textbox.send_keys(Keys.RETURN)

time.sleep(6)
driver.quit()
# Task 2: Handling Checkboxes
import time


# https://the-internet.herokuapp.com/checkboxes
# 1. Write a script to:
# Open a webpage with multiple checkboxes.
# Select all checkboxes on the page..
# 2. Write a script to:
# Open a webpage with specific checkboxes.
# Verify if a checkbox with the label "Accept Terms and Conditions" is selected. If not, select it.
# 3. Write a script to:
# Open a webpage with multiple checkboxes.
# Deselect all selected checkboxes.
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serviceObj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr = webdriver.Chrome(service=serviceObj)
# dr.get("https://the-internet.herokuapp.com/checkboxes")
# time.sleep(2)
# chks=dr.find_elements(By.XPATH,"//*[@type='checkbox']")
#
# for i in chks:
#     if i.is_selected():
#         i.click()
# time.sleep(3)
# for j in chks:
#     j.click()
# time.sleep(3)
#
# for j in chks:
#     j.click()
# time.sleep(3)
#
# Task 3: Handling Dropdowns
# https://www.globalsqa.com/demo-site/select-dropdown-menu/
# https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html
# 1. Write a script to:
# .
# Open a webpage with a dropdown menu.
# Select an option by visible text.
# 2. Write a script to:
# Open a webpage with a dropdown menu.
# Find All Match Case
# words, 1,480 characters
# Default Page Style
# English (India)
#

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# dr=webdriver.Chrome()
# dr.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
# s=Select(dr.find_element(By.TAG_NAME,"select"))
# op=s.options
# f=open("practice/output.txt",'a')
# for i in op:
#     f.write(i.text+'\n')
#
# # for i in range(len(op)):
#
# # s.select_by_value("Panama")
# time.sleep(4)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
dr=webdriver.Chrome()
dr.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")
dr.maximize_window()
s=Select(dr.find_element(By.ID,"course"))
op=s.options
for i in op:
    if i.text=="Java":
        i.click()
time.sleep(4)

s2=Select(dr.find_element(By.ID,"ide"))
op2=s2.options
for j in op2:
    if j.text=="Eclipse":
        j.click()
time.sleep(4)

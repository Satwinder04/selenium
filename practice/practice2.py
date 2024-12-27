# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import element_to_be_selected
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://www.wikipedia.org/")
# dr.find_element(By.XPATH,"//*[@id='search-input']/input").send_keys("Automation testing")
# time.sleep(5)

# ------------------------------------------------------------------------

# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import element_to_be_selected
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://demo.guru99.com/test/newtours/")
# dr.find_element(By.XPATH,"//*[@name='submit']").click()
# time.sleep(5)

# # ------------------------------------------------------------------------
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import element_to_be_selected
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://demo.guru99.com/test/newtours/")
# dr.find_element(By.XPATH,"//*[@href='register.php']").click()
# time.sleep(5)
#
# ------------------------------------------------------------------------

# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import element_to_be_selected
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://www.amazon.in/ref=nav_logo")
# dr.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("laptop")
# time.sleep(5)
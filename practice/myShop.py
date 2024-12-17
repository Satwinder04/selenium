# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("http://www.automationpractice.pl/index.php")
# searchBox=driver.find_element(By.ID,"search_query_top")
# searchBox.send_keys("tshirt")
# time.sleep(2)
# clk=driver.find_element(By.NAME,"submit_search")
# clk.click()
# time.sleep(2)
# clk2=driver.find_element(By.LINK_TEXT,"Faded Short Sleeve T-shirts")
# clk2.click()
# time.sleep(2)
#
# exp='Faded Short Sleeve T-shirts - My Shop'
# act=driver.title
# if exp==act:
#     print("test Pass")
# else:
#     print("test fail")


# ----------------------------------------------------------------------
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("http://www.automationpractice.pl/index.php")
# text1=driver.find_element(By.PARTIAL_LINK_TEXT,"Women").text
# print("the first option is", text1)
# # text2=driver.find_element(By.PARTIAL_LINK_TEXT,"Dresses").text
# # print("the first option is", text2)
# # text3=driver.find_element(By.PARTIAL_LINK_TEXT,"T-shirts").text
# # print("the first option is", text3)
# # text4=driver.find_element(By.PARTIAL_LINK_TEXT,"Blog").text
# # print("the first option is", text4)
#
# -------------------------------------------------------------------
import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("http://www.automationpractice.pl/index.php")
# imgLst=driver.find_elements(By.TAG_NAME,"img")
# print(len(imgLst))

# -------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("http://www.automationpractice.pl/index.php")
# imgLst=driver.find_elements(By.TAG_NAME,"a")
# print(len(imgLst))

# --------------------------------------------------------------------
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("http://www.automationpractice.pl/index.php")
# slider=driver.find_elements(By.CLASS_NAME,"homeslider-container")
# print(len(slider))

# ----------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("http://www.automationpractice.pl/index.php")
# text1=driver.find_elements(By.CLASS_NAME,"sf-menu")
# for i in text1:
#     print("the first option is", i.text)
#
#
# ------------------------------------------------------------------


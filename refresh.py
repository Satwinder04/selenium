# import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
#
# serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr=webdriver.Chrome(service=serviceObj)
# dr.get("https://github.com/Satwinder04")
# for i in range(20):
#     dr.refresh()


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
# p=driver.find_element(By.ID,"search_query_top").get_attribute("placeholder")
# print(p)
# searchBox.send_keys("tshirt")
# time.sleep(2)
# clk=driver.find_element(By.NAME,"submit_search")
# searchBox2=driver.find_element(By.ID,"search_query_top").get_attribute("value")
# # searchBox2=driver.find_element(By.ID,"search_query_top").get_attribute("id")
# print(searchBox2)
# clk.click()
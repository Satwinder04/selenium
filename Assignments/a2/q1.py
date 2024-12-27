import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=sobj)
driver.get("http://www.automationpractice.pl/index.php")
searchBox=driver.find_element(By.ID,"search_query_top")
searchBox.send_keys("search box")
time.sleep(2)
clk=driver.find_element(By.NAME,"submit_search")
clk.click()
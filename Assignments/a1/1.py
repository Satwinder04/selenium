from selenium import webdriver
from selenium.webdriver.chrome.service import Service

sobj= Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome(service=sobj)
driver.get("https://www.amazon.com.") # it will get link of site and open it in automated browser.
exp="Amazon.com" # this expected output
act=driver.title # this is actual outpt which is fatched directly form web page being automated
if act==exp: #it will compare both results
    print("test pass")
else:
    print("test failed")

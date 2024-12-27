import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serviceObj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=serviceObj)
dr.get("https://portfolio-vite-app.vercel.app/")
# dr.get("http://localhost:5173/")
print(dr.title)
print(dr.current_url)
time.sleep(5)
#
# for i in range(1,8):
#     dr.find_element(By.XPATH,f"//p[text()='0{i}']").click()
#     time.sleep(3)
#     print(f"Test case 0{i} Passed")
#     dr.find_element(By.XPATH,"//*[@id='projects']/div/button").click()
#     time.sleep(3)
#     dr.find_element(By.XPATH,"//h1[text()='Rocket']/following::a").click()
dr.find_element(By.XPATH,"//*[@id='contact']/div/div[1]/a[3]").click()
# dr.quit()
print(dr.current_url)
dr.close()
time.sleep(5)

print(dr.current_url)

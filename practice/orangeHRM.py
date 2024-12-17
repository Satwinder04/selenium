import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service_obj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
textbox1=driver.find_element(By.NAME,"username")
textbox1.send_keys("Admin")
time.sleep(5)
textbox2=driver.find_element(By.NAME,"password")
textbox2.send_keys("admin123")
# textbox2.send_keys(Keys.RETURN)
time.sleep(5)
click=driver.find_element(By.LINK_TEXT,"Login")
click.click()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
#
# service_obj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(5)
# textbox1 = driver.find_element(By.NAME, "username")
# textbox1.send_keys("Admin")
# time.sleep(5)
# textbox2 = driver.find_element(By.NAME, "password")
# textbox2.send_keys("admin123")
# textbox2.send_keys(Keys.RETURN)
# time.sleep(5)
#
# driver.quit()

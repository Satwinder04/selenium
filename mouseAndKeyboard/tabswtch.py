import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(4)
winds=driver.window_handles
print(winds)
print(len(winds))
print(type(winds))

for i in winds:
    driver.switch_to.window(i)
    time.sleep(2)
    if driver.title=="Human Resources Management Software | OrangeHRM":
        driver.close()

time.sleep(3)
# # driver.switch_to.window(winds[1])
# time.sleep(3)
# # c=driver.find_element(By.XPATH,"//div[@class='d-flex web-menu-btn']//li[1]//a[1]")
# # c.click()
# print(c.text)
# time.sleep(3)

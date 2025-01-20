import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(1)
textbox1=driver.find_element(By.NAME,"username")
textbox1.send_keys("Admin")
time.sleep(1)
textbox2=driver.find_element(By.NAME,"password")
textbox2.send_keys("admin123")
# textbox2.send_keys(Keys.RETURN)
time.sleep(1)
click=driver.find_element(By.XPATH,"//button[@type='submit']")
click.click()
time.sleep(10)


expected = "Dashboar"
act = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
if expected == act:
    print("test case pass")
else:
    print("test case fail")

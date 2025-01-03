import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
act=ActionChains(driver)
# driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("satwinder")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("satwinder")
# ctrl a
time.sleep(2)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
# ctrl c
time.sleep(2)
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
# ctrl c
time.sleep(2)
act.key_down(Keys.TAB)
act.key_up(Keys.TAB)

time.sleep(2)
# ctrl v
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)

time.sleep(2)

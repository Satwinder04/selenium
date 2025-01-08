import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://text-compare.com/")
time.sleep(2)
act=ActionChains(driver)
feild1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
feild1.send_keys("satwinder")
# driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("satwinder")
# ctrl a
time.sleep(2)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# ctrl c
time.sleep(2)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# TAB
time.sleep(2)
# act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
feild1.send_keys(Keys.TAB)
time.sleep(2)
# ctrl v
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
act.key_down(Keys.SHIFT).key_down(Keys.INSERT).key_up(Keys.INSERT).key_up(Keys.SHIFT).perform()

time.sleep(2)


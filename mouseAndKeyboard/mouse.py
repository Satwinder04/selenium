import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

computer=driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']")
notebook=driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Notebooks']")
action=ActionChains(driver)
action.move_to_element(computer).move_to_element(notebook).click().perform()
time.sleep(10)

exp="Notebooks"
act=driver.find_element(By.XPATH,"//h1[normalize-space()='Notebooks']").text

if exp==act:
    print("pass")
else:
    print("fail")

#
# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
#
# driver=webdriver.Chrome()
# action=ActionChains(driver)
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# right=driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')
# action.context_click(right).perform()
# time.sleep(4)
# driver.find_element(By.XPATH,"/html/body/ul/li[3]").click()
# a=driver.switch_to.alert
#
# print(a.text)
#
# exp="clicked: copy"
# if exp==a.text:
#     print("pass")
# else:
#     print("fail")
# time.sleep(4)
# a.accept()
# time.sleep(4)
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# # driver.implicitly_wait(5)
# action=ActionChains(driver)
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
# fram=driver.find_element(By.XPATH,'//*[@id="iframeResult"]')
# driver.switch_to.frame(fram)
# f1=driver.find_element(By.XPATH,"//input[@id='field1']")
# f1.clear()
# f1.send_keys("hooooo")
# time.sleep(3)
# f2=driver.find_element(By.XPATH,"//input[@id='field2']")
# time.sleep(3)
# copytext=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")
# action.double_click(copytext).perform()
# time.sleep(10)
#
# if f1.text==f2.text:
#     print("pass")
# else:
#     print("fail")
#
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver.implicitly_wait(5)
action=ActionChains(driver)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
for i in range(1,8):
    s=driver.find_element(By.XPATH,f"//div[@id='box{i}']")
    d=driver.find_element(By.XPATH,f"//div[@id='box10{i}']")
    action.drag_and_drop(s,d).perform()
    time.sleep(1)
    # assert "box6" in d.get_attribute("innerHTML"),"failed"




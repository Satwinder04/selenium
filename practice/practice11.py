# Task 1:
# https://testautomationpractice.blogspot.com/
# · Open a website in a new tab or window.
# · Switch between multiple windows using the window handle.
# . Close the specific window and return to the parent window.
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

dr=webdriver.Chrome()
url="https://testautomationpractice.blogspot.com/"
dr.get(url)
# act=ActionChains(dr)
# act.key_down(Keys.CONTROL)
# dr.find_element(By.ID,"apple").click()
# time.sleep(3)
# dr.find_element(By.ID,"lenovo").click()
# time.sleep(3)
# dr.find_element(By.ID,"dell").click()
# time.sleep(3)
# act.key_up(Keys.CONTROL)

dr.find_element(By.XPATH,"//a[normalize-space()='merrymoonmary']").click()
time.sleep(3)
winds=dr.window_handles
print(winds)
for i in winds:
    dr.switch_to.window(i)
    time.sleep(2)
    if dr.title=="merrymoonmary Stock Image and Video Portfolio - iStock":
        dr.close()
time.sleep(3)




# Task 2: Take Screenshots
# 1. Capture a screenshot of the webpage or a specific element.
# 2. Capture Screenshot of webpage
# 3. capture screenshot when your asseration is failed.
#
# Task 3:
# URL: https://www.google.com
# · Get all cookies from the current session.
# · Add a new cookie.
# · Delete a specific cookie.
# · Delete all cookies.
# Task 4:
# URL: https://www.wikipedia.org/
# · Set up Selenium to run in headless mode.
# . Verify if the page title or content can be fetched without displaying the browser.
#


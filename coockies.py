import time

from selenium import webdriver


driver=webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
a={
    "a":"satwinder",
    "b":"satwinder",
    "c":"satwinder",
    "d":"satwinder"
}
driver.add_cookie(a)
cookies= driver.get_cookies()
print(cookies)
print(len(cookies))

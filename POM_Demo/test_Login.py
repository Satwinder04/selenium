import time

import  pytest

from selenium import webdriver
from LoginPageObject import LoginPage



class TestLogin:
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(20)
        driver.maximize_window()
        lp = LoginPage(driver)
        time.sleep(2)
        lp.setUserName("Admin")
        time.sleep(2)
        lp.setUserPasesword("admin123")
        time.sleep(2)
        lp.clickLogin()
        act_title=driver.title
        assert act_title=="OrangeHRM"
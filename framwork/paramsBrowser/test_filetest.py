import time
import pytest
from selenium.webdriver.common.by import By


class TestCase:
    def test_google(self,setup):
        self.driver=setup
        self.driver.find_element(By.NAME, "q").send_keys("selenium")
        time.sleep(5)
        self.driver.find_element(By.NAME, "btnK").click()
        assert True
        self.driver.close()
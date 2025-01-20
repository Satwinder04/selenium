import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestCase:
    def test_chrome(self):
        try:
            driver=webdriver.Chrome()
            driver.get("https://www.google.com/")
            driver.find_element(By.NAME,"q").send_keys("selenium")
            time.sleep(5)
            driver.find_element(By.NAME,"btnK").click()
            title=driver.title
            assert driver.title==title
            time.sleep(2)
        finally:
            driver.close()

    def test_edge(self):
        try:
            driver=webdriver.Edge()
            driver.get("https://www.google.com/")
            driver.find_element(By.NAME,"q").send_keys("selenium")
            driver.find_element(By.NAME,"btnK").click()
            title = driver.title
            assert driver.title == title
            time.sleep(2)
        finally:
            driver.close()
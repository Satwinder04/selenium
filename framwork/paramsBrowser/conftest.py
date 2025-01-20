
import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser=="Chrome":
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")
        driver.implicitly_wait(3)
        driver.maximize_window()
        return driver
    elif browser=="Edge":
        driver = webdriver.Edge()
        driver.get("https://www.google.com/")
        driver.implicitly_wait(3)
        driver.maximize_window()
        return driver
    elif browser=="firefox":
            driver = webdriver.Firefox()
            driver.get("https://www.google.com/")
            driver.implicitly_wait(3)
            driver.maximize_window()
            return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
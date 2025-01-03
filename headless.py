from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome_options=options()

def Chrome():
    ops=Options()
    ops.add_argument("--headless")

    driver=webdriver.Chrome(options=ops)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(driver.title)

def Ege():
    ops = Options()
    ops.add_argument("--headless")

    driver = webdriver.Edge(options=ops)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(driver.title)

Ege()
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected

serviceObj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr = webdriver.Chrome(service=serviceObj)
dr.get("https://online.btes.co.in/login/index.php")
# time.sleep(2)
# Test cases for login form (email and password)
# Test cases for login form (username and password)
Usernames = [
    'valid_user',
    'invalid_user',
    'valid_user',
    '',
    'valid_user',
    'valid_user',
    'nonexistent_user',
    'VALID_USER',
    ' valid_user ',
    'valid_user+alias',
    'satwinder@123'
]

Passwords = [
    'ValidPass123',
    'ValidPass123',
    '',
    'ValidPass123',
    'short',
    'wrongpass',
    'ValidPass123',
    'ValidPass123',
    'ValidPass123',
    'ValidPass123',
    'Satwinder@123'
]

ExptResult = [
    'Invalid login, please try again',
    'Invalid login, please try again',
    'Invalid login, please try again',
    'Invalid login, please try again',
    'Invalid login, please try again',
    'Invalid login, please try again',
    'Invalid login, please try again',
    'Invalid login, please try again',
    'Invalid login, please try again',
    'Invalid login, please try again',
    'Satwinder Singh'
]


for u,p,e in zip(Usernames,Passwords,ExptResult):
    # time.sleep(2)
    dr.find_element(By.XPATH, "//*[@id='username']").send_keys(u)
    # time.sleep(2)
    dr.find_element(By.XPATH, "//*[@id='password']").send_keys(p)
    # time.sleep(2)
    dr.find_element(By.XPATH, "//*[@id='loginbtn']").click()
    time.sleep(6)
    if e=="Satwinder Singh":
        act=dr.find_element(By.XPATH,"//*[@class='usertext mr-1']").text
    else:
        act=dr.find_element(By.ID,"yui_3_17_2_1_1734628524914_29").text

    # dr.find_element(By.XPATH, "//*[@class='card-img dashboard-card-img']").click()
    # dr.find_element(By.XPATH,"//*[@id='yui_3_17_2_1_1734506008867_202']").click()
    time.sleep(2)

    # act = dr.find_element(By.XPATH, "//*[@class='page-header-headings']/h1").text
    # expt = "SDET with Python-AI for IT&R"

    if e == act:
        print("test pass")
    else:
        print("test fail")

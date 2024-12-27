import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected

serviceObj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr = webdriver.Chrome(service=serviceObj)
dr.get("https://online.btes.co.in/login/index.php")
time.sleep(2)
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
    'invalidpass123',
    'ValidPass123',
    'ValidPass',
    '123',
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


c=1
for u, p, e in zip(Usernames, Passwords, ExptResult):
    dr.find_element(By.XPATH, "//*[@id='username']").send_keys(u)
    time.sleep(1)
    dr.find_element(By.XPATH, "//*[@id='password']").send_keys(p)
    time.sleep(1)
    dr.find_element(By.XPATH, "//*[@id='loginbtn']").click()
    time.sleep(1)

    if e == "Satwinder Singh":
        act = dr.find_element(By.XPATH, "//*[@class='usertext mr-1']").text
    else:
        act = dr.find_element(By.XPATH,"//a[text()='Invalid login, please try again']").text
    if e == act:
        print(f"test case {c} pass")
    else:
        print(f"test case {c} fail")
    c+=1
    time.sleep(1)

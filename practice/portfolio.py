from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr=webdriver.Chrome(service=sobj)
dr.get("https://portfolio-vite-app.vercel.app/")
clk1=dr.find_element(By.LINK_TEXT,"02")
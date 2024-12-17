# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
#
# service_obj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get("https://demo.guru99.com/test/newtours/login.php")
# time.sleep(2)
# textbox1=driver.find_element(By.NAME,"userName")
# textbox1.send_keys("admin")
# time.sleep(2)
# textbox2=driver.find_element(By.NAME,"password")
# textbox2.send_keys("admin")
# time.sleep(2)
# click=driver.find_element(By.NAME,"submit")
# click.click()
# time.sleep(2)


# -------------------------------------------------------------------------------------
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("https://www.wikipedia.org/")
# # searchBox=driver.find_element(By.NAME,"search")
# searchBox=driver.find_element(By.ID,"searchInput")
# searchBox.send_keys("selenium Pyhton")
# time.sleep(5)
# clk=driver.find_element(By.CLASS_NAME,"pure-button")
# clk.click()
# time.sleep(5)
# --------------------------------------------------------------------------------------

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiA996Qp66KAxXayDgGHVISAQcQPAgI")
# # searchBox=driver.find_element(By.NAME,"search")
# searchBox=driver.find_element(By.NAME,"q")
# searchBox.send_keys("python programming language")
# time.sleep(5)
# clk=driver.find_element(By.NAME,"btnk")
# clk.click()
# time.sleep(5)
#
# # --------------------------------------------------------------------------------------
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("https://www.selenium.dev/")
# cls=driver.find_elements(By.CLASS_NAME,"nav-item")
# cls[3].click()
# # print(len(cls))
# time.sleep(5)

# # --------------------------------------------------------------------------------------
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("https://demoqa.com/automation-practice-form")
# clk=driver.find_elements(By.TAG_NAME,"input")
# print(len(clk))
# --------------------------------------------------------------------------------------

# import time
# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
#
# sobj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=sobj)
# driver.get("https://www.selenium.dev/documentation/")
# clk=driver.find_element(By.LINK_TEXT,"WebDriver").click()
# clk2=driver.find_element(By.PARTIAL_LINK_TEXT,"API").click()
#
# time.sleep(5)


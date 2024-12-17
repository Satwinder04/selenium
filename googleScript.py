# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.ie.service import Service
# # driver=webdriver.Chrome()
# # approch1
# # service_obj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# # driver=webdriver.Chrome(service=service_obj)
# # driver.get("https://www.google.com/")
# # # # driver.find_element(By.ID,"APjFqb").send_keys("selenium")
# # driver.find_element(By.NAME,"q").send_keys("selenium")
# # time.sleep(10)
#
# service_obj=Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com/")
# textbox=driver.find_element(By.NAME,"q")
# vl="selenium"
# textbox.send_keys(vl)
# time.sleep(5)
# click=driver.find_element(By.NAME,"btnK")
# click.click()
# time.sleep(5)
# exp_title=f'{vl} - Google Search'
# act_title=driver.title
# if exp_title==act_title:
#     print("test pass")
# else:
#     print("test fail")

#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
#
#
# service_obj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.google.com/")
#
# textbox = driver.find_element(By.NAME, "q")
# textbox.send_keys("https://github.com/Satwinder04")
# textbox.send_keys(Keys.RETURN)  # Simulate pressing Enter
#
# time.sleep(6)
# # Close the browser
# driver.quit()

# import time
#
# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.get("https://tailwindcss.com/docs/overscroll-behavior")
# driver.execute_script("window.scrollBy(0,500)","")
# time.sleep(3)
# value=driver.execute_script("return window.pageYOffset")
# print(value)
# time.sleep(6)

#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/")
# element=driver.find_element(By.XPATH,"/html/body/footer/section/div[1]/div/div/div[3]/div/div/img")
# time.sleep(3)
# driver.execute_script("arguments[0].scrollIntoView()",element)
#
# value=driver.execute_script("return window.pageYOffset;")
# print(value)
# time.sleep(6)

#
# import time
#
# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.get("https://tailwindcss.com/docs/overscroll-behavior")
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)","")
# time.sleep(3)
# value=driver.execute_script("return window.pageYOffset;")
# print(value)
# time.sleep(6)

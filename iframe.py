import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr = webdriver.Chrome(service=serviceObj)
dr.get("https://www.hyrtutorials.com/p/frames-practice.html#google_vignette")
startTime=time.time()
frm1=dr.find_element(By.ID,"frm1")
dr.switch_to.frame(frm1)
s=Select(dr.find_element(By.ID,"selectnav1"))
op=s.options
for i in op:
    # print(i.text)
    if i.text=="- Java":
        i.click()
        break
# time.sleep(5)

dr.switch_to.default_content()

frm2=dr.find_element(By.ID,"frm2")
dr.switch_to.frame(frm2)
dr.find_element(By.ID,"firstName").send_keys("satwinder")
dr.find_element(By.ID,"lastName").send_keys("Singh")
endTime=time.time()
totalTime=endTime-startTime
print(f"exicution time is : {totalTime}")
# time.sleep(5)
# ---------------------------------------------------------------
# import time
#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serviceObj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
# dr = webdriver.Chrome(service=serviceObj)
# dr.get("https://demo.automationtesting.in/Frames.html")
# a=dr.find_elements(By.XPATH,"//*[@class='analystic']")
# a[1].click()
# time.sleep(2)
#
# f1=dr.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
# dr.switch_to.frame(f1)
# time.sleep(2)
# f2=dr.find_element(By.XPATH,"//*[@class='iframe-container']/iframe")
# dr.switch_to.frame(f2)
# time.sleep(2)
# dr.find_element(By.XPATH,"//input").send_keys("Satwinder Singh")
# time.sleep(2)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service(r"D:\BEBO-tech\drivers\chromedriver-win64\chromedriver.exe")
dr = webdriver.Chrome(service=serviceObj)
dr.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(3)
dr.find_element(By.XPATH,"//*[text()='Click for JS Alert']").click()
time.sleep(3)
a=dr.switch_to.alert
a.accept()
time.sleep(3)


act1=dr.find_element(By.ID,"result").text
expt1="You successfully clicked an alert"
if act1==expt1:
    print("test pass")
else:
    print("failed")

#
# dr.find_element(By.XPATH,"//*[text()='Click for JS Confirm']").click()
# time.sleep(2)
# dr.switch_to.alert.dismiss()
# time.sleep(3)
#
# act2=dr.find_element(By.ID,"result").text
# expt2="You clicked: Cancel"
#
# if act2==expt2:
#     print("test pass")
# else:
#     print("failed")
#
# dr.find_element(By.XPATH,"//*[text()='Click for JS Prompt']").click()
# time.sleep(2)
# v="satwinder"
# dr.switch_to.alert.send_keys(f"{v}")
# time.sleep(3)
# dr.switch_to.alert.accept()
#
# act2=dr.find_element(By.ID,"result").text
# expt2=f"You entered: {v}"
#
# if act2==expt2:
#     print("test pass")
# else:
#     print("failed")



'''
3 steps 

rating is based upon 5 star's
level1---------
 step eligliblity for review   

level2---------
2 if person is elgible he can review (admistration got notification for aproval)
    if he didnt approved request it will automatically  accepted i 15 days
level3 -----------
again aprove process happens with no time limit 

test case 1 : to validate the per reach first level or not 
test case 2 : to validate the per write review in proper data type it should in text format
test case 3 : to validate the approve and reject button  is working or not 
test case 4 : to validate the autosubmittted fuctionality working properly or not within the give time 
test case 5 : to validate the their no time limmit in last level of apporving or rejecting 
to validate 
'''

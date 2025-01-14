import time
from selenium.webdriver.support.select import Select

from XLUtils import *
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url="https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
driver.get(url)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="wzrk-cancel"]').click()
file=r"dataDriven/intrest/simple_interest_data.xlsx"
s1="Sheet1"

rows=getRowCount(file,s1)
cols=getColumnCount(file,s1)

for r in range(2,rows+1):
    for c in range(1,cols+1):
        # print(readData(file,s1,r,c), end="  ")
        if c==1:
            principle=readData(file,s1,r,c)
            driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principle)
            # time.sleep(1)
        elif c==2:
            ROI=readData(file,s1,r,c)
            driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(ROI)
            # time.sleep(1)
        elif c==3:
            tenure=readData(file,s1,r,c)
            driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(tenure)
            # time.sleep(1)
        elif c==4:
            tenurePeriod=readData(file,s1,r,c)
            slct=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
            slct.select_by_visible_text(tenurePeriod)
            # time.sleep(1)
        elif c==5:
            frequency=readData(file,s1,r,c)
            slct2=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
            slct2.select_by_visible_text(frequency)
            # time.sleep(1)

            driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]').click()
        # time.sleep(1)
        if c==6:
            ExMV=readData(file,s1,r,c)
            AcMV=driver.find_element(By.ID,"resp_matval").text
            # print("ex",ExMV)
            # print("Ac",AcMV)
            if ExMV==float(AcMV):
                fillGreenColor(file,s1,r,8)
                writeData(file,s1,r,8,"Passed")
            else:
                fillRedColor(file,s1,r,8)
                writeData(file,s1,r,8,"Failed")
        # time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]').click()
print("Go, and check Exl File")
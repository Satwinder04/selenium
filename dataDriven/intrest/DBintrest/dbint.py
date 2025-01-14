import pymysql
import time
from selenium.webdriver.support.select import Select

from XLUtils import *
from selenium import webdriver
from selenium.webdriver.common.by import By

con=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="cal"
)
curs=con.cursor()
curs.execute("select * from cal_data")
driver = webdriver.Chrome()
url = "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
driver.get(url)
driver.maximize_window()
time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="wzrk-cancel"]').click()
driver.find_element(By.ID,"wzrk-cancel").click()
time.sleep(3)
file = r"dataDriven/intrest/DBintrest/simple_interest_data.xlsx"
s1 = "Sheet1"
rows = getRowCount(file, s1)
cols = getColumnCount(file, s1)
r=2
for row in curs:
    principle=str(row[0])
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle)
    # time.sleep(1)

    ROI=str(row[1])
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(ROI)
    # time.sleep(1)

    tenure=str(row[2])
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(tenure)
    # time.sleep(1)

    tenurePeriod=row[3]
    slct = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    slct.select_by_visible_text(tenurePeriod)
    # time.sleep(1)

    frequency=str(row[4])
    slct2 = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    slct2.select_by_visible_text(frequency)
    # time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]').click()
    # time.sleep(1)
    ExMV = row[5]
    AcMV = driver.find_element(By.ID, "resp_matval").text
    if ExMV == float(AcMV):
        fillGreenColor(file, s1, r, 8)
        writeData(file, s1, r, 8, "Passed")
    else:
        fillRedColor(file, s1, r, 8)
        writeData(file, s1, r, 8, "Failed")
    time.sleep(1)
    r+=1

    driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[1]').click()

    # print(principle)
    # print(ROI)
    # print(tenure)
    # print(tenurePeriod)
    # print(frequency)
    # print(ExMV)

    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]').click()
con.close()
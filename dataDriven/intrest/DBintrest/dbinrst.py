import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from XLUtils import *
import time
from selenium.webdriver.support.select import Select
#
# try:
#     driver=webdriver.Chrome()
#     url="https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
#     driver.get(url)
#     time.sleep(2)
#     driver.find_element(By.XPATH,'//*[@id="wzrk-cancel"]').click()
#     file=r"dataDriven/intrest/DBintrest/simple_interest_data.xlsx"
#     s1="Sheet1"
#
#     rows=getRowCount(file,s1)
#     cols=getColumnCount(file,s1)
#
#     con=pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="password",
#         database="cal"
#     )
#     curs=con.cursor()
#     curs.execute("select * from cal_data")
#
#     for row in curs:
#         print(row[0],row[1],row[2],row[3],row[4],row[5])
#         # principle = row[0]
#         # driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle)
#         # time.sleep(1)
#         # rate_of_interest = row[1]
#         # driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate_of_interest)
#         # time.sleep(1)
#         #
#         # tenure = row[2]
#         # driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(tenure)
#         # time.sleep(1)
#         #
#         # tenure_period = row[3]
#         # slct = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
#         # slct.select_by_visible_text(tenure_period)
#         # time.sleep(1)
#         #
#         # frequency = row[4]
#         # slct2 = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
#         # slct2.select_by_visible_text(frequency)
#         # time.sleep(1)
#         #
#         # driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[1]').click()
#         #
#         # AcMV = driver.find_element(By.ID, "resp_matval").text
#         # expected_maturity =row[5]
#         # if expected_maturity==float(AcMV):
#         #     fillGreenColor(file, s1, rows, 8)
#         #     writeData(file, s1,rows , 8, "Passed")
#         # else:
#         #     fillRedColor(file, s1, rows, 8)
#         #     writeData(file, s1, rows, 8, "Failed")
#         #
#         # driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[2]').click()
#
#
#
#     # for i in curs:
#     #     print(i[0],i[1],i[2])
#     print("Go, and check Exl File")
#     con.close()
# # except:
# #     print("database not connected")

driver=webdriver.Chrome()
# url="https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
# driver.get(url)
time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="wzrk-cancel"]').click()
file=r"dataDriven/intrest/DBintrest/simple_interest_data.xlsx"
s1="Sheet1"

rows=getRowCount(file,s1)
cols=getColumnCount(file,s1)
con=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="cal"
)
curs=con.cursor()
curs.execute("select * from cal_data")

for row in curs:
    print(row[0],row[1],row[2],row[3],row[4],row[5])


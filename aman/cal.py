from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from XLUtils import *

driver = webdriver.Chrome()
driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")
driver.maximize_window()

file = r"D:\BEBO TECHNOLOGY\Selenium\DDT_using_Excel\Calculate.xlsx"

rows = getRowCount(file,'Sheet2')

for r in range(2,rows+1):
    IDA = readData(file,'Sheet1',r,1)
    LofCD = IDA = readData(file,'Sheet1',r,2)
    IR = readData(file, 'Sheet1', r, 3)
    Comp =readData(file,'Sheet1',r,4)
    AP = readData(file, 'Sheet1', r, 5)


    driver.find_element(By.XPATH,'//*[@id="mat-input-0"]').clear()
    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(IDA)

    driver.find_element(By.XPATH,'//*[@id="mat-input-1"]').clear()
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(LofCD)

    driver.find_element(By.XPATH,'//*[@id="mat-input-2"]').clear()
    driver.find_element(By.XPATH, '//*[@id="mat-input-2"]').send_keys(IR)

    compIn = Select(driver.find_element(By.XPATH,'//*[@id="mat-select-value-1"]'))
    compIn.select_by_visible_text(Comp)

    cal_button = driver.find_element(By.XPATH,'//*[@id="CIT-chart-submit"]/div')
    cal_button.click()

    AP_amount = driver.find_element(By.XPATH, '//*[@id="cdAPY"]').text

    if AP==AP_amount:
        print("test passed")
        writeData(file, "Sheet1", r, 7, "Passed")
        fillGreenColor(file, "Sheet1", r, 7)
    else:
        print("test failed")
        writeData(file, "Sheet1", r, 7, "Failed")
        fillRedColor(file, "Sheet1", r, 7)

driver.close()
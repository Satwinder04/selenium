import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

loction=os.getcwd()

def chrome_setup():
    # preferences={"download.default_directory":"D:\BEBO-tech\Selenium\Selenium\download"}
    preferences={"download.default_directory":loction}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    dr = webdriver.Chrome(options=ops)
    return dr
driver = chrome_setup()
driver.get("https://www.pexels.com/photo/charming-cottage-in-sunlit-forest-29935806/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='SpacingGroup_default__s_Qnp SpacingGroup_wrap__WdQqN']//div[@class='dropdown_wrapper__Wwmqn']//a[@class='Button_button__RDDf5 spacing_noMargin__F5u9R spacing_pr30__J0kZ7 spacing_pl30__01iHm MediumDownloadSizeSelector_downloadButton__QGPhk Button_clickable__DqoNe Button_color-alien__c13Rt Link_link__Ime8c spacing_noMargin__F5u9R']//span//span[@class='Button_text__Yp1Qo'][normalize-space()='Free download']").click()
time.sleep(10)
driver.quit()

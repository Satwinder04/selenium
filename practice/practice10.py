import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://www.flipkart.com/clothing-and-accessories/~cs-aerg0b0afc/pr?sid=clo&collection-tab-name=KK%2CSets%2CDM%2CSarees&fm=neo%2Fmerchandising&iid=M_2b3eb777-ca72-4332-8ee1-bfa3a6b3b325_1_372UD5BXDFYS_MC.HQXTE43PO8HC&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Fashion~Women%2BEthnic_HQXTE43PO8HC&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L1_view-all&cid=HQXTE43PO8HC")
driver.find_element(By.XPATH,"/html/body/div[3]/div/span").click()

fashion=driver.find_element(By.XPATH,"//div[@class='_1wE2Px']")
fashion2=driver.find_element(By.XPATH,"//a[@class='_1BJVlg _11MZbx']")
fashion3=driver.find_element(By.XPATH,"//div[@class='_31z7R_']//a[2]")

action=ActionChains(driver)
time.sleep(2)
action.move_to_element(fashion).move_to_element(fashion2).move_to_element(fashion3).click().perform()
time.sleep(2)

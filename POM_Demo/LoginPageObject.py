from selenium.webdriver.common.by import By


class LoginPage:
    txt_username_Name="username"
    txt_password_Name="password"
    btn_signin_xpath="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    #action

    def setUserName(self,username):
        self.driver.find_element(By.NAME,'txt_username_Name').send_keys(username)
    def setUserPasesword(self,userpass):
        self.driver.find_element(By.NAME,'txt_password_Name').send_keys(userpass)
    def clickLogin(self):
        self.driver.find_element(By.NAME,'btn_signin_xpath').click()

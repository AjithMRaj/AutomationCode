from selenium.webdriver.common.by import By

class Loginpage():
    def __init__(self,Driver):
        self.Driver =Driver

        self.Username_Textbox_Xpath="//input[@name='username']"
        self.Password_Textbox_CSS="input[type='password']"
        self.Login_btn_Xpath="//button[@type='submit']"
    def enter_Username(self,Username):
        self.Driver.find_element(By.XPATH,(self.Username_Textbox_Xpath)).clear()
        self.Driver.find_element(By.XPATH,(self.Username_Textbox_Xpath)).send_keys("Admin")
    def enter_Password(self,Password):
        self.Driver.find_element(By.CSS_SELECTOR,(self.Password_Textbox_CSS)).clear()
        self.Driver.find_element(By.CSS_SELECTOR,(self.Password_Textbox_CSS)).send_keys("admin123")
    def click_loginbtn(self):
        self.Driver.find_element(By.XPATH,(self.Login_btn_Xpath)).click()

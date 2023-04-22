from selenium.webdriver.common.by import By
class Homepage():
    def __init__(self,Driver):
        self.Driver=Driver
        self.welcome_classname="oxd-icon.bi-caret-down-fill.oxd-userdropdown-icon"
        self.logout_linktext="Logout"
    def click_welcome(self):
       self.Driver.find_element(By.CLASS_NAME,(self.welcome_classname)).click()
    def click_logout(self):
        self.Driver.find_element(By.LINK_TEXT,(self.logout_linktext)).click()

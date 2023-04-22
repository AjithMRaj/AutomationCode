import time
import moment
import allure
import pytest
from pages.loginpage import Loginpage
from pages.homepage import Homepage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLoginHRM():

    def test_login(self):
        Driver=self.Driver
        Driver.get(utils.URL)
        login=Loginpage(Driver)
        login.enter_Username(utils.USERNAME)
        login.enter_Password(utils.PASSWORD)
        login.click_loginbtn()
        time.sleep(2)
        # currenttime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        # screenshotName = "screenshots" + currenttime
        # allure.attach(self.Driver.get_screenshot_as_png(), name=screenshotName,
        #               attachment_type=allure.attachment_type.PNG)
        # Driver.get_screenshot_as_file(
        #     "C:/Users/Admin/Desktop/Selenium Python Notes/Screenshots/" + screenshotName + ".png")

    #@pytest.mark.skip()
    def test_logout(self):
        try:
            Driver =self.Driver
            homepage=Homepage(Driver)
            homepage.click_welcome()
            time.sleep(3)
            homepage.click_logout()
            x=Driver.title
            assert x=="OrangeHR"
        except AssertionError as error:
            Driver = self.Driver
            print("Assertion error occurred")
            print(error)
            time.sleep(2)
            currenttime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshotName = "Screenshots"+currenttime
            allure.attach(self.Driver.get_screenshot_as_png(),name=screenshotName,attachment_type=allure.attachment_type.PNG)
            Driver.get_screenshot_as_file("C:/Users/Admin/Desktop/Selenium Python Notes/Screenshots/"+screenshotName+".png")
            raise
        except:
            print("There was an exception")
            raise
        else:
            print("NO exceptions occurred")
        finally:
            print("I am inside finally blocked/Unblocked")

















    # Driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
    # Driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("admin123")
    # Driver.find_element(By.XPATH,"input[type='password']").click()
    # x=Driver.title
    # assert x=="OrangeHRM"

# def test_logout(test_setup):
    # Driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
    # time.sleep(3)
    # wait1 = WebDriverWait(Driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Logout")))
    # wait1.click()

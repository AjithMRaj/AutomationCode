import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="edge",help="type in browse")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    global Driver
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        Driver = webdriver.Chrome(
            executable_path="C:/Users/Admin/PycharmProjects/PageObjectModule/Drivers/chromedriver.exe")
    elif browser=="firefox":
         Driver = webdriver.Firefox(
             executable_path="C:/Users/Admin/PycharmProjects/PageObjectModule/Drivers/geckodriver.exe")
    elif browser=="edge":
        Driver=webdriver.Edge(executable_path="C:/Users/Admin/PycharmProjects/PageObjectModule/Drivers/msedgedriver.exe")
    Driver.implicitly_wait(10)
    Driver.maximize_window()
    request.cls.Driver=Driver
    yield
    print("Test Completed")
    Driver.close()
    Driver.quit()



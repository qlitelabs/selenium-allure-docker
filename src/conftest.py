import pytest
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# # Get browser name from arguments, use parser as it is
# # this allows to access Python parser to add a new optional parameter
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome:  ")


# conftest is used to have the fixtures in one place, so this portion was in login_test.py
# just added request param, from selenium import webdriver and request.cls.driver = driver
# this fixture or function will run before, in this case, the class, as that is the scope
@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager

    browser = os.getenv('BROWSER')
    if browser == "chrome":
        # only this command is needed to download or look the chromedriver, no need for .exe
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, 'CHROME'))
        # driver = webdriver.Chrome(executable_path= "C:/Users/jorge/Desktop/Work/Code/Mine/PythonAutomationFramework/drivers/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, 'FIREFOX'))
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.maximize_window()
    # next line will sent the driver variable to the class
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test completed.")

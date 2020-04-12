from selenium import webdriver
import pytest
import allure
import moment

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as environment

#to link the setup in conftest.py
@pytest.mark.usefixtures("test_setup")

class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(environment.URL)

        login = LoginPage(driver)
        login.enter_username(environment.USERNAME)
        login.enter_password(environment.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRM"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = environment.whoami()
            screenshotName = testName + "_screenshot_" + currTime
            # save screenshot in allure
            allure.attach(driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            #to get the file on specific path
            driver.get_screenshot_as_file("/usr/src/app/screenshots/"+ screenshotName+".png")
            raise
        except:
            print("There was an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = environment.whoami()
            screenshotName = testName + "_screenshot_" + currTime
            # save screenshot in allure
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            # to get the file on specific path
            driver.get_screenshot_as_file(
                "/usr/src/app/screenshots/" + screenshotName + ".png")
            #the raise is to show it as a failure
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("Inside finally block")

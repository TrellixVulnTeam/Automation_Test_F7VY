from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNT(BasePage):

    # def is_title_matches(self):
    #     return "My Store" in self.driver.title

    def navigate_to_about_us_page(self):

        about_us_link = self.driver.find_element(*AboutUsLocators.ABOUT_US)
        about_us_link.click()
        time.sleep(2)

    def verify_email_address_invalid(self):

        email_add = self.driver.find_element(*AboutUsLocators.EMAILADD)
        email_add.send_keys("test")
        sign_up = self.driver.find_element(*AboutUsLocators.SIGN_UP)
        sign_up.click()
        time.sleep(2)
        error = self.driver.find_element(*AboutUsLocators.ERROR)
        assert error is not None, "Error is not present"










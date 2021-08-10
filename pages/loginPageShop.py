
from locators.page_elements import *
from utils import environment as env
from extensions.commands import *



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPageShop(BasePage):
    def is_title_matches(self):
        return "My Store" in self.driver.title

    """Login creds for use in checkout flow"""
    def click_signin(self):
        signin = self.driver.find_element(*ShopLogin.SIGNIN)
        signin.click()
        time.sleep(2)

    def signin_invalid_email(self):
        email = self.driver.find_element(*ShopLogin.EMAIL)
        psswd = self.driver.find_element(*ShopLogin.PSSWD)
        signinBtn = self.driver.find_element(*ShopLogin.SIGNINBTN)
        alertError = self.driver.find_element(*ShopLogin.ALERTERROR)
        email.send_keys("test")
        psswd.send_keys("12345")
        signinBtn.click()
        assert alertError is not None, "Error is not displayed"
        time.sleep(2)

    def signin_invalid_password(self):
        email = self.driver.find_element(*ShopLogin.EMAIL)
        psswd = self.driver.find_element(*ShopLogin.PSSWD)
        signinBtn = self.driver.find_element(*ShopLogin.SIGNINBTN)
        alertError = self.driver.find_element(*ShopLogin.ALERTERROR)
        email.send_keys("erika1231@mailinator.com")
        psswd.send_keys("1111")
        signinBtn.click()
        assert alertError is not None, "Error is not displayed"
        time.sleep(2)

    def signin_successful(self):
        email = self.driver.find_element(*ShopLogin.EMAIL)
        psswd = self.driver.find_element(*ShopLogin.PSSWD)
        signinBtn = self.driver.find_element(*ShopLogin.SIGNINBTN)
        alertError = self.driver.find_element(*ShopLogin.ALERTERROR)
        email.send_keys("erika1231@mailinator.com")
        psswd.send_keys("12345")
        signinBtn.click()
        time.sleep(2)
        pageTitle = "My account - My Store"
        assert pageTitle in self.driver.title
        time.sleep(2)

    def screenshot(self):
        Commands.take_screenshot(self.driver, test="search_test")


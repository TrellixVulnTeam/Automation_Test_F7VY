""" PYTEST PAGE ELEMENT IDENTIFIERS GO HERE """

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USN_INPUT = (By.XPATH, 'sample_xpath')
    PWD_INPUT = (By.XPATH, 'sample_xpath')
    LOGIN_CTA = (By.XPATH, 'sample_xpath')


class LandingPageLocators(object):
    SEARCH_CTA = (By.XPATH, 'sample_xpath')


class Search(object):
    SEARCH_FIELD = (By.XPATH, '//input[@title="Search"]')
    SEARCH_CTA = (By.XPATH, '(//input[@value="Google Search"])[2]')

class ShopLogin(object):
    SIGNIN = (By.XPATH, '//a[@class="login"]')
    EMAIL = (By.XPATH, '//input[@id="email"]')
    PSSWD = (By.XPATH, '//input[@id="passwd"]')
    SIGNINBTN = (By.XPATH, '//button[@id="SubmitLogin"]')
    ALERTERROR = (By.XPATH, '//div[@class="alert alert-danger"]')

class WebbysLocators(object):
    NOMINEES = (By.XPATH, '//div[@class="mod-winners-nav__results "]/div[3]//div[@class="mod-winners-gallery__nominee"]')
    IMAGE = (By.XPATH, './/div[@class="mod-winners-gallery__image"]/a/img')
    # EYEBROW = (By.XPATH, './/div[@class="mod-winners-gallery__credits"]')
    # TITLE = (By.XPATH, './/h2[@class="mod-winners-gallery__title"]')

class LinkNavLocators(object):
    LINKS = (By.XPATH, '//div[@class="w3-light-grey"]/a')

class AboutUsLocators(object):
    ABOUT_US = (By.XPATH, '//div[@id="homepage-page-overlay"]//a[@href="/about-us"]')
    EMAILADD = (By.XPATH, '//input[@id="newsletter_email"]')
    SIGN_UP = (By.XPATH, '//button[@class="btn-newsletter-signup"]')
    ERROR = (By.XPATH, '//div[@class="newsletter-action error"]')

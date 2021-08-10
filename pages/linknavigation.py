from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestLinks(BasePage):

    # def is_title_matches(self):
    #     return "My Store" in self.driver.title

    def navigate_links(self):
        links = self.driver.find_elements(*LinkNavLocators.LINKS)
        for link in links:
            print(link.text)















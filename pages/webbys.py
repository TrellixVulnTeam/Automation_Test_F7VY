from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestWebbys(BasePage):

    # def is_title_matches(self):
    #     return "My Store" in self.driver.title

    def identify_placeholder_image(self):

        container = self.driver.find_elements(*WebbysLocators.NOMINEES)
        for con in container:

            images = con.find_element(*WebbysLocators.IMAGE)
            source = images.get_attribute("src")
            result = source.endswith("no-image_620x317.jpg")
            assert result == False, "Placeholder image is available"
            print(source)









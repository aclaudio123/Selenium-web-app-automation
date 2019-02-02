# The base_page contains steps definitions
# that are identical for every page

from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        # current base url without any endpoint
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        # every page has a title
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

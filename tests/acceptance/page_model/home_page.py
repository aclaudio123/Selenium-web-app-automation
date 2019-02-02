from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):  # homepage inheriting from base page

    # in Python, methods are called like so HomePage.name_of_method().
    # However, for methods without any arguments, we can use Python's
    # @property decorator to call them without any brackets at the end.
    # Therefore, HomePage.name_of_method() == HomePage.name_of_method
    # @property indicates the methods are properties of the HomePage class

    @property
    def url(self):
        # get the base url + homepage endpoint
        return super(HomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)

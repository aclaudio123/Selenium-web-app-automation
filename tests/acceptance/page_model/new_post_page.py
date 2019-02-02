from selenium.webdriver.common.by import By

from tests.acceptance.locators.new_post_page import NewPostLocators
from tests.acceptance.page_model.base_page import BasePage


class NewPostPage(BasePage):
    @property
    def url(self):
        return super(NewPostPage, self).url + '/post'

    @property
    def form(self):
        return self.driver.find_element(*NewPostLocators.NEW_POST_FORM)

    def form_field(self, name):
        # finding children elements of form
        return self.form.find_element(By.NAME, name)

    @property
    def submit_button(self):
        return self.driver.find_element(*NewPostLocators.SUBMIT_BUTTON)




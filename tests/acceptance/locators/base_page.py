# The base_page locator contains locators
# used for finding elements in the base_page model

from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'  # same way to locate all page titles
    NAV_LINKS = By.CLASS_NAME, 'nav-link'

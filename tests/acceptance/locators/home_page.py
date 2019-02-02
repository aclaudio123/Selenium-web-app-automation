# locators describe how we searching for each element
# on a page, and what the element is going to be. It helps
# to reduce duplications or hard coding locator tags in our
# scripts.
# However, some elements can be located the same way on all
# pages e.g. the title BY.TAG_NAME, 'h1'.
# Therefore, generic elements will be put in a locators' base_page
#

from selenium.webdriver.common.by import By


class HomePageLocators:
    NAVIGATION_LINK = (By.ID, 'blog-link')



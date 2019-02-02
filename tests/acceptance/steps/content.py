from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')  # this step is generic, can mean any page
def step_impl(context):
    page = BasePage(context.driver)  # using the base_page model for generic steps
    assert page.title.is_displayed()


@then('The title tag has content "(.*)"')  # another generic step
def step_impl(context, title_content):
    page = BasePage(context.driver)
    assert page.title.text == title_content  # getting the page title text


@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)

    assert page.posts_section.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]

    assert len(posts_with_title) > 0
    # evaluate to true if all post is visible else false. alternative is any()
    assert all([post.is_displayed() for post in posts_with_title])


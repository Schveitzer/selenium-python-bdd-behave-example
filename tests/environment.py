import allure
from allure_commons.types import AttachmentType
from helper.helper import HELPER
from pages.contact_page import CONTACT_PAGE
from pages.login_page import LOGIN_PAGE
from browser import DRIVER
from data.credentials import load_credentials


def before_all(context):
    context.browser = DRIVER
    context.login_page = LOGIN_PAGE
    context.contact_page = CONTACT_PAGE
    context.helper = HELPER
    context.baseUrl = "http://automationpractice.com/index.php"
    context.user = load_credentials()


def after_step(context, step):
    # Take screenshot if step fails and attach in report file
    if step.status == 'failed':
        allure.attach(context.browser.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=AttachmentType.PNG)


def after_all(context):
    context.browser.quit()

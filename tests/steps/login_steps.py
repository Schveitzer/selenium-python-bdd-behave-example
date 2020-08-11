from behave import step
from nose.tools import assert_equal
from constants import system_messages


@step("I'm on the login page")
def step_impl(context):
    context.login_page.open(context)


@step("eu faço login com o usuário: '{username}'")
def step_impl(context, username):
    user = context.user[username]
    context.login_page.login(user['email'], user['password'])


@step("I'm logged with the user: '{username}'")
def step_impl(context, username):
    user = context.user[username]
    if context.login_page.button_sign_in_out().text == 'Sign in':
        context.login_page.login(user['email'], user['password'])
        context.helper.wait_for_element_is_visible(context.login_page.welcome_message())

    elif context.login_page.user_name().text != user['name']:
        context.login_page.button_sign_in_out().click()
        context.login_page.login(user['email'], user['password'])
        context.helper.wait_for_element_is_visible(context.login_page.welcome_message())


@step("I try to access with; email: '{email}' and password: '{password}'")
def step_impl(context, email, password):
    context.login_page.login(email, password)


@step("system displays a message showing that data is invalid")
def step_impl(context):
    assert_equal(context.login_page.invalid_credentials_message().text, system_messages.LOGIN_FAILED)


@step("system displays welcome message")
def step_impl(context):
    assert_equal(context.login_page.welcome_message().text, system_messages.WELCOME_MESSAGE)


@step("I clear the browsing data")
def step_impl(context):
    context.browser.delete_all_cookies()

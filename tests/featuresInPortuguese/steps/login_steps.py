from behave import step
from nose.tools import assert_equal
from constants import system_messages


@step('eu estou na página de login')
def step_impl(context):
    context.login_page.open(context)


@step("eu faço login com o usuário: '{username}'")
def step_impl(context, username):
    user = context.user[username]
    context.login_page.login(user['email'], user['password'])


@step("eu estou logado com o usuário: '{username}'")
def step_impl(context, username):
    user = context.user[username]
    if context.login_page.button_sign_in_out().text == 'Sign in':
        context.login_page.login(user['email'], user['password'])
        context.helper.wait_for_element_is_visible(context.login_page.welcome_message())

    elif context.login_page.user_name().text != user['name']:
        context.login_page.button_sign_in_out().click()
        context.login_page.login(user['email'], user['password'])
        context.helper.wait_for_element_is_visible(context.login_page.welcome_message())


@step("eu tento fazer login com os dados; email: '{Email}' e senha: '{Senha}'")
def step_impl(context, Email, Senha):
    context.login_page.login(Email, Senha)


@step("sistema exibe mensagem informando que dados são invalidos")
def step_impl(context):
    assert_equal(context.login_page.invalid_credentials_message().text, system_messages.LOGIN_FAILED)


@step("sistema exibe mensagem de boas vindas")
def step_impl(context):
    assert_equal(context.login_page.welcome_message().text, system_messages.WELCOME_MESSAGE)


@step("que eu limpo os dados de navegação")
def step_impl(context):
    context.browser.delete_all_cookies()

from behave import step
from nose.tools import assert_equal

from constants import system_messages, system_label


@step("eu clico no botão contato para abrir a página de contato")
def step_impl(context):
    context.contact_page.contact_link().click()
    context.helper.wait_for_element_is_visible(context.contact_page.contact_page_header())


@step("sistema exibe o título da página de contato")
def step_impl(context):
    context.helper.wait_for_element_is_visible(context.contact_page.contact_page_header())
    assert_equal(context.contact_page.contact_page_header().text, system_label.CUSTOMER_SERVICE_LABEL)


@step("eu envio uma mensagem com documento")
def step_impl(context):
    content = {
        "subject": "Customer service",
        "message": "My message test",
        "file": "test.pdf"
    }
    context.contact_page.send_menssage(content)


@step("sistema exibe mensagem de menssagem enviada com sucesso")
def step_impl(context):
    context.helper.wait_for_element_is_visible(context.contact_page.sucess_message())
    assert_equal(context.contact_page.sucess_message().text, system_messages.MESSAGE_SENT)


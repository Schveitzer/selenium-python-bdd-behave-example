from behave import step
from nose.tools import assert_equal

from constants import system_messages, system_label


@step("I click on the contact button to open the contact page")
def step_impl(context):
    context.contact_page.contact_link().click()
    context.helper.wait_for_element_is_visible(context.contact_page.contact_page_header())


@step("system displays the title of the contact page")
def step_impl(context):
    context.helper.wait_for_element_is_visible(context.contact_page.contact_page_header())
    assert_equal(context.contact_page.contact_page_header().text, system_label.CUSTOMER_SERVICE_LABEL)


@step("I send a message with attachment")
def step_impl(context):
    content = {
        "subject": "Customer service",
        "message": "My message test",
        "file": "test.pdf"
    }
    context.contact_page.send_menssage(content)


@step("system displays successfully sent message")
def step_impl(context):
    context.helper.wait_for_element_is_visible(context.contact_page.sucess_message())
    assert_equal(context.contact_page.sucess_message().text, system_messages.MESSAGE_SENT)


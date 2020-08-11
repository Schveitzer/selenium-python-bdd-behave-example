import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser import Driver


class ContactPage(Driver):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ContactPage()
        return cls.instance

    def contact_link(self):
        return self.driver.find_element(By.ID, "contact-link")

    def contact_page_header(self):
        return self.driver.find_element(By.CLASS_NAME, "page-heading.bottom-indent")

    def subject_contact(self):
        return self.driver.find_element(By.ID, "id_contact")

    def message_field(self):
        return self.driver.find_element(By.ID, "message")

    def button_submit_message(self):
        return self.driver.find_element(By.ID, "submitMessage")

    def sucess_message(self):
        return self.driver.find_element(By.CLASS_NAME, "alert.alert-success")

    def input_file(self):
        return self.driver.find_element(By.ID, "fileUpload")

    def send_menssage(self, content):
        if content["file"] is not None:
            local_file_path = os.getcwd() + "/tests/documents/" + content["file"]
            self.input_file().send_keys(local_file_path)
        select = Select(self.subject_contact())
        select.select_by_visible_text(content["subject"])
        self.message_field().send_keys(content["message"])
        self.button_submit_message().click()


CONTACT_PAGE = ContactPage.get_instance()

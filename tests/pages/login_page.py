from selenium.webdriver.common.by import By
from browser import Driver


class LoginPage(Driver):

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def open(self, context):
        self.driver.get(context.baseUrl)

    def button_login(self):
        return self.driver.find_element(By.CLASS_NAME, "login")

    def input_email(self):
        return self.driver.find_element(By.ID, "email")

    def input_password(self):
        return self.driver.find_element(By.ID, "passwd")

    def button_submit_login(self):
        return self.driver.find_element(By.ID, "SubmitLogin")

    def welcome_message(self):
        return self.driver.find_element(By.CLASS_NAME, "info-account")

    def invalid_credentials_message(self):
        return self.driver.find_element(By.XPATH, "//li[text() ='Authentication failed.']")

    def button_sign_in_out(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@class, 'log')]")

    def user_name(self):
        return self.driver.find_element(By.XPATH, "//div[@class='header_user_info']//span")

    def login(self, user, password):
        self.button_login().click()
        self.input_email().send_keys(user)
        self.input_password().send_keys(password)
        self.button_submit_login().click()


LOGIN_PAGE = LoginPage.get_instance()

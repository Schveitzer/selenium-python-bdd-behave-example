from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from browser import Driver


class Helper(Driver):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Helper()
        return cls.instance

    # For this function passes locator as parameter
    # ex: self.wait_for_element_located_not_exist(By.ID, "passwd")
    def wait_for_element_located_not_exist(self, *locator):
        WebDriverWait(self.driver, 1).until(ec.invisibility_of_element_located(locator))

    # For this function passes element as parameter
    # ex: self.wait_for_element_is_visible(context.login_page.welcome_message())
    def wait_for_element_is_visible(self, element):
        WebDriverWait(self.driver, 10).until(ec.visibility_of(element))

    def move_to_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_for_element_clickable_and_click(self, element):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable(element))
        element.click()

    def move_to_element_and_click(self, element):
        self.move_to_element(element)
        element.click()


HELPER = Helper.get_instance()

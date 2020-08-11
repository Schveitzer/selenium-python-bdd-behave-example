from selenium import webdriver


class Driver:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Driver()
        return cls.instance

    capabilities_chrome = {
        'browserName': 'chrome',
        'goog:chromeOptions': {
            'args': [
                '--disable-extensions',
                '--disable-gpu',
                '--disable-infobars',
                '--disable-web-security',
                '--start-maximized'
            ],
            'prefs': {
                'download.default_directory': "./test-report/Downloads",
                'download.directory_upgrade': True,
                'download.prompt_for_download': False,
                'plugins.always_open_pdf_externally': True,
                'safebrowsing_for_trusted_sources_enabled': False
            }
        }
    }
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=capabilities_chrome,
    )
    driver.implicitly_wait(10)
    verificationErrors = []
    accept_next_alert = True

    def quit(self):
        self.driver.quit()

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()


DRIVER = Driver.get_instance()

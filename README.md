# Selenium Python Behave
#### [Para ver o projeto em português clique aqui](https://github.com/Schveitzer/selenium-python-bdd-behave-example/tree/master/tests/featuresInPortuguese)

In this project I demonstrate how to use Selenium WebDriver with Behave for automation of web interface tests using BDD concepts.

Nose was used for assertions.

This project includes:

- Framworks:
    - Selenium
    - Behave
    - Nose

- Features:
    - Page Object with Singleton Pattern
    - Report with Allure (Print screen on fail)
    - Code lint with Pylint
    - Simple commands with Make

## Requirements
- Python >= 3.6 - [How install Pytohn](https://www.python.org/downloads/)
- Pip >= 20.0.x - [How install pip](https://pip.pypa.io/en/stable/installing/)
- Docker >= 18.09 - [How install Docker](https://docs.docker.com/get-docker/)
- Docker Compose >= 1.24 [How install Docker Compose](https://docs.docker.com/compose/install/)
- Allure Cliente >= 2.9 [how install allure](https://docs.qameta.io/allure/#_commandline)

## Getting Started
Install dependencies:

```bash
$ make setup
```
Start Zalenium server:
```bash
$ make zalenium
```
## Config
In this project all the settings of the webdriver are in the file [browser.py](https://github.com/Schveitzer/selenium-python-bdd-behave-example/blob/master/tests/browser.py)

The behave settings are in the file [behave.ini](https://github.com/Schveitzer/selenium-python-bdd-behave-example/blob/master/behave.ini)

## To run tests:
```bash
$ make tests
```

## Live preview of your running tests

> http://localhost:4444/grid/admin/live
 
## Reports
Run the command below to generate the test report in the folder `./test-report/allure-report`:

```bash
$ make report.generate
```

To view the report in the browser, run the command:

```bash
$ make report.open
```
## Lint Code
To lint the code, run:

```bash
$ make code.lint
```
## Behave Context and environment.py
Variable of "context" in Behave is a place where you can store information to share for all tests, this is very useful for the easy reuse of pages, functions and information.
 
It is through the context variable that we will pass the pages between tests, so it is easier to reuse without the need to instantiate each class in each step or tests that is necessary.

Behave's context variables as well as the functions to be executed before, during and after the tests, are stored in the file   [environment.py](https://github.com/Schveitzer/selenium-python-bdd-behave-example/blob/master/tests/environment.py)

```Python
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
```
## Pages and Singleton
The pages will be transmitted through the context variables, the context variables are managed by Behave itself, many times the Behave management ends up instantiating the same class repeatedly, which causes crashes and unnecessary use of resources, to avoid this type of problem it is very important that the Design Pattern Singleton is implemented, where we will prevent the class from being instantiated again if it already exists.

In this project, the Singleton pattern is implemented as shown below, where the class instance is stored in a constant that is used by the context of Behave and other classes.

There are several ways to implement the Singleton pattern and instantiate classes in Python, but this way it is easier and simpler to share the pages between tests, where we do not need to extend the class to each step or function.

[login_page.py](https://github.com/Schveitzer/selenium-python-bdd-behave-example/blob/master/tests/pages/login_page.py)
```python
from selenium.webdriver.common.by import By
from browser import Driver

class LoginPage(Driver):

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def button_login(self):
        return self.driver.find_element(By.CLASS_NAME, "login")

LOGIN_PAGE = LoginPage.get_instance()

```
## Locator strategy

The strategy to locate the elements aims to facilitate their reuse between the various step files, an example of an element on the login page:

```python
    def button_submit_message(self):
        return self.driver.find_element(By.ID, "submitMessage")
		
```

## Helpers, Data and Constants

In the project a class called Helper was created, in it we will have functions that will be shared among all tests.

The data such as login credentials have been stored and a Json file, this file is loaded by the credentials.py file, this facilitates the maintenance and use of data that will be shared between the tests.

And in the constants folder we have Python files that contain the system constants, that is, messages, labels and other elements of the application that will be consumed by the tests.

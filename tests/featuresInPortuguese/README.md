# WebdriverIO Appium Cucumber boilerplate 

Neste projeto demonstro como usar o Selenium WebDriver com o Behave para automação de testes de interface web usando conceitos de BDD
Para os assertions foi feito o uso do Nose.

Este projeto inclui:

- Framworks:
    - Selenium
    - Behave
    - Nose

- Features:
    - Page Object
    - Relatórios com Allure (Print em caso de falha)
    - Lint de código com Pylint
    - Comandos simples com Make
   
## Pré-requisitos
- Python >= 3.6 - [Como instalar Pytohn](https://www.python.org/downloads/)
- Pip >= 20.0.x - [Como instalar pip](https://pip.pypa.io/en/stable/installing/)
- Docker >= 18.09 - [Como instalar o Docker](https://docs.docker.com/get-docker/)
- Docker Compose >= 1.24 [Como instalar o Docler Compose](https://docs.docker.com/compose/install/)
- Allure Cliente >= 2.9 [Como instalar allure](https://docs.qameta.io/allure/#_commandline)

## Começando
Instale as dependências:

```bash
$ make setup
```
Inicie o servidor do Zalenium:
```bash
$ make zalenium
```

## Configurações
Neste projeto todas as configurações do webdriver estão no arquivo [browser.py](./tests/browser.py)

As configurações do behave estão no arquivo [behave.ini](./behave.ini)

## Para executar os testes:
>Substituir as pastas: features e steps, pelas contidas na pasta featureInPortugues.
>
>Descomentar a linha 9 do behave.ini

```bash
$ make tests
```

## Para acompanhar a execução dos testes

> http://localhost:4444/grid/admin/live

## Relatório
Execute o comando abaixo para gerar o relatório dos testes na pasta `./test-report/allure-report`:

```bash
$ make report.generate
```

Para visualizar o relatório no navegador execute o comando:

```bash
$ make report.open
```
## Lint do código
Para executar o lint no código execute:

```bash
$ make code.lint
```
## Behave Context e environment.py
 Avariável de "context" no Behave é um lugar onde você poderá armazenar informações para compartilhar por todos os testes, isso é muito útil para o reuso fácil de páginas, funções e informações.
 
 É através da variável de contexto que vamos passar as páginas entre os testes, dessa forma fica mais fácil o reuso sem a necessidade de instanciar cada classe em  cada step ou testes que for necessário.

As variáveis de contexto do Behave assim como as funções a serem executadas antes, durante e após os testes, ficam armazenadas no arquivo  [environment.py](./tests/environment.py)

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
## Páginas e Singleton
As páginas serão transmitidas através das variáveis de contexto, as variáveis de contexto são gerenciadas pelo próprio Behave, muitas vezes o gerenciamento do Behave  acaba instanciando a mesma classe repetidas vezes, o que causa travamentos e uso desnecessário de recursos, para evitar este tipo de problema é muito importante que seja implementado o Design Pattern Singleton, onde vamos evitar que a classe seja instanciada novamente caso ela já exista.

Neste projeto o padrão Singleton é implementado da forma mostrada abaixo, onde a instância da classe é armazenada em uma constante que é usada pelo contexto do Behave e outras classes.

Existem várias formas de se implementar o padrão Singleton  e instanciar classes no Python, porém desta forma fica mais fácil e simples compartilhar as páginas entre os testes, onde não precisamos ficar estanciado a classe a cada step ou função.

[login_page.py](./tests/pages/login_page.py)
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
## Estratégia para localizar, obter e utilizar os elementos
A estratégia para localizar os elementos visa facilitar o reuso dos mesmos entre os vários arquivos de steps, exemplo de um elemento da página de login:

```python
    def button_submit_message(self):
        return self.driver.find_element(By.ID, "submitMessage")
		
```

## Helpers, Dados e Constantes
No projeto foi criado um classe chamada Helper, nela vamos ter funções que serão compartilhadas entre todos os testes.

Os dados como por exemplo a credenciais de login foram armazenadas e um arquivo Json, esse arquivo é carregado pelo arquivo credentials.py, isto facilita a manutenção e uso de dados que serão compartilhados entre os testes.

E na pasta constants temos arquivos Python que contém as constante do sistema, isto é, mensagens, labels e outros elementos da plicação que serão consumidos pelos testes.

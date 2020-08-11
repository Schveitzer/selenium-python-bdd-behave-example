# Created by Alan Schveitzer at 05/08/2020
# language: pt
# -- file:*.feature

Funcionalidade: Sending message to customer service

    Contexto:
        Dado eu estou na página de login
          E eu estou logado com o usuário: 'User 1'

    @trivial
    Cenário: Exibe a página de envio de mensagens
        Quando eu clico no botão contato para abrir a página de contato
        Então sistema exibe o título da página de contato

    @normal
    Cenário: Envia mensagem com anexo
        Quando eu clico no botão contato para abrir a página de contato
            E eu envio uma mensagem com documento
        Então sistema exibe mensagem de menssagem enviada com sucesso
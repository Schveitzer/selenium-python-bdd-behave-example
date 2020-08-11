# Created by Alan Schveitzer at 05/08/2020
# language: pt
# -- file:*.feature

Funcionalidade: Validações no login

    Contexto:
        Dado que eu limpo os dados de navegação
          E eu estou na página de login

    @normal
    Esquema do Cenário: Exibe mensagem de aviso, ao fazer login com credenciais inválidas
        Quando eu tento fazer login com os dados; email: '<Email>' e senha: '<Senha>'
        Então sistema exibe mensagem informando que dados são invalidos

      Exemplos:
        | Email             | Senha  |
        | admin1.it@chk.com | 12346. |
        | admin1.it@chk.com | /12346 |

    @critical
    Cenário: Exibe login realizado com sucesso, ao informar credenciais válidas
        Quando eu faço login com o usuário: 'User 1'
        Então sistema exibe mensagem de boas vindas
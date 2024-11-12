# Defina um usuário e senha, e depóis verifique se o login do usuário é
# valido

USUARIO = 'my'
SENHA = '123'

while True:
    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')

    if USUARIO == usuario and SENHA == senha:
        print('LOGIN ACEITO!!!')
        break
    print('ERROR: Usuário e/ou Senha INVALIDOS')

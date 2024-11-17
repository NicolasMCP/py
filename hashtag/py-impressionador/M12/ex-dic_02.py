print('Para lembrar uso com update\n---------------------------')

dicionario = {}

print('INCLUSÃO: update')
dicionario.update({'nome': 'Nome do Fulano', 'endereco': 'Rua tal e qual', 'email': 'Fulano@email.com'})

print(f'o conteúdo do dic. é: {dicionario}\n')

print('ATUALIZA: também com update')
dicionario.update({'nome': 'Ciclano', 'endereco': 'Rua do Ciclano', 'email': 'Ciclano@email.com'})

print(f'o conteúdo do dic. é: {dicionario}')

print('Para lembrar uso direto, com a chave\n------------------------------------')

dicionario = {}

print('INCLUSÃO: por ser a primeira vez, inclui (visto que nenhuma das chaves existem)')
dicionario['nome'] = 'Nome do Fulano'
dicionario['endereco'] = 'Rua tal e qual'
dicionario['email'] = 'Fulano@email.com'

print(f'o conteúdo do dic. é: {dicionario}\n')

print('ATUALIZA: quando as chaves já existem, os dados são atualizados')
dicionario['nome'] = 'Ciclano'
dicionario['endereco'] = 'Rua do Ciclano'
dicionario['email'] = 'Ciclano@email.com'

print(f'o conteúdo do dic. é: {dicionario}')

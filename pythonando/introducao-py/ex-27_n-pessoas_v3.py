# Faça um programa que o usuário possa cadastrar n pessoas
# armazenando nome, idade, rg

pessoas = []
nome = input('Digite o nome: ')  # *
while nome.strip() != '':        # *
    pessoa = {'nome': nome,
              'idade': input('Digite a idade: '),
              'RG': input('Digite o RG: ')}
    pessoas.append(pessoa)
    print()
    nome = input('Digite o nome: ')

print('\n' + ('\n\n'.join('\n'.join(f"'{chave}': '{conteudo}'" for chave, conteudo in pessoa.items()) for pessoa in pessoas)) + '\n\nFim do programa')

# * Contribuição de Evandro Neto (Comunidade Pythonando, Discord)
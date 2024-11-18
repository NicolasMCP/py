# Faça um programa que o usuário possa cadastrar n pessoas
# armazenando nome, idade, rg

pessoas = []
while True:
    nome = input('Digite o nome: ')
    if nome.strip() != '':
        pessoa = {'nome': nome,
                  'idade': input('Digite a idade: '),
                  'RG': input('Digite o RG: ')}
        pessoas.append(pessoa)
        print()
    else:
        for pessoa in pessoas:
            print()
            for chave, conteudo in pessoa.items():
                print(f"'{chave}': '{conteudo}'")
        print()
        print('Fim do programa')
        break

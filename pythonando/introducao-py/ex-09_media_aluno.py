# Receber 4 notas de um aluno e exiba se ele foi aprovado 
# (nota maior ou igual que 6)
# se ele ficou de recuperação (nota maior ou igual a 4) ou
# se ele foi reprovado (nota menor que 4)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terçeira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f'Aprovado com a Media: {media}')
elif media >= 4:
    print(f'Recuperação com a Media: {media}')
else:
    print(f'Reprovado com a Media: {media}')

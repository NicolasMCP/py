# Receba um número e exiba se ele é positivo ou negativo

num = float(input('Digite um número: '))

if num > 0:
    print(f'O número {num} é Positivo!')
elif num < 0:
    print(f'O número {num} é Negativo!')
else:
    print(f'O número {num} é Neutro!')

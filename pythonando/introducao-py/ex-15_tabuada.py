# Receba um número do usuário e mostre a tabuada desse número

x = int(input('Digite a tabuada do: '))

i = 0
while i < 12:
    i += 1
    print(f'{i} x {x} = {i*x}')


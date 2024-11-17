import random

print('\nUsando números inteiros apenas por didática\n')

print('Exemplo 1\n')

x = [f'5 x {i} = {i*5}' for i in range(1, 11)]
print(*x,sep='\n')

print('\nExemplo 2\n')

y = [random.randint(500, 2000) for i in range(10)]
print(y)

print('Cobrar 90% de imposto nos que forem de 1000 ou mais...')
l = [int(i * 1.9) if i >= 1000 else i for i in y]
print(l)

print('\nExemplo 3 - Mantenha apenas os valores até 2500 da última lista')
z = [i for i in l if i <= 2500]
print(z)

print()

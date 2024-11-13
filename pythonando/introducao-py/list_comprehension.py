import random

# estou usando números inteiros apenas por didática

print('\nExemplo 1\n')

x = [f'5 x {i} = {i*5}' for i in range(1, 11)]
print(x)

print('\nExemplo 2\n')

y = [random.randint(500, 2000) for i in range(10)]
print(y)

# cobrar 90% de imposto nos que forem de 1000 ou mais
l = [int(i * 1.9) if i >= 1000 else i for i in y]
print(l)

print('\nExemplo 3\n')

# preserve somente os valores até 2500 usando a lista 'l'
z = [i for i in l if i <= 2500]
print(z)

print()

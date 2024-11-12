nomes = ['Cristina', 'Nícolas', 'Alejandra', 'Lujan', 'Silvia', 'Macarena', 'Estela', 'Guadalupe']

print('_'*90, end='\n\n')

for i in nomes:
    print(f'Nome: {i}')

print('_'*90, end='\n\n')

for i, n in enumerate(nomes):
    print(f'Nome_{i+1}: {n}')

print('_'*90, end='\n\n')

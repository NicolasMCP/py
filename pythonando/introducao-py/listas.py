nomes = ['Cristina', 'Nícolas', 'Lujan', 'Silvia', 'Estela', 'Macarena', 'Alejandra', 'Guadalupe']

print('_'*90, end='\n\n')

for i in nomes:
    print(f'Nome: {i}')

print('_'*90, end='\n\n')

for i, n in enumerate(nomes):
    print(f'Nome {i+1}: {n}')

print('_'*90, end='\n\n')

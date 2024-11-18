print('Inserindo dados 1o trimestre')
fat_1_trimestre = {'jan': 200000,
                   'fev': 160000,
                   'mar': 205000}
print(f'O faturamento em março foi de: {fat_1_trimestre['mar']}')
print('Os valores do dicionario do 1o trimestre são: ', fat_1_trimestre.values())
print(f'Faturamento do 1o trimestre', sum(fat_1_trimestre.values()))

fat_semestre = fat_1_trimestre.copy()
fat_semestre.update({'abr': 180000,
                     'mai': 201000,
                     'jun': 222000})
print('Semestre')

print('\nChaves', fat_semestre.keys())

print('\nValores', fat_semestre.values())

print(*fat_semestre.items(),sep='\n')
# como vimos antes, faz o update do valor
fat_semestre['mai'] = 188000

print(*fat_semestre.items(),sep='\n')
print('errei a chave, coloquei o \'M\' maiúsculo...')
fat_semestre['Mai'] = 188888
print('muito cuidado com isto... o dic entende como uma chave totalmente diferente')
print(*fat_semestre.items(),sep='\n')

print('\nMesmo ao criar ele não aceita 2 chaves iguais, veja...')
fat_2o_semestre = {'jul': 130000,
                   'ago': 120000,
                   'set': 300000,
                   'out': 199000,
                   'nov': 260000,
                   'dez': 500000,
                   'set': 333000}
print('\nVeja que fica somente o último valor dado a Setembro')
print(*fat_2o_semestre.items(),sep='\n')


# Receba 'M' para Masculino e 'F' para Feminino, e exiba o sexo da pessoa

sexo = input('Digite o sexo (M/F):')

if sexo == 'F' or sexo == 'f':
    print('Sexo: Femenino')
elif sexo == 'M' or sexo == 'm':
    print('Sexo: Masculino')
else:
    print('Campo Sexo MAL INFORMADO!')

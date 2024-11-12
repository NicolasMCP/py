# Receba 'F' para Feminino e 'M' para Masculino, e exiba o sexo da pessoa

sexo = input('Digite o sexo (F/M):')

if sexo == 'F' or sexo == 'f':
    print('Sexo: Femenino')
elif sexo == 'M' or sexo == 'm':
    print('Sexo: Masculino')
else:
    print('Campo Sexo MAL INFORMADO!')

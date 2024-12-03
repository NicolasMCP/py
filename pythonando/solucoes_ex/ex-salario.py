# 2 - Salário
# Nível: 1
# Faça um Programa que leia quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato:
# ***********
# * Entrada *
# ***********
# O arquivo de entrada contém 2 valores de ponto flutuante.
# ***********
# *  Saída  *
# ***********
# Exiba os seguintes dados arrendondados para baixo exatamente como na tabela
# abaixo:
# Exemplos de entradas      Exemplos de saídas
# 120                       Salario bruto: 14760
# 123                       INSS: 1180
#                           SINDICATO: 738
#                           Salario liquido: 11217
#
#

valor_hora = float(input())
qtde_horas = float(input())

salario_bruto = valor_hora * qtde_horas
ir = salario_bruto * .11
inss = salario_bruto * .08
sindicato = salario_bruto * .05

print(f'Salario bruto: {int(salario_bruto)}')
print(f'INSS: {int(inss)}')
print(f'SINDICATO: {int(sindicato)}')
print(f'Salario liquido: {int(salario_bruto - ir -inss -sindicato)}')
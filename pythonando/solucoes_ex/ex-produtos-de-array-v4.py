# 9 - Produtos de arrays
# Dado um array de inteiros nums , retorne um array output onde output[i] é o
# produto de todos os elementos de nums exceto nums[i] .
# ************
# * Entradas *
# ************
# A primeira linha representa todos os números do array separados por um
# espaço
# ************
# *  Saídas  *
# ************
#
# Exemplo de entradas       Exemplo de saídas
# -------------------------------------------
# 1 2 3 4                   [24, 12, 8, 6]
# -------------------------------------------
# Exemplo de entradas       Exemplo de saídas
# 4 2 3 4                   [24, 48, 32, 24]
#
#
from functools import reduce

produto = lambda num: reduce(lambda x, y: x * y, num)

entrada = list(map(int, input().split()))
saida = []
for i in range(len(entrada)):
    if i == 0:
        temp = entrada[1:]
    elif i == len(entrada):
        temp = entrada[:len(entrada)-2]
    else:
        temp = entrada[:i] + entrada[i + 1:]
    # print(temp)
    saida.append(produto(temp))

print(saida)

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///
#
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
# PARA RODAR O CÓDIGO PYTHON sem complicação use:
# nu run ex-produtos-de-array.py

from numpy import prod

entrada = list(map(int, input().split()))

saida = []
for i in range(len(entrada)):
    entrada_c = entrada.copy()
    entrada_c.pop(i)
    saida.append(int(prod(entrada_c)))

print(saida)

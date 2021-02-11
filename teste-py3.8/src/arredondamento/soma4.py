# Nícolas Ramos
# soma com Decimal, tudo certo (sem problemas de arredondamento, mesmo usando decimais)

from decimal import Decimal


def soma(a, b):
    return a + b


print('1.3 + 2.1 = ', end='')
print(soma(Decimal("1.3"), Decimal("2.1")))

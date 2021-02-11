# Nícolas Ramos
# soma com inteiros, tudo certo (dividindo depois para considerar 2 casas decimais)

def soma(a, b):
    return soma_int(a * 100, b * 100)


def soma_int(x: int, y: int):
    return (x + y) / 100


print('1.3 + 2.1 = ', end=f'')
print(soma(1.3, 2.1))

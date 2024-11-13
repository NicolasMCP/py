# Receba 10 valores (int) e exiba a soma de todos eles

x = [int(input(f'{i} num.: ')) for i in range(1,11)]
print(f'A soma é: {sum(x)}')

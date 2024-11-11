# Receba 3 numeros inteiros e exiba o maior deles.

# Versão 2, considerando numeros iguais

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = int(input('Digite o terceiro número inteiro: '))
print()

if num1 == num2 == num3:
    print(f'Todos os valores são iguais: {num1}')
elif num1 > num2:
    if num1 > num3:
        print(f'O maior é primeiro número, com o valor: {num1}')
    elif num1 == num3:
        print(f'Os maiores são o primeiro e o terceiro número, com o valor: {num1}')
    else:
        print(f'O maior é terceiro número, com o valor: {num3}')
elif num1 == num2 and num1 > num3:
    print(f'Os maiores são o primeiro e o segundo número, com o valor: {num1}')
elif num2 > num3:
    print(f'O maior é segundo número, com o valor: {num2}')
elif num2 == num3:
    print(f'Os maiores são o segundo e o terceiro número, com o valor: {num2}')
else:
    print(f'O maior é terceiro número, com o valor: {num3}')

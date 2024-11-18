# Receba 3 numeros inteiros e exiba o maior deles.

# Versão 3, refatorado após ver aula, sem considerar numeros iguais

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = int(input('Digite o terceiro número inteiro: '))
print()

if num1 > num2 and num1 > num3:
    print(f'O maior é primeiro número, com o valor: {num1}')
elif num2 > num3 and num2 > num1:
    print(f'O maior é segundo número, com o valor: {num2}')
elif num3 > num1 and num3 > num2:
    print(f'O maior é terceiro número, com o valor: {num3}')

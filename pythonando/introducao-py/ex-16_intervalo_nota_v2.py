# Escreva um programa que receba notas de um aluno (0-10), caso a nota
# esteja fora desse intervalo peça para o profesor digitar novamente

while True:
    nota = int(input('Digite a nota do Aluno (0-10): '))
    if nota >= 0 and nota <= 10:
        print(f'Nota do Aluno {nota}')
        break
    print(f'Nota {nota}, fora do intervalo, corrija.')












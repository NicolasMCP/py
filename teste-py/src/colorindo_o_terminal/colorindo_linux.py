# Nícolas Ramos
# impressão colorida no console linux,
# para windows tem que incluir a biblioteca ansi no config.sys
# device=ANSI.SYS

print('meu programa em python')
a = 2
b = 3
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'

cor_padrao = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'

fundo_preto = '\033[40m'
fundo_vermelho = '\033[41m'
fundo_verde = '\033[42m'
fundo_amarelo = '\033[43m'
fundo_azul = '\033[44m'
fundo_magenta = '\033[45m'
fundo_ciano = '\033[46m'
fundo_branco = '\033[47m'

print(f'{vermelho}primeiro número: {a}\n'
      f'{amarelo}segundo número: {b}\n'
      f'{azul}soma: {soma}\n'
      f'{ciano}subtração: {subtracao}\n'
      f'{cor_padrao}{negrito}multiplicação: {multiplicacao}\n{cor_padrao}'
      f'{preto}divisão: {divisao}\n'
      f'{magenta}resto: {resto}{cor_padrao}')

print('----------------------------------')
print(f'{vermelho}vermelho')
print(f'{verde}verde')
print(f'{azul}azul')
print(f'{ciano}ciano')
print(f'{magenta}magenta')
print(f'{amarelo}amarelo')
print(f'{preto}preto')
print(f'{branco}branco{cor_padrao}')
print(f'{negrito}negrito (da cor_padrao){cor_padrao}')
print(f'{reverso}reverso (da cor_padrao){cor_padrao}')

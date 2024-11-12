'''
# 0 a 4
for i in range(0,5):
    print(i,end=' ')

print()
print('-'*90)

# 2 a 100 (pares)
for i in range(2,101,2):
    print(i,end=' ')

print()
print('-'*90)

# 40 a 2 (pares)
for i in range(40,1,-2):
    print(i,end=' ')

print()
print('-'*90)

# iterando lista
x = [2, 7, 'x', 'z', 45, 47, -12]
for i in x:
    print(i,end=' ')

print()
print('-'*90)

nome = input('Digite seu nome: ')
for i in nome:
    print(i,end=', ')
'''
print()
print('-'*90)

for i in range(2,10):
    print(f'\n[Tabuada {i}]\n')
    for x in range(1,11):
        print(f'{x} x {i} = {x*i}')

print()
print('-'*90)

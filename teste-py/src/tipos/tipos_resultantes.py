# Nícolas Ramos
# alguns detalhes que podem enganar

print(type(3 + 18 / 3))
# o resultado numerico é nove redondo, mas é um int ou um float ?
# observe...

a = 54
b = 3
print(type(15 + a / b))


# veja a diferença
print(3 + 18 / 3)
print(15 + a / b)
print(type(3 + 18 // 3))
print(type(15 + a // b))
print(3 + 18 // 3)
print(15 + a // b)

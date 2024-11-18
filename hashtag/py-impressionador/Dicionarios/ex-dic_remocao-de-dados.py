fat_2o_semestre = {'jul': 130000,
                   'ago': 120000,
                   'set': 300000,
                   'out': 199000,
                   'nov': 260000,
                   'dez': 500000}
fat_bk = fat_2o_semestre.copy()
print(fat_2o_semestre)
# simplesmente descarta o item de setembro
del fat_2o_semestre['set']

print(fat_2o_semestre)
# com o pop eu posso guardar o valor do item que esta sendo deletado
dez = fat_2o_semestre.pop('dez')

print(fat_2o_semestre)
print(f'O mês de dez era: {dez}')

print('--> Vejamos depois de fat_2o_semestre.clear()')
fat_2o_semestre.clear()
print(fat_2o_semestre)
fat_2o_semestre = fat_bk.copy()
print('Votando todos os dados')
print(fat_2o_semestre)
print('mas o que acontece se eu usar: "del fat_2o_semestre"')

del fat_2o_semestre
print(fat_2o_semestre)
# ERRO CODE 1
# NameError: name 'fat_2o_semestre' is not defined

from datetime import datetime

estranhos = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
             21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
             41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

minuto_atual = datetime.today().minute

if minuto_atual in estranhos:
    print("Este é um miuto um pouco estranho.")
else:
    print("Não, este não é um minuto estranho.")

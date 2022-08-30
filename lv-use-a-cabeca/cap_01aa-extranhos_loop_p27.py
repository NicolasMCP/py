import time
from datetime import datetime

extranhos = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
             21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
             41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for ciclo in range(20):
    minuto_atual = datetime.today().minute

    if minuto_atual in extranhos:
        print("Este é um minuto um pouco extranho.")
    else:
        print("Este não é um minuto extranho.")

    time.sleep(10)

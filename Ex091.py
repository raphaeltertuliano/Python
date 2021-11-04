#Crie um programa onde 4 jogadores um dado e tenham
#resultados aleatórios.
##Guarde esse resultados em um dicionário. No final, coloque esse
#dicionário em ordem ,sabendo que o vencedor tirou o maior número na dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}
for j, d in jogadores.items():
    print(f'{j} tirou {d} no dado')
    sleep(1)
print('-=' * 20)
print('-----RANKING-----')
sleep(1)
ranking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')


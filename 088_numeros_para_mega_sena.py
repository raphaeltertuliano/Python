#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear
#6 números de 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
jogos = []
lista = []
tot = 1
quant = int(input('Quantos jogos da MEGA SENA deseja fazer?: '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 17)
for i, u in enumerate(jogos):
    print(f'Jogo {i+1} = ', end='')
    print(f'{u}')
print('-=' * 17)

#Melhore o DESAFIO 061, perguntando para o usuário se ele quer
#mostrar mais algum termo.
#O programa encerra quando ele disser que quer mostrar 0 termos.
from time import sleep
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
opção = 1
while opção > 0:
    while cont <= 10:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
        sleep(0.5)
    print('FIM')
    print('''Mostrar outro termo? 
[ 1 ] - SIM
[ 0 ] - Não''')
    opção = int(input('Opção: '))
    if opção == 1:
        primeiro = int(input('Primeiro termo: '))
        razão = int(input('Razão: '))
        termo = primeiro
        cont = 1
        while cont <= 10:
            print(f'{termo} -> ', end='')
            termo += razão
            cont += 1
            sleep(0.5)
        print('FIM')
print('Obrigado. Volte sempre')

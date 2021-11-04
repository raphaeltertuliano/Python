#Faça um programa que jogue par ou impar com o computador. O jogo só será
#interrompido quando o jogador PERDER, mostrando o total de vitoria consecutivas
#que ele conquistou no final do jogo.

from random import randint
j = c = je = ce = soma = cont = jogadas = 0
print('-='*20)
print(f'{"Jogo do Par ou impar":^40}')
print('-='*20)
while True:
    while True:
        print('''Você quer par ou impar?
[ 1 ] - PAR
[ 2 ] - IMPAR''')
        j = int(input('Qual você escolhe?: '))
        if j > 2 or j <= 0:
            print('\033[31mOpção inválida. Tente novamente\033[m')
        if j == 1:
            j = 'PAR'
            c = 'IMPAR'
            print('Você escolheu PAR')
            break
        if j == 2:
            j = 'IMPAR'
            c = 'PAR'
            print('Você escolheu IMPAR')
            break
    while True:
        je = int(input('Qual o número que você quer?: '))
        if j == 'PAR' and je % 2 != 0:
            print('\033[31mEscolha somente números pares\033[m')
        if j == 'PAR' and je % 2 == 0:
            break
        if j == 'IMPAR' and je % 2 != 0:
            break
        if j == 'IMPAR' and je % 2 == 0:
            print('\033[31mEscolha somente números impares\033[m')
    ce = randint(1, 20)
    soma = je+ce
    print(f'Você escolheu \033[34m{je}\033[m e o computador escolheu \033[34m{ce}\033[m. ', end='')
    print(f'Total \033[33m{soma}\033[m')
    if j == 'PAR' and soma % 2 == 0:
        cont += 1
        jogadas += 1
    if j == 'PAR' and soma % 2 != 0:
        jogadas += 1
        break
    if j == 'IMPAR' and soma % 2 == 0:
        jogadas += 1
        break
    if j == 'IMPAR' and soma % 2 != 0:
        cont += 1
        jogadas += 1
print('-'*55)
print(f'Você ganhou {cont} vezes consecutivas e fez {jogadas} jogadas')
print('-'*55)

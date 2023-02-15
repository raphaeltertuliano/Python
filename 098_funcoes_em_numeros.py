#Faça um programa que tenha uma função chamada contador(), que receba três
#parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que
#ralizar três contagens através da função criada:
#A)- de 1 a 10 contando de 1 em 1
#B)- de 10 a 0 contando de 2 em 2
#C)- Uma contagem personalizada

from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= p
        print('FIM')


contador(0, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar a contagem!')
ini = int(input('INICIO: '))
fim = int(input('FIM:    '))
pas = int(input('PASSO:  '))
contador(ini, fim, pas)

#Faça um programa que tenha uma função chamada maior(), que receba
#vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos e dizer qual deles é o maior.
from time import sleep
def maior(*numeros):
    print('Analisando os valores...')
    cont = maior = 0
    for elemento in numeros:
        print(f'{elemento} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = elemento
        else:
            if elemento > maior:
                maior = elemento
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado é {maior}')
    print('-=' * 20)


maior(4, 7, 3, 9)
maior(3, 8, 5)
maior(3, 7)
maior(6)
maior()

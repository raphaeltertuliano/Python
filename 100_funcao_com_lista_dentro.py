#Faça um programa que tenha uma lista chamada números e duas funções
#chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
#e vai coloca-los dentro da lista e o segunda função vai mostrar a soma
#entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia(lista):
    """
    Sorteia números aleatórios e coloca ele em uma lista
    :param lista: Uma lista aleatória de 5 números
    :return:Sem um retorno específico
    Função criada por Gustavo Guanabara do curso em Vídeo
    """
    print('Sorteando os 5 valores de lista:', end='')
    for contador in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
help(sorteia)

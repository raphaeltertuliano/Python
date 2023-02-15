#Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
#depois disso, mostre a listagem de números gerados e também
#o maior e o menor que estão na tupla

from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f's valores sorteados foram: {num}')
print(f'O maior número da lista é {max(num)}')
print(f'O menor número da lista é {min(num)}')

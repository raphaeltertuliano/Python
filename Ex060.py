#Faça um programa que leia um número qualquer e mostre o seu fatorial
#EX: 5! = 5x4x3x2x1=120
#PS: usei o laço for, porque eu sei o limite que começa e que termina
from math import factorial
n = int(input('Digite um número para saber o seu Fatorial: '))
c = 0
f = factorial(n)
print(f'{n}! >>> ', end='')
for c in range(n, 0, -1):
     print(f'{c} ', end='')
     print('X ' if c > 1 else '=', end='')
print(f' {f}')


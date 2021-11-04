#Escreva um programa que leia um número n inteiro e mostre na tela
#os n primeiros elemento de uma sequencia de Fibonacci
#Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termosmostrar?: '))
t1 = 0
t2 = 1
cont = 3
print('~' * 30)
print(f'{t1} -> {t2}', end='')
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}',end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' -> FIM')
print('~' * 30)

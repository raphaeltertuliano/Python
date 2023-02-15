#Faça um programa que leia um número inteiro e diga
#se ele é ou não um número primo
tot = 0
num = int(input("digite um número inteiro: "))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {num} foi divisivel {tot} vezes')
if tot == 2:
    print('Por tanto, ELE É PRIMO')
else:
    print('Por tanto, ELE NÃO É PRIMO')

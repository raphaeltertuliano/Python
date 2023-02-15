#Faça um programa que leia um ano e mostre se ele é BISSEXTO

a = int(input('Digite um ano: '))
if a % 4 == 0:
    print(f'O ano {a} é BISSEXTO')
else:
    print(f'O ano {a} NÃO É BISSEXTO')

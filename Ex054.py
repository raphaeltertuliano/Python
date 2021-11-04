#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atigiram
#a maioridade e quantas pessoas já são maiores

import datetime
maior = 0
menor = 0
for p in range(1, 8):
    pessoa = int(input(f'Ano de nascimento da {p}ª pessoa: '))
    if datetime.datetime.today().year - pessoa >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} pessoas são menores de idade')

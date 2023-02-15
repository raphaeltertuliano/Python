#Escreva um programa que pergunte o salário de um funcionário e calcule
#o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
#Para inferiores ou iguais, o aumento é de 15%

s = float(input('Salário atual do funcionário: R$'))
if s >= 1250:
    ns = ((s*10)/100)+s
    print(f'O novo salário é de: R${ns:.2f}')
else:
    ns = ((s*15)/100)+s
    print(f'O novo salário é de: R${ns:.2f}')

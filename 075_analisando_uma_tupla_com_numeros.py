#Desenvolva um programa que leia quatro valores pelo teclado
#e guarde-os em uma tupla. No final mostre:
#A)-Quantas vezes apareceu o valor 9
#B)-Em que posição foi digitado o primeiro valor 3
#C)-Quais foram os números pares

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'A lista é: {num}')
if num.count(9) == 0:
    print('Não foi digitado nenhum número 9')
else:
    print(f'O número 9 foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 aparece pela primeira vez na posição {num.index(3)+1}')
else:
    print('Não foi digitado nenhum número 3')
print('Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

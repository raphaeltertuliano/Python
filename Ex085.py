#Crie um programa onde o usuário possa digitar sete valores numéricos
#e cadastre-os em uma lista única que mantenha separados os valores
#pares e impares. No final, mostre os valores pares e impares
#em ordem crescente.

numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('Os valores pares em ordem crescente são: ', end='')
for w in numeros[0]:
    if w % 2 == 0:
        print(f'{w} ', end='')
print()
print('Os valores impares em ordem crescente são: ', end='')
for w in numeros[1]:
    if w % 2 != 0:
        print(f'{w} ', end='')

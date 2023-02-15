#Faça um programa que leia 5 valores e guarde-os em uma lista.
#No final, mostre qual foi o maior e qual foi o menor e quais foram as suas
#respectivas posições na lista.

valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont+1}º valor:')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(valores)
print(f'O maior valor é {maior} e está na posição ', end='')
for pos, num in enumerate(valores):
    if num == maior:
        print(f'{pos+1}...')
print(f'O menor valor é {menor} e está na posição ', end='')
for pos, num in enumerate(valores):
    if num == menor:
        print(f'{pos+1}...')

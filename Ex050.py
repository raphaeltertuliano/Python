#Desenvolva um programa que leia seis números inteiros e mostre a soma
#apenas daqueles que forem pares. Se o número for impara, desconsidere-o
soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você digitou {cont} números pares e a soma foi {soma}')

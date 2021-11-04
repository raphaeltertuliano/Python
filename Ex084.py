#Faça um programa que leia nome e peso de várias pessoas, guardando
#tudo em uma lista. No final mostre:
#A)- Quantas pessoas foram cadatradas
#B)- Uma listagem com as pessoas mais pesadas
#C)- Uma listagem com as pessoas mais leves

temp = []
pessoas = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    pessoas.append(temp[:])
    if len(pessoas) == 1:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    temp.clear()
    esc = str(input('Deseja continuar? [S/N]: '))
    if esc in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]} ', end='')

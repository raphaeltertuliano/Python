#Crie um programa que leia o nome e o preço de vários produtos.
#O programa devera perguntar se o usuário quer continuar.
#No final mostre:
#A) - Qual é o total gasto na compra.
#B) - Quantos produtos custam mais de R$1000,00
#C) - Qual é o nome do produto mais barato.
total = maisde1000 = maisbarato = cont = 0
nomemaisbarato = ''
print('-'*30)
print(f'{"LOJAS RAPHAEL":^30}')
print('-'*30)
while True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço do produto: R$'))
    total += p
    cont += 1
    if cont == 1:
        maisbarato = p
        nomemaisbarato = n
    else:
        if p < maisbarato:
            maisbarato = p
            nomemaisbarato = n
    if p > 1000:
        maisde1000 += 1
    while True:
        escolha = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if escolha == 'S':
            break
        if escolha == 'N':
            break
    print('-'*30)
    if escolha == 'N':
        break
print
print(f'O total gasto na compra foi R${total:.2f}')
print(f'Um total de {maisde1000} produtos custam mais de R$1000.00')
print(f'O produto mais barato é {nomemaisbarato} custando R${maisbarato:.2f}')

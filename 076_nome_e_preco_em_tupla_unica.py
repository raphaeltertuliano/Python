#Crie um programa que tenha uma tupla única com os nomes de produtos
#e seus respectivos preços na sequência. No final, mostre uma listagem
#de preços, organizando os dados de forma tabular
listagem = ('Pão', 10,
'Leite', 3.79,
'Presunto', 25.49,
'Mussarela', 42,
'Mortadela', 26,)
print('-'*40)
print(f'{"Tabela de preços":^40}')
print('-'*40)
for pos, c in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    if pos % 2 != 0:
        print(f'R${c:>7.2f}')
print('-'*40)

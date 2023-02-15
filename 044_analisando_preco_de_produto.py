#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o o seu preço normal e condição de pagamento:
#- Á vista dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- Em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros

valor = float(input('Valor do produto: R$'))
print('''Condições de pagamento:
[ 1 ] - Á vista dinheiro/cheque 10% de desconto
[ 2 ] - À vista no cartão de crédito: 5% de desconto
[ 3 ] - 2x no cartão
[ 4 ] - 3x no cartão ou mais (juros 20%)''')
cond = int(input('Forma de pagamento: '))
if cond == 1:
    novo_valor = valor-(valor*10)/100
    print(f'O produto custará: R${novo_valor:.2f}')
elif cond == 2:
    novo_valor = valor-(valor*5)/100
    print(f'O produto custará: R${novo_valor:.2f}')
elif cond == 3:
    print(f'O produto custará: R${valor:.2f}')
elif cond == 4:
    novo_valor = valor+(valor*20)/100
    print(f'O produto custará: R${novo_valor:.2f}')
else:
    print('\033[31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE')

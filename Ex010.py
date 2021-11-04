#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar
#valor do Dólar em 2021 = R$5,11

dinheiro = float(input('Quanto de dinheiro você tem na carteira?: R$'))
print(f'O valor é de R${dinheiro:.2f}')
print(f'Com esse valor da para comprar US${dinheiro/5.110:.2f}')
#Faça um algoritmo que leia o preço de um produto e
#mostre seu novo preço, com 5% de desconto

produto = float(input('Preço original do produto: R$'))
produto5 = (produto*5)/100
preçonovo = produto-produto5
print(f'O produto de R${produto:.2f}, vai para R${preçonovo:.2f}')

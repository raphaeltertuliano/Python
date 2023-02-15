#Escreva um programa que pergunte a quantidade de KM percorridos por um
#carro e a quantidade de dias que ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.

k = float(input('Quantos Kilometro rodados?: '))
d = float(input('Quantos dias o carro ficou alugado?: '))
vtotal = (k*60) + (d*0.15)
print(f'O preço total é de R${vtotal:.2f}')

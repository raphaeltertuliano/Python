#Escreva um progrma que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre um mensagem de que ele foi multado
#A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Velocidade do carro: '))
if v <= 80:
    print('Dentro do limite de velocidade. Boa viagem')
else:
    print(f'Velocidade: {v:.1f}Km/h. Acima do limite!')
    p = (v - 80)*7
    print(f'Você foi multado. Valor da multa: R${p:.2f}')

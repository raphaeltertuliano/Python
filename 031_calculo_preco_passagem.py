#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
#de até 200Km e R$0,45 para viagens mais longas

d = float(input('Distância da viagem[Em Km]: '))
if d <= 200:
    p = d * 0.50
    print(f'A viagem sairá por: R${p:.2f}')
else:
    p = d * 0.45
    print(f'A viagem sairá por: R${p:.2f}')

#Faça um programa que leia a altura e a largura de um parede em metros
#e calcule a sua área e a quantidade de tinta necessária para pinta-la,
#sabendo que cada litro de tinta, pinta uma área de 2m²

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
tinta = area/2
print(f'Esta parede tem {area:.3f}m² de área')
print(f'Para pinta-la serão necessários {tinta:.3f} litros de tinta')

#Faça um programa que tenha uma função chamada área(), que receba
#as dimensões de um terrono retangular(largura e comprimento) e
#mostre a área do terreno.

def área(a, b):
    areaterreno = a*b
    print('-='*20)
    print(f'A área de um terreno {a} X {b} = {areaterreno}M²')

print('-----MEDIDA DE TERRENOS-----')
lado1 = float(input('Largura (M): '))
lado2 = float(input('COMPRIMENTO (M): '))
área(lado1, lado2)

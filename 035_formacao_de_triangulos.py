#Desenvolva um programa que leia o comprimento de 3 retas
#e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas medidas formam um TRIÂNGULO')
else:
    print('Essas medidas NÃO FORMAM UM TRIÂNGULO')

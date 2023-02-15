#Faça um programa que leia o comprimento de um cateto oposto
#e de um cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa

import math
coposto = float(input('Medida de um cateto: '))
cadjacente = float(input('Medida do outro cateto: '))
hipotenusa = math.hypot(coposto, cadjacente)
print(f'A hipotenusa desse triâgulo é de: {hipotenusa:.2f}')

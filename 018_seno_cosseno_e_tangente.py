#Faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno, cosseno e tangente desse ângulo

import math
ang = float(input('Valor do ângulo a ser calculado: '))
print(f'O ângulo de {ang}° tem seno {math.sin(ang):.3f}, cosseno {math.cos(ang):.3f} e tangente {math.tan(ang):.3f}')

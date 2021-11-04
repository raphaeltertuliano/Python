#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
#diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
#e use algumas dessas funções.
from Ex107 import moeda
num = float(input('Digite um valor: R$'))
print(f'O valor de {num} aumentado em 10% é R${moeda.aumentar(num, 10)}')
print(f'O valor de {num} diminuido 13% é R${moeda.diminuir(num, 13)}')
print(f"O dobro de {num} é RS{moeda.dobro(num)}")
print(f'A metade de {num} é R${moeda.metade(num)}')
#Fiz o módulo moeda e o importei para usar suas funções
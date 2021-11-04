#Adapte o código do desafio 107, criando uma função adicional chamada moeda()
#que consiga mostrar os valores como um valor monetário formatado.

from Ex108 import moeda
num = float(input('Digite um valor: R$'))
print(f'O valor de {moeda.moeda(num)} aumentado em 10% é {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'O valor de {moeda.moeda(num)} diminuido 13% é {moeda.moeda(moeda.diminuir(num, 13))}')
print(f"O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}")
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')

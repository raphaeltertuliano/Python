#Modifique as funções que foram criadas no desafio 107
#para que elas aceitem um parâmetro a mais,
#informando se o valor retornado por elas vai ser ou não
#formatado pela função moeda() desenvolvida no desafio 108
from Ex109 import moeda
num = float(input('Digite um valor: R$'))
print(f'O valor de {moeda.moeda(num)} aumentado em 10% é {moeda.aumentar(num, 10, True)}')
print(f'O valor de {moeda.moeda(num)} diminuido 13% é {moeda.diminuir(num, 13, True)}')
print(f"O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}")
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')

#Crie um pacote utilidadeCeV que tenha dois módulos internos
#chamados moeda e dado.
#Transfira todas as funções utilizadas nos desafios 107, 108 e 109
#para o primeiro pacote e mantenha tudo funcionandofrom Ex111 import moeda
from Ex111.utilidadesCeV import moeda
num = float(input('Digite um valor: R$'))
moeda.resumo(num, 80, 35)

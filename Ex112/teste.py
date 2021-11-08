#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
#chamado dado. Crie um função chamada leiadinheiro() que seja capaz de funcionar
#como a função input(), mas com uma validação dos dados para aceitar apenas
#valores monetários.
from Ex112.utilidadesCeV import dado, moeda
num = dado.leiadinheiro('Digite um valor: R$')
moeda.resumo(num, 80, 35)

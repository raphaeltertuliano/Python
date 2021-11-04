#Escreva um programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo computador.
#O programa deverá escrever na tela
#se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('_____JOGO DA ADIVINHAÇÃO_____')
print('O computador escolherá um número!')
n = randint(0, 5)
print('Escolhendo...')
sleep(1.5)
print('Ja escolhi! Agora é a sua vez!')
u = int(input('Digite um número de 0 a 5: '))
if n == u:
    print('Usuário VENCEU! Parabens!')
else:
    print('Usuário PERDEU. Tente novamente!')
print(f'O computador escolheu {n} e o usuário escolheu {u}')

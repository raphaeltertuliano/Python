#Melhore o DESAFIO 028 onde o computador vai "pensar" em um número
#de 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.
palpite = 0
from random import randint
from time import sleep
print('_____JOGO DA ADIVINHAÇÃO_____')
print('O computador escolherá um número!')
n = randint(0, 10)
print('Escolhendo...')
sleep(1.5)
print('Ja escolhi! Agora é a sua vez!')
u = int(input('Digite um número de 0 a 10: '))
palpite += 1
if u < n:
    print('Mais... Tente novamente')
if u > n:
    print('Menos... Tente novamente')
while not n == u:
    u = int(input('Digite um número de 0 a 10: '))
    palpite += 1
    if u < n:
        print('Mais... Tente novamente')
    if u > n:
        print('Menos... Tente novamente')
print(f'Parabens, acertou. Você precisou de {palpite} palpites até acertar')


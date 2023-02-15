#Crie um programa que tenha uma tupla totalmente preenchida com uma
#contagem por extenso, de 0 até 20.
#Seu programa deverá ler um número  pelo teclado (entre 0 e 20) e
# mostra-lo por extenso

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número [0 a 20]: '))
    if num < 0 or num > 20:
        print('\033[31mDigite apenas números entre 0 e 20. Tente novamente\033[m')
    else:
        print(f'Você digitou o número {extenso[num]}')
        break

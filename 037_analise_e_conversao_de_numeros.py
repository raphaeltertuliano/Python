#Escreva um programa que leia um número inteiro qualquer e peça para
#o usuário escolher qual será a base de conversão
#-1 para Binário
#-2 para octal
#-3 para hexadecimal

n = int(input('Digite um número: '))
o = int(input(f'''Você deseja converter o número {n} para:
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal
Sua opção: '''))
if o == 1:
    print(f'{bin(n)[2:]}')
elif o == 2:
    print(f'{oct(n)[2:]}')
elif 0 == 3:
    print(f'{hex(n)[2:]}')
else:
    print('\033[31mOpção inválida. Tente novamente')

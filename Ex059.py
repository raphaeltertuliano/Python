#Crie um programa que leia dois valores e mostre um menu na tela
#[1] somar [2] multiplicar [3] maior [4] novos numeros [5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep
n3 = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while n3 != 5:
    print('''[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos números
[ 5 ] - Sair do programa''')
    n3 = int(input('O que deseja fazer agora?: '))
    if n3 == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
    elif n3 == 2:
        print(f'A multiplicação entre {n1} X {n2} é {n1*n2}')
    elif n3 == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
    elif n3 == 4:
        print('Vamos começar novamente :)')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif n3 == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente')
print('Obrigado. Volte sempre!')

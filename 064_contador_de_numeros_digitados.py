#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai para quando o usuário digitar 999, que é a condição de parada
#No final, mostre quantos números foram digitados e qual foi a soma entre eles.
#(Desconsiderando o flag)
soma = 0
digitados = 0
n = int(input('Digite um número inteiro [999 para parar]: '))
while n != 999:
    digitados += 1
    soma += n
    n = int(input('Digite um número inteiro [999 para parar]: '))
print(f'Você digitou {digitados} números e a soma entre ele é {soma}')

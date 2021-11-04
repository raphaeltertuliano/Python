#Crie um programa que leia vários números pelo teclado.
#No final da execução, mostre a média entre todos os valores
#e qual foi o menor e o maior valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
opção = 'S'
cont = soma = maior = menor = 0
while opção in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opção = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
média = soma / cont
print(f'Você digitou {cont} valores e a média é {média}')
print(f'O menor valor foi {menor} e o maior foi {maior}')

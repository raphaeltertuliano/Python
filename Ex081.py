#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso mostre:
#A)- Quantos números foram digitados.
#B)- A lista de valores, ordenada de forma decrescente
#C)- Se o valor 5 foi digitado e está ou não na lista

lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    while True:
        opção = str(input('Quer continuar? [S/N]: ')).upper()
        if opção == 'S':
            break
        elif opção == 'N':
            break
        elif opção not in 'SN':
            print('Opção inválida. Digite apenas S ou N')
    if opção == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {cont} números')
print(f'A lista em forma decrescente é {lista}')
if 5 in lista:
    print(f'O número 5 faz parte da lista')
else:
    print('O número 5 não faz parte da lista')

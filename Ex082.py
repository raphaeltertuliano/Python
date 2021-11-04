#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas valores pares
#e os valores impares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas

principal = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    principal.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
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
print(f'Lista principal de números: {principal}')
print(f'Lista dos números pares: {par}')
print(f'Lista dos números impares: {impar}')

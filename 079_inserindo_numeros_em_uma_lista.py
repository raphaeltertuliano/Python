#Crie um programa onde o usuário possa digitar vários valores numéricos
#e cadastro-los em uma lista. Caso o número já exista lá dentro,
#ele não será adicionado
#No final, serão exibidos todos os valores únicos, em ordem crescente.

numeros = []
while True:
    num = (int(input('Digite um número: ')))
    if numeros == '':
        numeros.append(num)
        print('Número adicionado com sucesso')
    elif num not in numeros:
        print('Número adicionado com sucesso')
        numeros.append(num)
    else:
        print('Número duplicado. Não vou adicionar')
    while True:
        opção = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if opção[0] in 'SN':
            break
        if opção not in 'SN':
            print("Opção inválida. Digite apenas S ou N")
    if opção[0] == 'N':
        break
numeros.sort()
print(f'Os números digitados foram: {numeros}')

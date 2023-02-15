#Faça um programa que leia o sexo de uma pessoa, mas só aceite
#os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
#até ter um valor correto.

sexo = 'c'
while not sexo in 'MF':
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo not in 'MF':
        print('Inválido. Tente novamente')

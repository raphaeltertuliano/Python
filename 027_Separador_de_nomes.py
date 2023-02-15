#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e último nome separadamente
#EX: Ana Maria de Souza
#primeiro = Ana
#último = Souza

n = str(input('Nome completo: ')).strip()
dividido = n.split()
print(f'O nome é: {n}')
print(f'Primeiro nome: {dividido[0]}')
print(f'Último nome: {dividido[-1]}')

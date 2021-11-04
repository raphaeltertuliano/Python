#Crie um programa que leia o nome de uma pessoa
#e diga se ela tem 'SILVA' no nome.

n = str(input('Digite o nome completo: ')).upper()
nome = n.strip().split()
print(f'O nome tem Silva?: {"SILVA" in nome}')

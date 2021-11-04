#Crie um programa que leia o nome de uma pessoa e mostre
#1) O nome com todas as letras maúsculas
#2) O nome com todas as letras minúscula
#3) Quantas letras ao todo(sem considerar os espaços)
#4) Quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo: '))
print(f'O nome todo em maiúsculo é: {nome.upper()}')
print(f'O nome todo em minúsculo é: {nome.lower()}')
dividido = nome.split()
dividido2 = ''.join(dividido)
print(f'O nome tem ao todo {len(dividido2)} letras')
print(f'O primeiro nome tem {len(dividido[0])} letras')


#Crie um programa que leia o nome de um cidade
#e diga se ele começa ou não com 'SANTO'.

cid = str(input('Digite o nome da cidade: ').strip())
nome = cid.upper().strip().split()
print('SANTO' in nome[0])

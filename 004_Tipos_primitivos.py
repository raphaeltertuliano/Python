#Crie um programa que leia algo pelo teclado e mostre o seu tipo primitivo
# e todas as informações possíveis sobre ele

s = input('Digite algo: ')
print(f'É um número?: {s.isnumeric()}')
print(f'É alfabético?: {s.isalpha()}')
print(f'É alfanumérico?: {s.isalnum()}')
print(f'Está escrito todo em maiúsculo?: {s.isupper()}')
print(f'Está escrito todo em minúsculo?: {s.islower()}')
print(f'A primeira letra é maiúscula?: {s.istitle()}')
print(f'São somente espaços?: {s.isspace()}')

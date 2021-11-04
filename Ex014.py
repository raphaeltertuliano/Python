#Escreva um programa que converta uma temperatura digitada em
# C° e converta para F°

c = float(input('Qual a temperatura em C°: '))
f = (c*(9/5))+32
print(f'A temperatura é: {f:.1f}F°')

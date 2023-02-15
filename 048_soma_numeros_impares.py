#Faça um programa que calcule a soma entre todos os números impares
#que são multiplos de 3 e que se encontram no intervalo de 1 até 500
cont = 0
soma = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            cont += c
            soma += 1
print(f'A soma dos {soma} valores solicitados é de {cont}')

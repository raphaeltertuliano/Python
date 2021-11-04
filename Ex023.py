#Faça um programa que leia de 0 a 9999 e mostre na tela
#cada um dos digitos separados
#EX: digite um número: 1834
#unidade: 4
#dezena 3
#centena: 8
#milhar: 1

num = int(input('Digite um número[0 a 999]: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num //1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

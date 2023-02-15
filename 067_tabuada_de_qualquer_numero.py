#Faça um programa que mostre a tabuada de vários números , um de cada vez,
#para cada valor digitado pelo usuário. O programa será interrompido quando
#o número solicitador for negativo.
n = 0
while True:
    n = int(input('Digite um número para saber a sua taboada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
        
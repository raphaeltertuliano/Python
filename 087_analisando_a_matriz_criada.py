#Aprimore o desafio anterior, mostrando no final:
#A)- A soma de todos os valores pares digitados
#B)- A soma dos valores da terceira coluna
#C)- O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
    scoluna += matriz[l][2]
    for c in range(0, 3):
        if c == 0:
            mai = matriz[1][c]
        elif matriz[1][c] > mai:
            mai = matriz[1][c]
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da terceira coluna é {scoluna}')
print(f'O maior valor sa segunda linha é {mai}')

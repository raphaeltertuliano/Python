#Refaça o desafio 035 dos triângulos, acrescentando o recurso
#de mostrar que tipo de triângulo será formado:
#- Equilátero: todos os lados iguais
#- Isósceles: dois lados iguais
#- Escaleno: todos os lados diferentes

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Essas medidas formam um triângulo EQUILÁTERO')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Essas medidas formam um triângulo ISÓSCELES')
    elif r1 != r2 != r3 != r1:
        print('Essas medidas formam UM triângulo ESCALENO')
else:
    print('Essas medidas não formam um triângulo')

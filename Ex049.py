#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
#escolher, só que agora utilizando um laço for

n = int(input('Digite um número para saber a sua taboada: '))
for c in range(1, 11):
    print(f'{n} X {c} = {n*c}')

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa mostre:
#-A média de idade do grupo
#-Qual é o nome do homem mais velho
#-Quantas mulheres tem menos de 20 anos
totidade = 0
homemidade = 0
homemnome = ''
totmulher = 0
for p in range(1, 5):
    print(f'_____{p}ª pessoa_____')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).upper().strip()
    totidade += idade
    if p == 1 and sexo == 'M':
        homemidade = idade
        homemnome = nome
    if sexo == 'M' and idade > homemidade:
        homemidade = idade
        homemnome = nome
    if sexo == 'F' and idade < 20:
        totmulher += 1
media = totidade/4
print(f'A média de idade foi {media} anos')
print(f'O homem mais velho se chama {homemnome} e tem {homemidade} anos')
print(f'Um total de {totmulher} mulheres tem menos de 20 anos')

#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário
#quer ou não continuar. No final, mostre:
#A) - Quantas pessoas são maiores de 18 anos
#B) - Quantos homens foram cadastrados
#C) - Quantas mulheres tem menos de 20 anos
maiores = homens = mulheres20 = 0
while True:
    print('-' * 30)
    print(f'{"Cadastro de pessoas":^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        maiores += 1
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            homens += 1
            break
        if sexo == 'F' and idade > 20:
            mulheres20 += 1
            break
        if sexo == 'F' and idade <= 20:
            break
        if sexo not in 'MF':
            print('Escolha somente M ou F')
    while True:
        escolha = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Escolha somente S ou N')
        if escolha == 'S':
            break
        if escolha == 'N':
            break
    if escolha == 'N':
        break
print('-='*22)
print(f'Ao todo {maiores} pessoas são maiores de 18 anos')
print(f'Ao todo foram {homens} homens cadastrados')
print(f'Ao todo {mulheres20} mulheres tem mais de 20 anos')
print('-='*22)

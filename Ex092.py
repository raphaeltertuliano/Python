#Crie um programa que leia nome, ano de nascimento
#e carteira de trabalho e cadastre-os(com idade) em um dicionário se a
#CTPS for diferente de zero, o dicionário receberá também o ano de
#contratação e o salário. Calcule e acrescente, além da idade,
#com quantos anos a pessoa vai se aposentar

import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['nascimento'] = int(input('Data de nascimento: '))
pessoa['idade'] = (datetime.datetime.today().year) - pessoa['nascimento']
pessoa['CTPS'] = int(input('Número CTPS [0 se não tiver]: '))
if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Ano da 1ª contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['contratação']+35
print('-=' * 25)
for k, v in pessoa.items():
    print(f'{k} -> {v}')


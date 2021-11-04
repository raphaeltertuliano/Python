#A Confederação Nacional de Natação precisa de um programa
#que leia o ano de nascimento de um atléta e mostre a sua catagoria,
#de acordo com a sua idade:
#- até 9 anos: MIRIM
#- até 14 anos: INFANTIL
#- até 19 anos: JUNIOR
#- até 20 anos: SÊNIOR
#- acima: MASTER

import datetime
nasc = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - nasc
print(f'Idade: {idade} anos')
if idade < 9:
    print('Categoria: \033[34mMIRIM')
elif idade == 14 or idade <= 19:
    print('Categoria: \033[34mINFANTIL')
elif idade == 19 or idade <= 20:
    print('Categoria: \033[34mSÊNIOR')
else:
    print('Categoria: \033[34mMASTER')

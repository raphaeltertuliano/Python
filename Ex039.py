#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade:
#- Se ele ainda vai se alistar no serviço militar
#- Se é hora de se alistar
#- Se já passou do tempo do alistamento
#Seu programa deverá mostrar o tempo que fala ou que passou do prazo

import datetime
anonasc = int(input('Ano de nascimento: '))
anotem = datetime.date.today().year-anonasc
print(f'Você tem {anotem} anos')
if anotem < 18:
    print('Você ainda não precisa se alistar')
    print(f'Faltam {18-anotem} anos para o alistamento')
elif anotem == 18:
    print('Você está na idade de se alistar')
else:
    print(f'Já passou {anotem-18} anos do tempo de se alistar')


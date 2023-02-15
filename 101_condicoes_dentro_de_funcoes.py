#Crie um programa que tenha uma função chamada voto()
#que vai receber como parãmetro o ano de nascimento de uma pessoa,
#indicando o valor literal indicando se a pessoa tem voto NEGADO,
#OPCIONAL ou OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    #importado dentro da função para economizar o máximo de memória possivel para quem vai usar
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f"{idade} anos. Voto NEGADO"
    elif idade >= 18 and idade < 60:
        return f"{idade} anos. Voto OBRIGATÓRIO"
    else:
        return f"{idade} anos. Voto OPCIONAL"


nasc = int(input('Em que ano você nasceu?: '))
print(voto(nasc))




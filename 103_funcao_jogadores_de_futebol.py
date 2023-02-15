#Faça um programa que tenha uma função chamada ficha(), que receba dois
#parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador,
#mesmo que algum dado não tenha sido informado corretamente
def ficha(jog=0, gols=0):
    """
    Mostra o nome e número de gols de um jogador
    :param jog: Nome do jogador
    :param gols: Gols feitos por ele no campeonato
    :return: Nome do jogador e número de gols
    """
    if jog == '':
        jog = '<desconhecido>'
    if gols == '' or gols.isnumeric() == False:
        gols = 0
    return f'O jogador {jog} fez {gols} gol(s) no campeonato'


print('-' * 30)
jogador = str(input('Nome do jogador: '))
numgols = str(input('Gols no campeonato: '))
print(ficha(jogador, numgols))

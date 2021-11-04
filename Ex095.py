#Aprimore o DESEFIO 093 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento
#de cada jogador
time = []
jogador = {}
gols = []
totgols = 0
while True:
    jogador['Nome do jogador'] = str(input('Nome do jogador: '))
    jogador['Partidas jogadas'] = int(input('Partidas jogadas: '))
    for c in range(0, jogador['Partidas jogadas']):
        gols.append(int(input(f'Gols na partida {c+1}: ')))
    jogador['Gols por partida'] = gols[:]
    for v in gols:
        totgols += v
    jogador['Gols no campeonato'] = totgols
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while True:
        escolha = str(input('Deseja continuar? [S/N]: ')).upper()
        if escolha == 'N':
            break
        elif escolha == 'S':
            break
        elif escolha not in 'SN':
            print('ERRO! Digite apenas S ou N')
    if escolha == 'N':
        break
print(f'{"COD.":<4}{"Nome":^8}{"Gols":>9}')
for posição,jogador in enumerate(time):
    print(f'{posição:<6}{jogador["Nome do jogador"]:<11}{jogador["Gols por partida"]}')
while True:
    dados = int(input('Deseja ver dados de qual jogador?[999 p/ parar]: '))
    if dados == 999:
        break
    elif dados >= len(time):
        print(f'ERRO! Não existe jogador {dados}')
    else:
        print(f'---LEVANTAMENTO DO JOGADOR {time[dados]["Nome do jogador"]}---')
        for partida, gnapart in enumerate(time[dados]["Gols por partida"]):
            print(f'    Na partida {partida+1} foram {gnapart} gols')

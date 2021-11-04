#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.No final, tudo
#isso será guardado em um dicionário, incluindo o total de gols feitos
#durante o campeonato

jogador = {}
gols = []
totgols = 0
jogador['Nome do jogador'] = str(input('Nome do jogador: '))
jogador['Partidas jogadas'] = int(input('Partidas jogadas: '))
for c in range(0, jogador['Partidas jogadas']):
    gols.append(int(input(f'Gols na partida {c+1}: ')))
jogador['Gols por partida'] = gols
for v in gols:
    totgols += v
jogador['Gols no campeonato'] = totgols
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('-=' * 20)
print(f'O jogador {jogador["Nome do jogador"]} jogou {jogador["Partidas jogadas"]} partidas')
for p, g in enumerate(gols):
    print(f'   => Na partida {p+1} foram {g} gols')
print(f'Um total de {totgols} gols')

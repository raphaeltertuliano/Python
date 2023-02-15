#Crie uma tupla preenchida com os 20 primeiros colocados da tabela
#do campeonato brasileiro de futebol, na ordem de colocação.
#Depois mostre:
#A)- Apenas os 5 primeiros colocados
#B)- Os último 4 colocados da tabela
#C)- Uma lista com os times em ordem alfabética
#D)- Em que posição da tabela está o time da Chapecoense.(tabela 2017)

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco da Gama', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo',
         'Fluminence', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí',
         'Ponte Preta', 'Atlético-GO')
print(f'Tabela {times}')
print(f'Os cinco primeiros colocados são {times[:5]}')
print(f'Os 4 últimos colocados são {times[-4:]}')
print(f'A tabela em ordem alfabética é {sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')


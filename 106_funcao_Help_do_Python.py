#Faça um minisistema que utilize o Intective Help do Python. O usuário
#vai digitar o comando e o manual vai aparecer. Quando o usuário
#digitar FIM, o programa se encerrará
#OBS: use cores
from time import sleep
c = ('\033[m',      #0 - sem cor
     '\033[97;41m',  #1 - vermelho
     '\033[97;42m',  #2 - verde
     '\033[97;43m',  #3 - amarelo
     '\033[97;44m',  #4 - azul
     '\033[97;45m',  #5 - roxo
     '\033[7;97m'    #6 - branco
     )


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA', 2)
    comando = str(input('Comando ou bibliotéca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
sleep(1)
titulo('ATÉ LOGO', 1)

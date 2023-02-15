#Crie um pequeno sistema modularizado que permita cadastrar pessoas
#pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar
#todas as pessoas cadastradas.
from Ex115.lib.interface import *
from Ex115.lib.arquivo import *
from time import sleep

arq = 'cadastrodepessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu({'Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sitema'})
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do programa... Até Logo')
        break
    else:
        print('\033[31mERRO. Digite uma opção válida!\033[m')
    sleep(2)

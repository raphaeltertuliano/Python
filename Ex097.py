#Faça um programa que tenha uma função chamada escreva(), que receba
#um texto qualquer como parãmetro e mostre uma mensagem adaptável.
#Ex: escreva('Olá, Mundo!')
#saída:
#~~~~~~~~~~~~~
# Olá, Mundo!
#~~~~~~~~~~~~~

def escreva(txt):
    tamanho = len(txt)+2
    print('~' * tamanho)
    print(f' {txt}')
    print('~' * tamanho)

frase = str(input('Escreva algo: '))
escreva(frase)
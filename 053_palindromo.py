#Crie um programa que leia uma frase qualquer e
#diga se ela é um palíndromo,
#desconsiderando os espaços.
#PS: palíndromo é uma frase que o inverso dela é igual ao jeito
#normal de leitura e escrita
#EX: o inverso de ARARA é ARARA
frase = str(input('Digite uma palavra ou frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Temos um palindromo!')
else:
    print('Não é um palindromo!')

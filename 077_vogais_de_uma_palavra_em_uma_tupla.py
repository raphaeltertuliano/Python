#Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
#Depois disso, você deve mostrar, quais são as suas vogais

palavras = ('pedra', 'papel', 'tesoura', 'computador', 'camiseta',
            'calça', 'colher', 'garfo',)
for pos, c in enumerate(palavras):
    print(f'Na palavra {c.upper()} temos as vogais ', end='')
    for d in c:
        if d in 'AaEeIiOoUu':
            print(d, end=' ')
    print()

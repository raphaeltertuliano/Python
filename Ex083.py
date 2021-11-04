#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá se a expressão passada está com os parênteses
#abertos e fechados na ordem correta.

expressão = str(input('Digite uma expressão: '))
lista = []
for simb in expressão:
    if simb == '(':
        lista.append('(')
    if simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão está errada')

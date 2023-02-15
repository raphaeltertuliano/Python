#Crie um programa que tenha uma função fatorial() que receba
#dois parâmetros: o primeiro que indique um número a calcular
#e outro chamado show, que terá o valor  lógico (OPCIONAL) indicando se
#será mostrado ou não na tela o processo de cálculo fatorial
def fatorial(num, show=False):
    fat = 1
    for elemento in range(num, 0, -1):
        if show:
            if elemento > 1:
                print(f'{elemento} x ', end='')
            else:
                print('= ', end='')
        fat *= elemento
    return fat


numero = int(input('Digite um numero para saber seu fatorial: '))
print(fatorial(numero, show=True))

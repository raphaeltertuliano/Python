#Crie um programa que simule um caixa eletrônico. No início, pergunte
#ao usuário qual o valor a ser dacado(número inteiro) e o programa vai
#informar quantas césulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
print('-='*15)
print(f'{"CAIXA ELETRÔNICO":^30}')
print('-='*15)
v = int(input('Valor a ser sacado: R$'))
total = v
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
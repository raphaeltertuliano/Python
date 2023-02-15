#Faça um programa que tenha a função leiaint() que vai funcionar de
#forma semelhante à função input() do Python, só que fazendo a validação
#para aceitar apenas um valor numérico.
#EX: n = leiaint('digite um n')
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite apenas números inteiros\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')


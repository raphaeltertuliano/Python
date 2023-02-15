def leiadinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[31mERRO! "{n}" não é um valor válido\033[m')
        else:
            valor = float(n)
            ok = True
        if ok:
            break
    return valor


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
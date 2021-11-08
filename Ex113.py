def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar o valor')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido\033[m')
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar o valor')
            return 0
        else:
            return n


n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')

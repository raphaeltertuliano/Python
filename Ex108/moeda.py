def aumentar(n, taxa):
    resposta = ((n * taxa) / 100) + n
    return resposta


def diminuir(n, taxa):
    return n - ((n * taxa) / 100)


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'. replace('.', ',')


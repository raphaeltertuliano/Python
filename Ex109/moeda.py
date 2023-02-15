def aumentar(n=0, taxa=0, formato=False):
    """
    Aumenta o valor pela taxa que foi descrita
    :param n: valor monetário
    :param taxa: valor do aumento
    :param formato: se vai ter a formatação(R$, vírgula(,))
    :return: o valor digitado formatado ou não
    """
    resposta = ((n * taxa) / 100) + n
    return resposta if formato is False else moeda(resposta)


def diminuir(n=0, taxa=0, formato=False):
    """
    Diminui o valor pela taxa que foi descrita
    :param n: valor monetário
    :param taxa: valor da diminuição
    :param formato: se vai ter a formatação(R$, vírgula(,))
    :return: o valor digitado formatado ou não
    """
    resposta = n - ((n * taxa) / 100)
    return resposta if formato is False else moeda(resposta)


def dobro(n=0, formato=False):
    """
    Dobra o valor que foi descrito
    :param n: valor monetário
    :param formato: se vai ter a formatação(R$, vírgula(,))
    :return: o valor digitado formatado ou não
    """
    resposta = n * 2
    return resposta if formato is False else moeda(resposta)


def metade(n=0, formato=False):
    """
    Metade dovalor que foi descrito
    :param n: valor monetário
    :param formato: se vai ter a formatação(R$, vírgula(,))
    :return: o valor digitado formatado ou não
    """
    resposta = n / 2
    return resposta if formato is False else moeda(resposta)


def moeda(n=0, moeda='R$'):
    """
    Formata o valor com R$ e vírgula(,)
    :param n: valor monetário
    :param moeda: padrão R$
    :return: valor formatado se solicitado pelo usuário
    """
    return f'{moeda}{n:.2f}'. replace('.', ',')


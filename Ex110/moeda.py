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


def resumo(n=0, taxa1=0, taxa2=0):
    """
    Mostra o resumo do valor digitado
    :param n: valor digitado
    :param taxa1:  % de aumento do valor digitado
    :param taxa2:  % de diminuição do valor digitado
    :return: sem retorno
    """
    print('-' * 30)
    print(f'{"Resumo do valor":^30}')
    print('-' * 30)
    print(f'Preço analisado:    {moeda(n)}')
    print(f'Dobro do preço:     {dobro(n, True):<5}')
    print(f'Metade do preço:    {metade(n, True):<5}')
    print(f'80% de aumento:     {aumentar(n, 80, True):<5}')
    print(f'35% de redução:     {diminuir(n, 35, True):<5}')
    print('-' * 30)

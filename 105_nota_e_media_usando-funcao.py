#Faça um programa que tenha uma função chamada notas() que pode receber
#várias notas de alunos e vai retornar um dicionário com as
#seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação(opcional)
#adicione também as docstrigs da função.
def notas(*n, sit=False):
    """
    Mostra a média de uma sala e diz a situação dela
    colocando tudo em um dicionário
    :param n: Número de notas passadas
    :param sit: Situação da turma
    :return: Dicionário com todos os dados da turma
    """
    turma = {}
    turma["Total"] = len(n)
    turma['Maior nota'] = max(n)
    turma['Menor nota'] = min(n)
    turma['Média'] = (sum(n))/len(n)
    if sit:
        if turma['Média'] >= 7:
            turma['Situação'] = 'BOA'
        elif turma['Média'] >= 5:
            turma['Situação'] = 'RAZOAVEL'
        else:
            turma['Situação'] = 'RUIM'
    sala = turma
    return sala


resp = notas(7, 8, 9, sit=True)
print(resp)
help(notas)

#Faça um programa que leia nome e média de um aluno, guardando também a situação
#em um dicinário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Qual é a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = "APROVADO"
elif aluno['media'] >= 5 and aluno['media'] <= 6.9:
    aluno['situacao'] = "de RECUPERAÇÂO"
else:
    aluno['situacao'] = "REPROVADO"
print("-=" * 20)
print(f'O aluno {aluno["nome"]} tem média {aluno["media"]}')
print(f'{aluno["nome"]} está {aluno["situacao"]}')

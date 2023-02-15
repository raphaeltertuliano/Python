#Crie um programa que leia o nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo
#a média de cada um e permita que o usuário possa mostrar as notas
#de cada aluno individualmente

turma = []
aluno = []
notas = []
media = []
while True:
    nome = str(input('Nome do aluno: '))
    aluno.append(nome)
    n1 = float(input('Nota 1: '))
    notas.append(n1)
    n2 = float(input('Nota 2: '))
    notas.append(n2)
    m = (n1 + n2)/2
    media.append(m)
    aluno.append(notas[:])
    aluno.append(m)
    turma.append(aluno[:])
    notas.clear()
    aluno.clear()
    esc = str(input('Deseja continuar? [S/N]: '))
    if esc in 'Nn':
        break
print(turma)
print(f'{"Nº":<5}{"NOME":<6}{"MÉDIA":>9}')
for a, b in enumerate(turma):
    print(f'{a:<5}', end='')
    print(f'{b[0]:<6}', end='')
    print(f'{b[2]:>7}')
while True:
    ind = int(input('Deseja ver as notas de qual aluno? [999 p/ encerrar]: '))
    if ind == 999:
        break
    print(f"As notas de {turma[ind][0]} são: {turma[ind][1]}")
print()
print("-----FIM DO PROGRAMA. OBRIGADO-----")


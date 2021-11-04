#Crie um programa que leia duas notas de um aluno e calcule a sua média,
#mostrando uma mensagem no final, de acordo com a média atigida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print(f'A média foi {m:.1f}')
if m < 5.0:
    print('REPROVADO')
elif m == 5.0 or m < 6.9:
    print('RECUPERAÇÃO')
elif m >= 7.0:
    print('APROVADO')

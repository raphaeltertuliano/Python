#Escreva um programa para aprovar o empréstimo bacário
# para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador
#e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
#do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa?: R$'))
salario = float(input('Qual o valor do salário?: '))
pagamento = int(input('Em quantos anos pretende pagar?: '))
mensalidade = casa/(pagamento*12)
if mensalidade <= salario-((salario*70)/100):
    print(f'A mensalidade sai R$\033[34m{mensalidade:.2f}\033[m')
else:
    print('\033[31mFinanciamento não aprovado\033[m')


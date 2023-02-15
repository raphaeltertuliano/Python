#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule o seu IMC e mostre o seu status, de acordo com a tabela abaixo:
#- Abaixo de 18.5: Abaixo do peso
#- Entre 18.5 e 25: Peso ideal
#- 25 a 30: Sobrepeso
#- 30 a 40: Obesidade
#- Acima de 40: Obesidade mórbida

peso = float(input('Peso [Kg]: '))
altura = float(input('Altura [Cm]: '))
imc = peso/((altura/100)**2)
print(f'Seu IMC é: {imc:.1f} >>> ', end='')
if imc < 18.5:
    print('\033[31mAbaixo do Peso')
elif imc == 18.5 or imc < 25:
    print('\033[34mPeso Ideal')
elif imc == 25 or imc < 30:
    print('\033[33mSobrepeso')
elif imc == 30 or imc < 40:
    print('\033[33mObesidade')
else:
    print('\033[31mObesidade Mórbida')

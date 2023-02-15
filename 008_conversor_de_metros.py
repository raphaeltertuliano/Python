#Escreva um progrma que leia um valor em metros
#e o exiba convertido em centímetros e milímetros

comprimento = float(input('Quantos metros?: '))
print(f'O valor em metro é: {comprimento:.3f}m')
print(f'Em centímetros é: {comprimento*100:.3f}cm')
print(f'Em milímetros é {comprimento*1000:.3f}mm')

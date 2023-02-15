#Faça um programa que leia uma frase pelo teclado e mostre:
#1) Quantas vezes Aparece a letra 'A'
#2) Em que posição ela aparece pela primeira vez
#3) Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A letra A parece a primeira vez na posição {frase.find("A")+1}')
print(f'A letra A aparece pela última vez na posição {frase.rfind("A")+1}')

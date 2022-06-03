'''
2) Escrever um programa para ler um número inteiro e informar se ele é divisível por 5.
Dica: um número é divisível por outro se o resto for igual a 0. Logo, você precisa obter o resto da divisão e comparar com 0.
Se o resto da divisão for igual a 0, então é divisível por 5, senão, não é.
'''

n1 = int(input("digite um número: "))
logica = n1 % 5

if(logica == 0):
    print("esse numero é divisivel por 5")
else:
    print("esse número NÃO é divisivel por 5")

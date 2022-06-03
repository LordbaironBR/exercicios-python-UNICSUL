'''
7) Escreva um programa em Python para imprimir todas as letras do
alfabeto (valor de ‘A’ ASCII é 65 e o valor de ‘Z’ ASCII é 90).
'''

for x in range(65,91):
    print(str(x) + ' significa "   {}   " na tabela ASCII'.format(chr(x)))
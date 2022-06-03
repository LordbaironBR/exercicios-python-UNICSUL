'''
8) Escreva um programa em Python para imprimir todas as letras do alfabeto (valor de ‘a’ ASCII é 97 e o valor de ‘z’ ASCII é 122).
'''

for x in range(97,123):
    print(str(x) + ' significa "   {}   " na tabela ASCII'.format(chr(x)))
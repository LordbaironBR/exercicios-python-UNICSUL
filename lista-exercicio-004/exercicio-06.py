'''
6)Escreva um programa em Python para imprimir todos os caracteres ASCII com seus valores (imprimir a tabela ASCII).
'''

for x in range(33,126):
    print(str(x) + ' significa "   {}   " na tabela ASCII'.format(chr(x)))
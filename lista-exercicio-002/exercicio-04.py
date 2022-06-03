'''
4) Escrever um programa que leia um valor X inteiro e positivo, e também leia outros 3 valores a, b e c, que também são inteiros.
    Se o valor de X é PAR então calcular e imprimir na tela a média aritmética de a, b e c. Caso contrário, se X>10
    então calcular e imprimir na tela a média ponderada de a, b e c. Os pesos dos valores são respectivamente 2, 3 e 4
'''

#ter a biblioteca numpy instalada

import numpy as np

x = int(input("1º Valor (usado como parâmetro): "))
a = int(input("2º Valor: "))
b = int(input("3º Valor: "))
c = int(input("4º Valor: "))
modulo = x % 2
mediaaritimetica = [a,b,c]
valores = np.array([a,b,c])
pesos = np.array([2,3,4])
mediaponderada = np.inner(valores,pesos)


if(modulo == 0):
    print("1º valor é PAR logo irei imprimir a média aritimética do 2º,3º e 4º valor"
          "\n média aritimética de {} e {} e {} é igual á: {}".format(a,b,c,sum(mediaaritimetica)))
if(x > 10):
    print("1º valor é maior que 10 logo irei imprimir a média ponderada"
          "\n média ponderada de {} {} {} é igual á: {}".format(a, b, c,mediaponderada))
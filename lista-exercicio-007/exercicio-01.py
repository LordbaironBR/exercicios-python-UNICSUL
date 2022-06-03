"""
Faça um programa que leia 10 números inteiros e os armazene em duas listas. Armazene números pares em uma lista chamada PAR e números ímpares em uma lista chamada IMPAR. Mostrar os vetores na tela.
"""

import random

x = 0
numeros = []
par = []
impar = []

while x <10:
    x+=1
    n= int(random.randint(0,99))
    numeros.append(n)
    if(n%2 == 0):
        par.append(n)

    else:
        impar.append(n)
print("da lista de numeros: {}"
      "\n os pares são: {}"
      "\n os impares são: {}".format(numeros,par,impar))



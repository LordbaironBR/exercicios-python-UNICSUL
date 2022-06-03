"""
Criar um programa em python que seja possível reverter qualquer lista. Não é para apenas imprimir o valor invertido. É para realmente inverter os valores da lista. Por exemplo:


Entrada: lista = [78,98,54,65,41]
Saída: lista = [41,65,54,98,78]

(é a mesma lista, porém agora na posição zero está o valor que, anteriormente, estava na posição quatro.
"""
import random


x=0
y=-1
z=int(input("Digite a quantidade de numeros da lista: "))
lista=[]
lista_invertida=[]


while x<z:
    x+=1
    n=int(random.randint(0,99))
    lista.append(n)

x=0
while x<z:
    x+=1
    lista_invertida.append(lista[y])


print("Lista original: {}"
      "\n"
      "\n Lista invertida: {}".format(lista,lista_invertida))

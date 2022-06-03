"""
Desenvolva um programa que, dado uma lista com 10 valores, o sistema encontre qual é o maior valor e qual a posição ele ocupa na lista.
Entrada: lista = [10,16,45,12,17,92,18,16]
Saída:
Maior 92
Posição 5
"""

import random
import numpy as np

l= [random.randint(0,99), random.randint(0,99), random.randint(0,99), random.randint(0,99), random.randint(0,99), random.randint(0,99), random.randint(0,99), random.randint(0,99), random.randint(0,99), random.randint(0,99)]







print("Lista original: {}"
      "\n Maior valor: {}"
      "\n No indice: {}".format(l,max(l),l.index(max(l))))



# Desenvolva um programa que receba o valor do raio de uma circuferencia e calcule a área
#   FORMULA: (pi . x r²)
import math

r = float(input("Qual raio da circuferencia" ))
a = math.pi*(r**2)

print("A área da cirferencia é {:.2f}".format(a))
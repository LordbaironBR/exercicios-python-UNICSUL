# 5) Escreva um programa que leia três números e mostre-os em ordem crescente
import math

a = int(input("1º Valor: "))
b = int(input("2º Valor: "))
c = int(input("3º Valor: "))
numeros = [a,b,c]

print(sorted(numeros))
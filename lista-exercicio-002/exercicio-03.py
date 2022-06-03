'''
3) Escrever um programa que solicite ao usuário um número e verifique se este número é par ou ímpar.
Dica: um número é par se o resto da divisão por dois for igual a zero. O número é ímpar se o resto da divisão por dois for diferente de zero.
'''

n1 = int(input("Digite um número: "))

if(n1 % 2 == 0):
    print("Esse número é par")
else:
    print("Esse número é impar")
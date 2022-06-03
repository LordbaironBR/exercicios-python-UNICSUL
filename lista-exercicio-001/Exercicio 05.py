# desenvolva um programa em python que solicite dois números ao usuario e, em seguida realize todas as operações aritimeticas, mostrando o resultado na tela

import math
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))

soma = n1 + n2
subtracao = n1 - n2
divisao = n1 / n2
multiplicacao = n1 * n2
potencia = n1 ** n2
raiz1 = math.sqrt(n1)
raiz2 = math.sqrt(n2)

# noinspection PyStringFormat
print(" Segue as seguintes operações"
      " \n {:.0f} + {:.0f} = {:.0f}"
      " \n {:.0f} - {:.0f} = {:.0f}"
      " \n {:.0f} / {:.0f} = {:.2f}"
      " \n {:.0f} * {:.0f} = {:.0f}"
      " \n {:.0f} ^ {:.0f} = {:.0f}"
      " \n Raiz qudrada de {:.0f} = {:.2f}"
      " \n Raiz quadrada de {:.0f} = {:.2f}"
        .format(n1,n2,soma,
            n1,n2,subtracao,
            n1,n2,divisao,
            n1,n2,multiplicacao,
            n1,n2,potencia,
            n1,raiz1,
            n2,raiz2)
      )

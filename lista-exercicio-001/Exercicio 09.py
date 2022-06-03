#   Desenvolva um programa para calcular o IMC de uma pessoa
#   FORMULA:    (peso/altura²)

peso = int(input("Digire seu peso em kg "))
altura = float(input("Digite sua altura em metros "))

imc = float(peso/(altura**2))

print("Seu IMC é {:.2f}".format(imc))
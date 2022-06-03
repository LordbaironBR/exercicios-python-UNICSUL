#   escreva um programa que mostre na tela o nome do usuario e a quantidade de dopos de água que ele bebeu hoje

nome = str(input("Qual seu nome? "))
ncoposdagua = int(input("Quantos copos de água você bebeu hoje ? "))

print("Olá {} hoje você bebeu {} copos de água".format(nome,ncoposdagua))
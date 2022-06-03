'''4) Escreva um programa em Python para imprimir (mostrar na tela) todos os números naturais do intervalo de n a m, sendo que n é o valor
inicial e m o valor final do intervalo. Estes limites devem ser informados pelo usuário. Sendo m um valor maior que n'''

n = int(input('digite o inicio do intervalo: '))
m = int(input('digite o fim do intervalo: '))

for x in range(n,m+1):
    print(x)
'''
1) Escreva um programa em Python para permitir que o usuário digite o número referente ao mês (1 Janeiro, 2 Fevereiro, 3 Março, ...). O sistema
deve informar o número de dias daquele mês.
'''


x = int(input('Digite número de mês: '))
mes = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
n = [1,2,3,4,5,6,7,8,9,10,11,12]

if(x not in n):
    print('digite corretamente o numero do mes')
else:
    if(x==1):
        print('Janeiro possui 31 dias')
    elif(x==2):
        print('Fevereiro possui 28 dias e 29 dias')
    elif(x==3):
        print('Março possui 31')
    elif(x==4):
        print('Abril possui 30 dias')
    elif(x==5):
        print('Maio possui 31 dias')
    elif(x==6):
        print('Junho possui 30 dias')
    elif(x==7):
        print('Julho possui 31 dias')
    elif(x==8):
        print('Agosto possui 31 dias')
    elif(x==9):
        print('Setembro possui 30 dias')
    elif(x==10):
        print('Outubro possui 31 dias')
    elif(x==11):
        print('Novembro possui 30 dias')
    elif(x==12):
        print('Dezembro possui 31 dias')
'''
1) Escreva um programa onde o usuário informa o salário recebido no mês e o valor gasto no mesmo mês. O programa deverá exibir na tela se o gasto está dentro do orçamento
(caso o valor gasto não ultrapasse o valor do salário) e se o valor gasto está fora do orçamento (se o valor ultrapassar o valor do salário).
'''

salario = float(input("informe seu salário/mês: "))
gasto = float(input("informe seu gasto/mês: "))

if(salario >= gasto):
    print("seus gastos estão dentro do orçamento")
else:
    print("melhor economizar,pois seus gastos estão ultrapassando seu orçamento")
'''
2) Podemos conferir o estado em quem um determinado CPF foi emitido, para isso, precisamos analisar o último algarismo, anterior aos
dois dígitos de controle. Por exemplo, no CPF 000.000.008-xx o número 8 indica que este documento foi emitido no estado de São Paulo.
Outro CPF 000.000.006-xx foi emitido no estado de Minas Gerais, e é possível afirmar isso analisando o número 6 antes dos dois dígitos e controle.
Veja a seguir a tabela e códigos de estados brasileiros e seus respectivos

códigos:
1. Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins;
2. Pará, Amazonas, Acre, Amapá, Rondônia e Roraima;
3. Ceará, Maranhão e Piauí;
4. Pernambuco, Rio Grande do Norte, Paraíba e Alagoas;
5. Bahia; e Sergipe;
6. Minas Gerais;
7. Rio de Janeiro e Espírito Santo;
8. São Paulo;
9. Paraná e Santa Catarina;
0. Rio Grande do Sul.

Construa um programa que, ao verificar um número de CPF, seja
capaz de informar em qual estado o documento foi emitido.
'''

cpf = str(input('Digite seu CPF (11 digitos, apenmas numeros) '))

if(cpf[8] == "1"):
    print("Seu CPF foi emitido no estado de ")

if(cpf[8] == "2"):
    print("Seu CPF foi emitido no estado de ")

if(cpf[8] == "3"):
    print("Seu CPF foi emitido no estado de ")

if(cpf[8] == "4"):
    print("Seu CPF foi emitido no estado de ")

if(cpf[8] == "5"):
    print("Seu CPF foi emitido no estado de ")

if(cpf[8] == "6"):
    print("Seu CPF foi emitido no estado de ")

if(cpf[8] == "7"):
    print("Seu CPF foi emitido no estado de ")

if(cpf[8] == "8"):
    print("Seu CPF foi emitido no estado de ")

if(cpf[8] == "9"):
    print("Seu CPF foi emitido no estado de ")

if(cpf[8] == "0"):
    print("Seu CPF foi emitido no estado de ")
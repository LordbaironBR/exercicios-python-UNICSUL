


a=int(input("Digite o valor do lado A: "))
b=int(input("Digite o valor do lado A: "))
c=int(input("Digite o valor do lado A: "))

if(a==b==c):
    print("Triângilo equilatero")
elif(a==b or a==c or b==c):
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")

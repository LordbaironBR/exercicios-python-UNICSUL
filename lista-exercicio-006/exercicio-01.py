palavra = str("dante")
tentativa = str("12345")


while(palavra != tentativa):
    a = str(input("Digite uma letra: "))
    if(a == "d"):
       tentativa = tentativa.replace("1","d")
    if (a == "a"):
        tentativa = tentativa.replace("2", "a")
    if (a == "n"):
        tentativa = tentativa.replace("3", "n")
    if (a == "t"):
        tentativa = tentativa.replace("4", "t")
    if (a == "e"):
        tentativa = tentativa.replace("5", "e")

    print(tentativa)


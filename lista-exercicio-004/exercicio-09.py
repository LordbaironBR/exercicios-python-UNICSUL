from numpy.core.defchararray import upper

palavra = str(input('digite um caractere: '))


if(palavra.isalpha() == True):
    print('isto é uma palavra')

    if(palavra.isupper() == True):
        print('essa palavra é maiuscula.')
    elif(palavra.islower() == True):
        print('essa palavra é minuscula.')
    else:
        print('essa palavra possui maiusculo e minusculo')
else:
    print('isto não é alfabético')


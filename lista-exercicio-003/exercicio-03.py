

numero = int(input('digite um numero inteiro até 4 digitos: '))
nstring = str(numero)
nx = nstring[0]


if(nstring.count(nx)) == len(nstring):
    print('{} é um número palíndromo, ou seja o reverso de si mesmo permanece igual'.format(numero))

if(len(nstring) == 1):
    n0 = int(nstring[0])
    if(n0**1 == numero):
        print('{} é um numero de armstrong'.format(numero))
    else:
        print('{} não é um número de armstrong'.format(numero))

if(len(nstring) == 2):
    n0 = int(nstring[0])
    n1 = int(nstring[1])
    if((n0**1)+(n1**2) == numero):
        print('{} é um numero de armstrong'.format(numero))
    else:
        print('{} não é um número de armstrong'.format(numero))

if(len(nstring) == 3):
    n0 = int(nstring[0])
    n1 = int(nstring[1])
    n2 = int(nstring[2])
    if((n0**1)+(n1**2)+(n2**3) == numero):
        print('{} é um numero de armstrong'.format(numero))
    else:
        print('{} não é um número de armstrong'.format(numero))

if(len(nstring) == 4):
    n0 = int(nstring[0])
    n1 = int(nstring[1])
    n2 = int(nstring[2])
    n3 = int(nstring[3])
    if((n0**1)+(n1**2)+(n2**3)+(n3**4) == numero):
        print('{} é um numero de armstrong'.format(numero))
    else:
        print('{} não é um número de armstrong'.format(numero))
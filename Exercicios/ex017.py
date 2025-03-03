import math

catOPOS = float(input('Comprimento do cateto oposto: '))
catADJ = float(input('Comprimento do cateto adjacente: '))

hipot =  ((catADJ ** 2) + (catOPOS ** 2)) ** (1/2)
#hipot = math.hypot(catADJ, catOPOS) #Outra forma de fazer com biblioteca

print('A hipotenusa vai medir {:.2f}'.format(hipot))
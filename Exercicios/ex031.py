distancia = int(input('Qual a distancia da sua viajem? '))
'''
if distancia <= 200:
    tarifa = 0.50

else:
    tarifa = 0.45
'''

tarifa = 0.50 if distancia <= 200 else 0.45

print('O valor a pagar e de R${}'.format(distancia * tarifa))
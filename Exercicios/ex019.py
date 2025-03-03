import random
um = input('Digite o primeiro nome')
dois = input('Digite o segundo nome')
tres = input('Digite o terceiro nome')
quatro = input('Digite o quarto nome')

valor = random.choice([um, dois, tres, quatro])

print('O nome escolhido foi: {}'.format(valor))
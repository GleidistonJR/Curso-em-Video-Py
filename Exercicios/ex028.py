import random

print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' *20)

n = random.randint(0,5)

user = int(input('Em que numero pensei? '))

print('PROCESSANDO')

if n == user:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}! '.format(n,user))
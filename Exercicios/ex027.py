nome = str(input('Digite seu nome completo')).strip().split()

print('Muito prazer em conhecer!')
print('Seu primeiro nome é {}'.format(nome[0].capitalize()))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1].capitalize()))
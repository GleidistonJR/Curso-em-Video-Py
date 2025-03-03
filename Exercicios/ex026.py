frase = str(input('Digite uma frase')).lower().strip()

print('A letra A apareceu {} vezes na frase'.format(frase.count('a')))
print('A Primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A Primeira letra A apareceu na posição {}'.format(frase.rfind('a')+1))

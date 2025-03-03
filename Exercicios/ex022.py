nome = str(input('Digite seu \033[32mnome completo:\033[m '))

nome = nome.strip()
print('Analisando seu nome...')

print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

final = nome.find(' ')

print('Seu primeiro nome é {} e ele tem {} letras '.format(nome[0:final],final))

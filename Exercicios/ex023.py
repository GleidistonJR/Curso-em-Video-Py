numero = int(input('Informe um \033[1;31mnumero:\033[m '))
print('Analizando o numero \033[1;32m{}\033[m'.format(numero))
print('\033[1;32mUnidade: \033[1;33m{}\033[m'.format((numero // 1) % 10))
print('\033[1;32mDezena: \033[1;33m{}\033[m'.format((numero // 10) % 10))
print('\033[1;32mCentena: \033[1;33m{}\033[m'.format((numero // 100) % 10))
print('\033[1;32mMilhar: \033[1;33m{}\033[m'.format((numero // 1000) % 10))
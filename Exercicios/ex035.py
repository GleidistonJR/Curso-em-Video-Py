print('\033[32m-=-\033[m'*15)
print(' '* 15, '\033[1;33mAnalisando\033[m')
print('\033[32m-=-\033[m'*15)

r1 = float(input('\033[1;31mPrimeiro segmento\033[m '))
r2 = float(input('\033[1;31mSegundo segmento\033[m '))
r3 = float(input('\033[1;31mTerceiro segmento\033[m '))

if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1 + r2:
    print('Os segmentos acima pode formar um triangulo')
else:
    print('Os segmentos acima NÂO pode formar um triangulo')
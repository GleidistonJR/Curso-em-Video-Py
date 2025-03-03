carteira = float(input('Quanto você tem na carteira? R$'))

dolar = 5.89

print('Com R${:.2f} cocê pode comprar US{:.2f}'.format(carteira, (carteira/dolar)))
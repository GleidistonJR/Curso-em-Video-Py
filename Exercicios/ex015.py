dias = int(input("Dias alugados: "))
km = int(input("km rodados: "))

valor = (dias * 60) + (km * 0.15)

print('Valor que deve ser pago é: R${:.2f}'.format(valor))
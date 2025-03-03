vel = int(input('Qual é a velocidade atua do carro? '))

if vel > 80:
    print('MULTADO! Você exedeu o limite permitido que é de 80Km/h')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('PARABENS! Você esta dentro do limite de velocidade!')

print('Dirija com segurança!')
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

dimensao = altura * largura

litros = dimensao / 2

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.3f}m².'.format(largura,altura,dimensao))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(litros))
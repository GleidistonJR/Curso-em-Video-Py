from datetime import date

ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} e BISSEXTO'.format(ano))
else:
    print('O ano {} NÃo é BISSEXTO'.format(ano))

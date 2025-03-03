dist = float(input('Uma distancia em metros'))

km =  dist/1000
hm =  dist/100
dam = dist/10
dm =  dist*10
cm =  dist*100
mm = dist*1000

print('A medida de 3.0m corresponde a ')
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))

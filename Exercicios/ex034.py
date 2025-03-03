salario = int(input('\033[32mQual o salario\033[m'))

if salario >= 1250:
    salario = salario + (salario *10 /100)
else :
    salario = salario + (salario * 15/100)

print('Novo salario e igual ha R${:.2f}'.format(salario))
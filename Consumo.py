print('Digite "R" para Residência')
print('Digite "I" para Industria')
print('Digite "C" para Comércio')
ins = input('Qual o tipo da instalação? ')
if ins == 'R' or ins == 'r' or ins == 'c' or ins == 'C' or ins == 'i' or ins == 'I':
    kwh = float(input('Quanto KWh foi consumido? '))

    if ins == 'R' or ins == 'r':
        if kwh <= 500:
            z = (0.40 * kwh)
            print('Valor total pago é R$ {:.2f}' .format(z))
        elif kwh > 500:
            x = (0.55 * kwh)
            print('Valor total pago é R$ {:.2f}'.format(x))
        else:
            print('Valor Inválido')
    if ins == 'C' or ins == 'c':
        if kwh <= 1000:
            z1 = (0.55 * kwh)
            print('Valor total pago é R$ {:.2f}'.format(z1))
        elif kwh > 1000:
            x2 = (0.60 * kwh)
            print('Valor total pago é R$ {:.2f}'.format(x2))
        else:
            print('Valor Inválido')
    if ins == 'I' or ins == 'i':
        if kwh <= 5000:
            z3 = (0.55 * kwh)
            print('Valor total pago é R$ {:.2f}'.format(z3))
        elif kwh >5000:
            x3 = (0.60 * kwh)
            print('Valor total pago é R$ {:.2f}'.format(x3))
else:
    print('Valor Inválido')

x = 0
print('Bem Vindo a Lanchonete de Sérgio Luiz Neves Rodrigues')
print('*' * 22 + 'Cardápio' + '*' * 23)
print('|Código|' + ' ' * 10 + '- Descrição - ' + ' ' * 10 + '|Valor(R$)|')
print('|  100 |' + ' ' * 8 + '- Cachorro-Quente - ' + ' ' * 6 + '|   9,00  |')
print('|  101 |' + ' ' * 6 + '- Cachorro-Quente Duplo - ' + ' ' * 2 + '|  11,00  |')
print('|  102 |' + ' ' * 12 + '- X-Egg - ' + ' ' * 12 + '|  12,00  |')
print('|  103 |' + ' ' * 10 + '- X-Salada - ' + ' ' * 11 + '|  13,00  |')
print('|  104 |' + ' ' * 11 + '- X-Bacon - ' + ' ' * 11 + '|  14,00  |')
print('|  105 |' + ' ' * 11 + '- X-Tudo - ' + ' ' * 12 + '|  17,00  |')
print('|  200 |' + ' ' * 6 + '- Refrigerante Lata - ' + ' ' * 6 + '|   5,00  |')
print('|  201 |' + ' ' * 9 + '- Chá Gelado - ' + ' ' * 10 + '|   4,00  |')

while True:
    y = input('insira o código do produto ')

    if y == '100':
        print('Cachorro Quente de 9 Reais adicionado na lista')
        valor = 9.00
        x += valor
    elif y == '101':
        print('Cachorro Quente Duplo de 11 Reais adicionado na lista')
        valor = 11.00
        x += valor
    elif y == '102':
        print('X-Egg de 12 Reais adicionado na lista')
        valor = 12.00
        x += valor
    elif y == '103':
        print('X-Salada de 13 Reais adicionado na lista')
        valor = 13.00
        x += valor
    elif y == '104':
        print('X-Bacon de 14 Reais adicionado na lista')
        valor = 14.00
        x += valor
    elif y == '105':
        print('X-Tudo de 17 Reais adicionado na lista')
        valor = 17.00
        x += valor
    elif y == '200':
        print('Refrigerante Lata de 5 Reais adicionado na lista')
        valor = 5.00
        x += valor
    elif y == '201':
        print('Chá Gelado de 4 Reais adicionado na lista')
        valor = 4.00
        x += valor
    else:
        print('Código inválida')
        continue
    print('deseja pedir mais alguma coisa?')
    print('1 - sim')
    print('0 - não')
    c = input('')
    if c == '1' or c == 'sim':
        continue
    else:
        print('Total a ser pago é de {:.2f} Reais'.format(x))
        print('Obrigado por comprar na lanchonete do Sérgio, Volte Sempre')
        break

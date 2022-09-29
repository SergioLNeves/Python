print('Bem Vindo a Lanchonete de Sérgio Luiz Neves Rodrigues')
x = 0
while True:
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

    y = int(input('insira o código do produto '))

    if y == '100':
      x += 9.00
      print('você escolheu frango por 9 reais')
    elif y == '101':
      x += 11.00
    elif y == '102':
      x += 12.00
    elif y == '103':
      x += 13.00
    elif y == '104':
      x += 14.00
    elif y == '105':
      x += 17.00
    elif y == '200':
      x += 5.00
    elif y == '201':
      x += 4.00
    else:
        print('Opção inválida')
        continue
    print('deseja pedir mais alguma coisa?')
    print('1 - sim')
    print('0 - não')
    c = input('')
    if c == '1' or c == 'sim':
        continue
    else:
        break
        print('Total a ser pago foi de {}' .format(x))

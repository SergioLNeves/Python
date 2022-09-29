def dimensoesObjeto():
    while True:
        try:
            altura = int(input('Qual a Altura do objeto (em cm): '))
            largura = int(input('Qual a Largura do objeto (em cm): '))
            comprimento = int(input('Qual o Comprimento do objeto (em cm): '))
            volume = altura * largura * comprimento
            if volume != 0:
                if volume < 1000:
                    print('O Volume do objeto é: {}cm³'.format(volume))
                    return 10.00

                elif 1000 <= volume < 10000:
                    print('O Volume do objeto é: {}cm³'.format(volume))
                    return 20.00

                elif 10000 <= volume < 30000:
                    print('O Volume do objeto é: {}cm³'.format(volume))
                    return 30.00

                elif 30000 <= volume < 100000:
                    print('O Volume do objeto é: {}cm³'.format(volume))
                    return 50.00

                elif volume >= 100000:
                    print('O volume do objeto é {}'.format(volume))
                    print('Não aceitamos objetos com dimensões tão grandes')
                    print('Entre com as dimensões desejadas novamente')
                    continue
            else:
                print('Dimensão inexistente, Peso negativo ou igual a 0 informado')
                print('Por favor entre com as dimensões desejadas novamente')
                continue
        except ValueError:
            print('Você digitou alguma dimensão com valores não numéricos')
            print('Por favor entre com as dimensões desejadas novamente')


def pesoObjeto():
    while True:
        try:
            pesos = float(input('Digite o peso do objeto (em kg): '))
            if pesos != 0:
                if pesos <= 0.1:
                    return 1

                elif 0.1 < pesos <= 1:
                    return 1.5

                elif 1 < pesos <= 10:
                    return 2

                elif 10 < pesos <= 30:
                    return 3

                elif pesos > 30:
                    print('O peso do objeto é {}'.format(pesos))
                    print('Não aceitamos objetos tão pesados')
                    print('Por favor entre com o peso desejado novamente')
                    continue
            else:
                print('Peso negativo ou igual a 0 informado')
                print('Entre com as dimensões desejados novamente')
                continue
        except ValueError:
            print('Você digitou alguma dimensão com valores não numéricos')


def rotaObjeto():
    while True:
        print('__________SELECIONE A ROTA DESEJADA_________')
        print('| CODIGO |            CIDADE               |')
        print('|   RS   | De Rio de Janeiro até São Paulo |')
        print('|   SR   | De São Paulo até Rio de Janeiro |')
        print('|   BS   | De Brasília até São Paulo       |')
        print('|   SB   | De São Paulo até Brasília       |')
        print('|   BR   | De Brasília até Rio de Janeiro  |')
        print('|   RB   | De Rio de Janeiro até Brasília  |')
        print('|' + '_' * 42 + '|')
        rotas = input('')

        if rotas == 'RS':
            return 1
        elif rotas == 'SR':
            return 1
        elif rotas == 'BS':
            return 1.2
        elif rotas == 'SB':
            return 1.2
        elif rotas == 'BR':
            return 1.5
        elif rotas == 'RB':
            return 1.5
        else:
            print('Você digitou uma rota que não existe')
            print('Entre com a rota desejada novamente')
            continue


print('Bem vindo a Companhia de Logistica do Sérgio Luiz Neves Rodrigues')
dimensao = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensao * peso * rota
print('Total a pagar R$ {} (dimensões: {} * peso: {} * rota: {}) '.format(total, dimensao, peso, rota))

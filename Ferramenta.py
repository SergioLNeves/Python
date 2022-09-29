listadepecas = [] 
def cadastrarPeca(pecas):
    print('Você selecionou a opção de Cadastrar Peça')
    print('Código da peça é {}' .format(pecas))
    nome = input('Por favor entre com o nome da peça: ')
    fabricante = input('Por favor entre com o nome da Fabricante: ')
    valor = float(input('Por favor entre com o Valor(R$) da peça: '))
    dicionariopeca = {'codigo'     : pecas,
                      'nome'       : nome,
                      'fabricante' : fabricante,
                      'valor'      : valor}
    listadepecas.append(dicionariopeca.copy())

def consultarPeca():
    while True:
        try:
            print('Você selecionou a opção de Consultar Peça')
            pecaconsultar = int(input('|        Escolha a opção desejada     | \n'
                                      '| 1 -    Consultar todas as peças     | \n'
                                      '| 2 -   Consultar peças por codigo    | \n'
                                      '| 3 - Consultar peças por Fabricantes | \n'
                                      '| 4 -            Retornar             | \n'
                                      '>>'))
            if pecaconsultar == 1:
                for consultor in listadepecas:
                    print('----------------------------')
                    for key, value in consultor.items():
                        print('{} : {}' .format(key,value))
                    print('____________________________')
            elif pecaconsultar == 2:
                entrada = int(input('Digite o Codigo da Peça: '))
                for consultor in listadepecas:
                    if (consultor['codigo'] == entrada):
                        print('----------------------------')
                        for key, value in consultor.items():
                            print('{} : {}'.format(key, value))
                        print('____________________________')

            elif pecaconsultar == 3:
                entrada = input('Digite o Fabricante da peça: ')
                for consultor in listadepecas:
                    if (consultor['fabricante'] == entrada):
                        print('----------------------------')
                        for key, value in consultor.items():
                            print('{} : {}'.format(key, value))
                        print('____________________________')

            elif pecaconsultar == 4:
                return
            else:
                print('Ops, Você digitou algo errado! escolha apenas uma das opções do menu')
                continue


        except ValueError:
            print('Ops, Você digitou algo errado! escolha exatamente uma das opções do menu')

def removerPeca():
    print('Você selecionou a opção de Remover Peça')
    entrada = int(input('Digite o Codigo da peça a ser Removida: '))
    for consultor in listadepecas:
        if (consultor['codigo'] == entrada):
            listadepecas.remove(consultor)



print('Bem vindo ao Controle de Estoque da Bicicletaria do Sérgio Luiz Neves Rodrigues')
contpeca = 0
while True:
    try:
        opcao = int(input('| Digite a opção desejada | \n'
                          '| 1 - Cadastrar Peças     |\n'
                          '| 2 - Consultar Peças     |\n'
                          '| 3 -  Remover Peças      |\n'
                          '| 4 - Sair do Programa    |\n'
                          '>>'))
        if opcao == 1:
            contpeca += 1
            cadastrarPeca(contpeca)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Obrigado por utilizar nosso programa')
            break
        else:
            print('Ops, Você digitou algo errado! escolha apenas uma das opções do menu')
            continue
    except ValueError:
        print('Ops, Você digitou algo errado! escolha exatamente uma das opções do menu')

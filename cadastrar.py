def validar(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def existe(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cria(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} criado com sucesso! \n'.format(arquivo))


def cadastrarjogo(arquivo, jogo, console):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{} \n'.format(jogo, console))
    finally:
        a.close()


def listar(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())


arquivo = 'games.txt'
if existe(arquivo):
    print('Arquivo localizado no sistema')
else:
    print('Arquivo inexistente')
    cria(arquivo)
    ####PRINCIPAL
while True:
    print('Menu')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = validar('Escolha a opção desejadas: ', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecidonada... \n')
        jogo = input('Qual o nome do jogo: ')
        console = input('Qual o nome do videogame: ')
        cadastrarjogo(arquivo, jogo, console)

    elif op == 2:
        print('Opção de listar cadastros selecidonada... \n')
        listar(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break

print('Bem Vindo a Loja de Sérgio Luiz Neves Rodrigues')
ru4087749 = float(input('Qual o valor do produto: '))
if ru4087749 != 0:
    quantidade = int(input('Quantidade de produtos: '))
    if quantidade != 0:
        if quantidade <= 9:
            semd = (ru4087749 * quantidade)
            desconto = semd * 0.0
            print('Valor do produto sem desconto é de R$ {:.2f}'.format(semd))
            print('Valor do produto com desconto é de R$ {:.2f}  (0% de desconto)'.format(semd - desconto))

        elif 10 <= quantidade <= 99:
            semd = (ru4087749 * quantidade)
            desconto = semd * 0.05
            print('Valor do produto sem desconto é de R$ {:.2f}'.format(semd))
            print('Valor do produto com desconto é de R$ {:.2f}  (5% de desconto)'.format(semd - desconto))

        elif 100 <= quantidade <= 999:
            semd = (ru4087749 * quantidade)
            desconto = semd * 0.10
            print('Valor do produto sem desconto é de R$ {:.2f}'.format(semd))
            print('Valor do produto com desconto é de R$ {:.2f}  (10% de desconto)'.format(semd - desconto))

        elif quantidade >= 1000:
            semd = (ru4087749 * quantidade)
            desconto = semd * 0.15
            print('Valor do produto sem desconto é de R$ {:.2f}'.format(semd))
            print('Valor do produto com desconto é de R$ {:.2f}  (15% de desconto)'.format(semd - desconto))

    else:
        print('Quantidade Invalida')
        print('Insira uma quantidade valida para e realizar a pesquisa de preço da loja')

else:
    print('Valor Invalido')
    print('Insira um valor valido para realizar a pesquisa de preço da loja')

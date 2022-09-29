print('Hoje no nosso cardápio temos os seguintes pratos')

print('1 - Arroz, feijão e batata frita com strogonoff ------ 18 reais')
print('2 - Macarrão, feijão e salsicha ------ 30 reais')
print('3 - Rodizio de churrasco com bebida liberado ------- 60 reais')

produto = int(input('Qual a sua escolha? '))
quantidade = int(input('Quantidade de pedidos '))
if(produto == 1):
  pagar = quantidade * 18
  print('Você comprou {} no prato de strogonoff. Total a pagar: {} ' .format(quantidade, pagar))
else:
  if(produto == 2):
    pagar = quantidade* 30
    print('Você comprou {} no prato de macarrão com salsicha, total a pagar: {}' .format(quantidade, pagar))
  else:
    if(produto == 3):
      pagar = quantidade * 60
      print('Você comprou {} no rodizio, total a pagar: {}' .format(quantidade, pagar))
    else:
      print('Produto Inexistente')

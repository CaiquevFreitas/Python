produto = []
preco = []
continuar = ''
total = 0
maior_valor = 0
menor_valor = 99999999999999999999999999999999
quant = 0
print("-"*35)
print("\tMercadão da Bahia")
print("-"*35)
while True:
    produto = input("Nome do produto: ").capitalize()
    preco = float(input("Preço do produto: R$"))
    continuar = input("Deseja continuar? [S/N] ").upper()
    total += preco
    quant += 1
    while preco > maior_valor:
        maior_valor = preco
        nome_maior = produto
    while preco < menor_valor:
        menor_valor = preco
        nome_menor = produto
    if continuar != 'S':
        break
print('{:-^40}'.format(' Fim do Programa '))
print("Você comprou {} produto(s), o total da compra foi R${:.2f}".format(quant,total))
print("O produto mais caro foi {}, custando R${:.2f}".format(nome_maior, maior_valor))
print("O produto mais barato foi {}, custando R${:.2f}".format(nome_menor, menor_valor))

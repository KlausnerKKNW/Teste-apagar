codigo = int(input('Insira o código do item: '))
quantidade = int(input('Insira a quantidade: '))

if codigo == 100:
    nome = 'cachorro quente'
    preco = 1.2
elif codigo == 101:
    nome = 'bauru simples'
    preco = 1.3
elif codigo == 102:
    nome = 'bauru com ovo'
    preco = 1.5
elif codigo == 103:
    nome = 'hambúrguer'
    preco = 1.2
elif codigo == 104:
    nome = 'cheeseburger'
    preco = 1.3
elif codigo == 105:
    nome = 'refrigerante'
    preco = 1

valor_total = preco * quantidade

print(f'Esse é o valor total da compra de {quantidade} {nome}: {valor_total}')

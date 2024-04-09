codigo = input('Insira o código do produto: ')
quantidade = int(input('Insira a quantidade desejada do produto: '))
if codigo == 'ABCD':
    preco = 5.3
    print(f'O preço total será: {preco * quantidade}')
elif codigo == 'XYPK':
    preco = 6
    print(f'O preço total será: {preco * quantidade}')
elif codigo == 'KLMP':
    preco = 3.2
    print(f'O preço total será: {preco * quantidade}')
elif codigo == 'QRST':
    preco = 2.5
    print(f'O preço total será: {preco * quantidade}')
else:
    print('Valor inválido')
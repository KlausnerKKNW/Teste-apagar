codigo = int(input('Insira o código do produto: '))
quantidade = int(input('Insira a quantidade desejada do produto: '))
if codigo == 1001:
    preco = 5.32
elif codigo == 1324:
    preco = 6.45
elif codigo == 6548:
    preco = 2.37
elif codigo == 987:
    preco = 5.32
elif codigo == 7623:
    preco = 6.45

print(f'O preço total será: {preco * quantidade}')
total = int(input('Insira a quantidade total: '))
itens = int(input('Insira a quantidade de itens: '))
if itens > 10 and total > 100:
    descont = total * 0.15
else:
    desconto = total * 0.06

print(f'O desconto é {desconto}')

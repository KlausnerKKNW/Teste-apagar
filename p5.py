aluguel = float(input('Insira o valor do aluguel: '))
area = float(input('Insira a área do imóvel: '))
total = float(input('Insira o valor total do imóvel: '))
if area > 50:
    if total > 350000:
        if aluguel > 1800:
            preco = aluguel * 12 + total
        else:
            preco = aluguel * 6 + total
    else:
        preco = aluguel + total
else:
    preco = total * 1.12

print(f'O preço final do imóvel é: {preco:.2f}')
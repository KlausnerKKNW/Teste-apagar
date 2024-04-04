total = float(input('Insira o total da nota fiscal: '))
serie = input('Insira a serie da nota fiscal: ')
if serie == 'E1':
    if total > 180:
        imposto = total * 0.17
    else:
        imposto = total * 0.14
else:
    if total > 199:
        imposto = total * 0.13
    else:
        imposto = total * 0.16

print(f'Esse é o valor do imposto: {imposto}')

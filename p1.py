idade = int(input('Insira sua idade: '))
altura = float(input('Insira sua altura: '))
if idade > 17:
    if altura > 160:
        bolsa = 1120
    else:
        bolsa = 1410
else:
    bolsa = 1439

print(f'De acordo com sua idade e altura, sua bolsa é: {bolsa}')

from math import pow

saldo = float(input('Insira seu saldo: '))
dias = int(input('Insira a quantidade de dias: '))
if saldo < 0:
    if dias < 30:
        saldo = saldo * 1.04
    else:
        saldo = saldo + pow((0.8), dias)
else:
    if dias < 30:
        saldo = saldo * 1.08
    else:
        saldo = saldo + pow((0.7), dias)

print(f'Esse é o seu saldo final: {saldo}')

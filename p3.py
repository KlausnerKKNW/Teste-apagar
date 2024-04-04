x1 = float(input('Digite o valor do x1: '))
y1 = float(input('Digite o valor do y1: '))
x2 = float(input('Digite o valor do x2: '))
y2 = float(input('Digite o valor do y2: '))
d1 = (x2 - x1)**2
d2 = (y2 - y1)**2
if d1 > d2:
    if x1 > x2:
        alfa = d1 * (x1)**2
    else:
        alfa = d1 * (x2)**2
else:
    alfa = (d2 - d1)**2

print(f'O valor do alfa vai ser: {alfa}')

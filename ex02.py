import math

a = int(input('Digite um número positivo: '))
b = int(input('Digite outro número positivo: '))
c = int(input('Digite outro número positivo: '))
if a >= 0 and b >= 0 and c >= 0:
    r = math.pow(a + b, 2)
    s = math.pow(b + c, 2)
    d = (r + s) / 2
    print('D é: ', d)
else:
    print('Valor inválido')
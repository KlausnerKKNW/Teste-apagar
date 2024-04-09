a = float(input('Insira a medida do lado a: '))
b = float(input('Insira a medida do lado b (base): '))
c = float(input('Insira a medida do lado c (altura): '))
if a >= b + c:
    print(f'Como {a} >= {b} + {c}, esse triângulo não existe.')
elif b >= a + c:
    print(f'Como {b} >= {a} + {c}, esse triângulo não existe')
elif c >= b + a:
    print(f'Como {c} >= {b} + {a}, esse triângulo não existe')
else:
    area = (b * c)/2
    print(f'A área do triângulo é: {area}')
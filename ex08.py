a = float(input('Insira o valor do coeficiente a: '))
b = float(input('Insira o valor do coeficiente b: '))
c = float(input('Insira o valor do coeficiente c: '))
d = float(input('Insira o valor do coeficiente d: '))
e = float(input('Insira o valor do coeficiente e: '))
f = float(input('Insira o valor do coeficiente f: '))

x = c*e - b*f / a*e - b*d
y = a*f - c*d / a*e - b*d

print(f'Os valores são: x = {x}; y = {y}')

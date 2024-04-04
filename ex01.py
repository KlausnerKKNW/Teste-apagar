import math

x1 = float(input('Digite a abscissa do ponto 1: '))
y1 = float(input('Digite a ordenada do ponto 1: '))
x2 = float(input('Digite a abscissa do ponto 2: '))
y2 = float(input('Digite a ordenada do ponto 2: '))

d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print('A distância entre os dois pontos é: ', d)
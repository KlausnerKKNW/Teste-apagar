custo_fabrica = float(input('Insira o custo de fábrica de um carro:'))
custo_consumidor = custo_fabrica + (custo_fabrica*0.28) + (custo_fabrica * 0.45)
print(f'Esse é o preço do carro para o consumidor: {custo_consumidor}')

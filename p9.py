idade = int(input('Insira sua idade: '))
tempo = int(input('insira seu tempo: '))
if idade > 65 or tempo > 35:
    aposentadoria = 100/100
else:
    aposentadoria = 75/100

print(f'Essa é a sua aposentadoria: {aposentadoria}')
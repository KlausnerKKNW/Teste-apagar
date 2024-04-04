idade = int(input('Insira a idade de um nadador: '))

if idade >= 18:
    classificacao = 'adulto'
elif idade >= 14:
    classificacao = 'juvenil B'
elif idade >=11:
    classificacao = 'juvenil A'
elif idade >= 8:
    classificacao = 'infantil B'
elif idade >= 5:
    classificacao = 'infantil A'
else:
    classificacao = 'inválido'

print(f'O nadador está na categoria: {classificacao}')

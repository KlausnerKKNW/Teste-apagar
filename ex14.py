nome = input('Insira o nome do aluno: ')
n1 = float(input('Digite a nota 1 de um aluno: '))
n2 = float(input('Digite a nota 2 de um aluno: '))
n3 = float(input('Digite a nota 3 de um aluno: '))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if maior == n1:
    m = (maior*4 + n2*3 + n3*3) / 10
elif maior == n2:
    m = (maior*4 + n1*3 + n3*3) / 10
else:
    m = (maior*4 + n1*3 + n2*3) / 10

print(f'Nome do aluno: {nome}')
print(f'Nota 1 do {nome}: {n1}')
print(f'Nota 2 do {nome}: {n2}')
print(f'Nota 3 do {nome}: {n3}')
print(f'Média do aluno {nome}: {m}')

if m >= 5:
    print(f'Aluno {nome} aprovado com média {m}')
else:
    print(f'Aluno {nome} reprovado com média {m}')
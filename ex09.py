n1 = float(input('Digite a nota 1 de um aluno: '))
n2 = float(input('Digite a nota 2 de um aluno: '))
n3 = float(input('Digite a nota 3 de um aluno: '))

m = (n1*2 + n2*3 + n3*5) / 10

if m >= 6:
    print(f'Aluno aprovado com média {m}')
else:
    print(f'Aluno reprovado com média {m}')
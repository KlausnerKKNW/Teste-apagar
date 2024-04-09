salario = float(input('Insira o seu salário: '))
cargo = int(input('Insira o código do seu cargo: '))
if cargo == 101:
    salario_novo = salario * 1.1
elif cargo == 101:
    salario_novo = salario * 1.2
elif cargo == 103:
    salario_novo = salario * 1.3
else:
    salario_novo = salario * 1.4

print(f'O seu salário de : {salario}, receberá um aumento de {salario_novo - salario}, e ficará: {salario_novo}')

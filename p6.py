idade = int(input('Insira sua idade: '))
renda = float(input('Insira sua renda: '))
experiencia = int(input('Insira seus anos de experiência: '))
if idade < 18:
    if experiencia < 6:
        if renda <= 1200:
            imposto = 0
        else:
            imposto = renda * 0.04
    else:
        if experiencia > 18:
            imposto = renda * 0.16
        else:
            imposto = renda * 0.14
else:
    imposto = renda * 0.22

print(f'Esse é o valor do imposto: {imposto:.2f}')
a = float(input('Digite um primeiro valor: '))
b = float(input('Digite um segundo valor: '))
c = float(input('Digite um terceiro valor: '))
maior = a
if b > a:
    if c > b:
        maior = c
    else:
        maior = b
elif c > a:
    maior = c

print(f'O maior valor é {maior}')


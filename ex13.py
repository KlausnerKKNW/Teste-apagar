a = int(input('Digite um primeiro valor inteiro: '))
b = int(input('Digite um segundo valor inteiro: '))
c = int(input('Digite um terceiro valor inteiro: '))
maior = a
if b > a:
    if c > b:
        maior = c
    else:
        maior = b
elif c > a:
    maior = c

print(f'O maior valor é {maior}')
a = float(input('Insira um número para a: '))
b = float(input('Insira um número para b: '))
c = float(input('Insira um número para c: '))

maior = a
menor = maior
meio = maior

if a == b == c:
    maior = a
    menor = a
    meio = a
    maiori = maior
    maiorp = maior
    if maior % 2 == 0:
        print('Não foi inserido um número ímpar.')
    if maior % 2 != 0:
        print('Não foi inserido um número par')
elif a == b and a != c:

    if c > maior:
        maior = c
    
    if a < menor:
        menor = a
    if c < menor:
        menor = c
    
    if maior % 2 == 0:
        maiorp = maior
        if menor % 2 == 0:
            print('Não foi inserido um número ímpar.')                
        else:
            maiori = menor
    if maior % 2 != 0:
        maiori = maior
        if menor % 2 != 0:
            print('Não foi inserido um número par.')
        else:
            maiorp = menor


elif a == c and a != b:

    if b > maior:
        maior = b
    
    if a < menor:
        menor = a
    if b < menor:
        menor = b
    
    if maior % 2 == 0:
        maiorp = maior
        if menor % 2 == 0:
            print('Não foi inserido um número ímpar.')                
        else:
            maiori = menor
    if maior % 2 != 0:
        maiori = maior
        if menor % 2 != 0:
            print('Não foi inserido um número par.')
        else:
            maiorp = menor

elif b == c and b != a:
    maior = b
    meio = b

    if a > maior:
        maior = a
    
    if b < menor:
        menor = b
    if a < menor:
        menor = a
    
    if maior % 2 == 0:
        maiorp = maior
        if menor % 2 == 0:
            print('Não foi inserido um número ímpar.')                
        else:
            maiori = menor
    if maior % 2 != 0:
        maiori = maior
        if menor % 2 != 0:
            print('Não foi inserido um número par.')
        else:
            maiorp = menor

elif a != b and b != c and a != c:

    if b > maior:
        maior = b
    if c > maior:
        maior = c
    
    if a < menor:
        menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    
    if a < maior and a > menor:
        meio = a
    elif b < maior and b > menor:
        meio = b
    elif c < maior and c > menor:
        meio = c

    if maior % 2 == 0:
        maiorp = maior
        if meio % 2 == 0:
            if menor % 2 == 0:
                print('Não foi inserido um número ímpar.')
            else:
                maiori = menor
        if meio % 2 != 0:
            maiori = meio

    elif maior % 2 != 0:
        maiori = maior
        if meio % 2 != 0:
            if menor % 2 != 0:
                print('Não foi inserido um número par.')
            else:
                maiorp = menor
        else:
            maiorp = meio

if maior % 2 == 0 and meio % 2 == 0 and menor % 2 == 0:
    print(f'O maior número par é: {maiorp}')
elif maior % 2 != 0 and meio % 2 != 0 and menor % 2 != 0:
    print (f'O maior número ímpar é: {maiori}')
else:
    print(f'O maior número par é: {maiorp}')
    print(f'O maior número ímpar é: {maiori}')
    
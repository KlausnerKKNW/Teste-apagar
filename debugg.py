for c in range(1, 10):
    a = c
    for c in range(1, 10):
        b = c
        for d in range(1, 10):
            c = d
            maior = a
            maior2 = 0
            maior3 = 0
            bt = 0
            ct = 0
            if a == b and b == c:
                bt = b + 1
                ct = c + 2
                b1 = b
                c1 = c
                b = bt
                c = ct
            elif a == b and b != c:
                bt = b + 1
                if bt == c:
                    bt += 1
                b1 = b
                b = bt
            elif a == c and a != b:
                ct = c + 1
                if ct == b:
                    ct += 1
                c1 = c
                c = ct
            elif b == c and b != a:
                bt = b + 1
                if bt == a:
                    bt += 1
                b1 = b
                b = bt
            if b > maior:
                maior = b
            if c > maior:
                maior = c
            if a < maior and a > maior2:
                maior2 = a
            if b < maior and b > maior2:
                maior2 = b
            if c < maior and c > maior2:
                maior2 = c
            if a < maior and a < maior2:
                maior3 = a
            if b < maior and b < maior2:
                maior3 = b
            if c < maior and c < maior2:
                maior3 = c
            if maior == bt:
                maior = b1
            if maior == ct:
                maior = c1
            if maior2 == bt:
                maior2 = b1
            if maior2 == ct:
                maior2 = c1
            if maior3 == bt:
                maior3 = b1
            if maior3 == ct:
                maior3 == c1
            if maior % 2 != 0:
                mi = maior
            elif maior2 % 2 != 0:
                mi = maior2
            elif maior3 % 2 != 0:
                mi = maior3
            else:
                mi = ''
            print(f'O a é: {a}')
            print(f'O b é: {b}')
            print(f'O c é: {c}')
            if maior % 2 == 0 and mi != '':
                print(f'O maior número par é: {maior}')
                print(f'O maior número ímpar é: {mi}')
            elif maior2 % 2 == 0 and mi != '':
                print(f'O maior número par é: {maior2}')
                print(f'O maior número ímpar é: {mi}')
            elif maior3 % 2 == 0 and mi != '':
                print(f'O maior número par é: {maior3}')
                print(f'O maior número ímpar é: {mi}')
            elif maior % 2 != 0 and maior2 % 2 != 0 and maior3 % 2 != 0:
                print(f'O maior número ímpar é: {maior}')
                print('Não foi inserido número par')
            elif maior % 2 == 0 and maior2 % 2 == 0 and maior3 % 2 == 0:
                print(f'O maior número par é: {maior}')
                print('Não foi inserido número ímpar.')

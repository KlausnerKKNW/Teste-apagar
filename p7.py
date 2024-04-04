cargo = input('Insira o seu cargo: ')
nivel_acesso = input('Insira o seu nível de acesso: ')
seguranca = input('Insira a segurança: ')
if cargo == 'CEO':
    if nivel_acesso == 1:
        if seguranca == 0:
            tempo = 166
        else:
            tempo = 150
    else:
        if seguranca > 0:
            tempo = 120
        else:
            tempo = 115
else:
    if nivel_acesso > 1:
        tempo = 110
    else:
        tempo = 106

print(f'Esse é o tempo: {tempo}')

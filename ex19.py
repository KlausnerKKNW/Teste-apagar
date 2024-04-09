n1 = float(input('Insira a nota 1: '))
n2 = float(input('Insira a nota 2:'))
n3 = float(input('Insira a nota 3: '))
media_e = int(input('''Insira 1, caso queira média aritmética;
Insira 2, caso queira média ponderada (3, 3, 4);
Insira 3, caso queira média harmônica: '''))

if media_e == 1:
    mn = 'média aritmética'
    m = (n1 + n2 + n3)/3
elif media_e == 2:
    mn = 'média ponderada'
    m = (n1*3 + n2*3 + n3*4)/10
elif media_e == 3:
    mn = 'média harmônica'
    m = 3/(1/n1 + 1/n2 + 1/n3)

print(f'A {mn} das notas é: {m}')


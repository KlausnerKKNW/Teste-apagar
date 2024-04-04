idade_dia = int(input('Digite sua idade em dias totais: '))
ano = idade_dia//365
mes = (idade_dia%365)//30
dia = (idade_dia%365)%30

print('Sua idade é: ', ano, 'anos, ', mes, 'meses, ', dia, 'dias.')
print(f'Essa é a sua idade em anos totais: {idade_dia / 365}')
print(f'Essa é a sua idade em meses totais: {idade_dia / 30:.0f}')
print(f'Essa é a sua idade em dias totais: {idade_dia}')
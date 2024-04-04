ano = int(input('Digite a sua idade em anos: '))
mes = int(input('Digite a sua idade com os meses a mais: '))
dia = int(input('Digite a sua idade com os dias a mais: '))

dia_total = ano*365 + mes*30 + dia

print(f'Essa é a sua idade expressa em dias totais: {dia_total}')
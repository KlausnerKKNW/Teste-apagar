evento = float(input('Digite o tempo em segundos do evento da fábrica: '))

hora = evento//3600
minuto = (evento%3600)//60
segundo = (evento%3600)%60

print(f'Esse evento é de duração: {hora} horas, {minuto} minutos, {segundo} segundos')

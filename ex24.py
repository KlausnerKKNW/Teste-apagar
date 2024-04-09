hi = int(input('Digite a hora de início do jogo (hora inteira): '))
hf = int(input('Digite a hora do final do jogo (hora inteira): '))
d = hf - hi
if d <= 24:
    print(f'A duração do jogo, em horas, é de {d}')
if d > 24:
    print(f'Inválido. A duração máxima do jogo deve ser de 24 horas, e nesse caso é de: {d} horas')

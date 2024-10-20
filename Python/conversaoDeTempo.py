entrada = int(input())
hora = entrada // 3600
minuto = (entrada % 3600) // 60
segundo = (entrada % 3600) % 60
print(f'{hora}:{minuto}:{segundo}')
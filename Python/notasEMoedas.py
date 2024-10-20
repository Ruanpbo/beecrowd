def reduzir(valor):
    notas = [100.00,50.00,20.00,10.00,5.00,2.00]
    moedas = [1.00,0.50,0.25,0.10,0.05,0.01]
    quantidades = []
    quantidadesmoedas = []

    for nota in notas:
        quantidades.append(valor // nota)
        valor %= nota
    
    for moeda in moedas:
        quantidadesmoedas.append(valor // moeda)
        valor %= moeda

    return quantidades, quantidadesmoedas

quantidades = reduzir(float(input()))

print("NOTAS:")
print(f"{int(quantidades[0][0])} nota(s) de R$ 100.00")
print(f"{int(quantidades[0][1])} nota(s) de R$ 50.00")
print(f"{int(quantidades[0][2])} nota(s) de R$ 20.00")
print(f"{int(quantidades[0][3])} nota(s) de R$ 10.00")
print(f"{int(quantidades[0][4])} nota(s) de R$ 5.00")
print(f"{int(quantidades[0][5])} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(quantidades[1][0])} moeda(s) de R$ 1.00")
print(f"{int(quantidades[1][1])} moeda(s) de R$ 0.50")
print(f"{int(quantidades[1][2])} moeda(s) de R$ 0.25")
print(f"{int(quantidades[1][3])} moeda(s) de R$ 0.10")
print(f"{int(quantidades[1][4])} moeda(s) de R$ 0.05")
print(f"{int(quantidades[1][5])} moeda(s) de R$ 0.01")
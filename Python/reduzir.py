def reduzir(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidades = []

    for nota in notas:
        quantidades.append(valor // nota)
        valor %= nota

    return quantidades

quantidades = reduzir(int(input()))

notas = [100, 50, 20, 10, 5, 2, 1]
for i, quantidade in enumerate(quantidades):
    print(f"{quantidade} nota(s) de R$ {notas[i]},00")
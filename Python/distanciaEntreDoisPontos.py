valor1 = input().split()
valor2 = input().split()

x1 = float(valor1[0])
y1 = float(valor1[1])
x2 = float(valor2[0])
y2 = float(valor2[1])

produto = (x2 - x1)**2 + (y2 - y1)**2

distancia = (produto ** (1/2))

print(f"{distancia:.4f}")
valor = input().split

a = float(valor[0])
b = float(valor[1])
c = float(valor[2])

triangulo = a * c / 2
print(f"TRIANGULO = {triangulo:.3f}")

circulo = 3.14159 * c ** 2
print(f"CIRCULO: {circulo:.3f}")

trapezio = (b + a) * c / 2
print(f"TRAPEZIO: {trapezio:.3f}")

quadrado = b ** 2
print(f"QUADRADO: {quadrado:.3f}")

retangulo = a * b
print(f"RETANGULO: {retangulo:.3f}")
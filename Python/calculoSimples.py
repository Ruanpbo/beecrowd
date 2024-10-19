# Leitura dos dados de entrada
linha1 = input().split()
linha2 = input().split()

# Extração dos valores da primeira linha
codigo1 = int(linha1[0])
numero_pecas1 = int(linha1[1])
valor_unitario1 = float(linha1[2])

# Extração dos valores da segunda linha
codigo2 = int(linha2[0])
numero_pecas2 = int(linha2[1])
valor_unitario2 = float(linha2[2])

# Cálculo do valor total a ser pago
valor_total = (numero_pecas1 * valor_unitario1) + (numero_pecas2 * valor_unitario2)

# Impressão do resultado
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")
def maiorAB(a, b):
    return(a + b + valor_absoluto(a-b)) // 2

def valor_absoluto(num):
    return -num if num < 0 else num

valor = input().split()

a = int(valor[0])
b = int(valor[1])
c = int(valor[2])

maior = maiorAB(a, b)
maior = maiorAB(maior, c)

print(f"{maior} eh o maior")
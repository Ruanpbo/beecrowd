n = int(input())
anos = n // 365
mes = (n % 365) // 30
dias = (n % 365) % 30

print(f"{anos} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")
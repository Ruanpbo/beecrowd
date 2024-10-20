valor = int(input())

cem = 0
cin = 0
vin = 0
dez = 0
fiv = 0
doi = 0
one = 0

while valor >=  100:
    valor -= 100
    cem += 1
else:
    while valor >= 50:
        valor -= 50
        cin += 1
    else:
        while valor >= 20:
            valor -= 20
            vin += 1
        else:
            while valor >= 10:
                valor -= 10
                dez += 1
            else:
                while valor >= 5:
                    valor -= 5
                    fiv += 1
                else:
                    while valor >= 2:
                        valor -= 2
                        doi += 1
                    else:
                        while valor > 0:
                            valor -= 1
                            one += 1

print(f"{cem} nota(s) de R$ 100,00")
print(f"{cin} nota(s) de R$ 50,00")
print(f"{vin} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{fiv} nota(s) de R$ 5,00")
print(f"{doi} nota(s) de R$ 2,00")
print(f"{one} nota(s) de R$ 1,00")
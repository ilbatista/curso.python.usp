numero = int(input("Informe um número inteiro: "))
contador = 0

for i in range(2,numero):
    if (numero % i == 0):
        contador += 1

if (contador > 0):
    print("não primo")
else:
    print("primo")
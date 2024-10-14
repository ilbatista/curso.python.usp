numero = input("Informe um número inteiro: ")
cont = 0

for i in range(len(numero)-1):
    if (numero[i] == numero[i+1]):
        cont += 1

if cont != 0:
    print("sim")
else:
    print("não")
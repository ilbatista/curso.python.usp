n = int(input("Informe um número inteiro: "))

contador = 1
repeticao = 1

while(repeticao <= n):
    if(contador % 2 != 0):
        print(contador)
        repeticao += 1
    contador += 1
    
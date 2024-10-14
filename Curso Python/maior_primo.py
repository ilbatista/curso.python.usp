def éPrimo(numero):
    contador = 0

    for i in range(2,numero):
        if (numero % i == 0):
            contador += 1

    if (contador > 0):
        return False
    else:
        return True
    
def maior_primo(numero):
    maiorprimo = 0
    cont = 1

    if(éPrimo(numero)):
        maiorprimo = numero
    else:
        for i in range(2,numero):
            if(éPrimo(i)):
                maiorprimo = i
    
    return maiorprimo

x = int(input("Informe um número inteiro:"))

print(maior_primo(x))
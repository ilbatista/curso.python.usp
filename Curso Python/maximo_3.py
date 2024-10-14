def maximo(x, y, z):
    if x > y:
        maior = x
        if x < z:
            maior = z
    else:
        maior = y
        if(y < z):
            maior = z

    return maior
    
x = input("Primeiro número: ")
y = input("Segundo número: ")
z = input("Terceiro número: ")

print(maximo(x,y,z))
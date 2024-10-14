import math

x1 = int(input("Informe a coordenada x do primeiro ponto: "))
y1 = int(input("Informe a coordenada y do segundo ponto: "))
x2 = int(input("Informe a coordenada x do primeiro ponto: "))
y2 = int(input("Informe a coordenada y do segundo ponto: "))

distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if (distancia >= 10):
    print("longe")
else:
    print("perto")
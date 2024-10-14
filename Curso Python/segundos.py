num = int(input("Digite um número inteiro: "))
dias = num // 86400
num = num % 86400
horas = num // 3600
num = num % 3600
minutos = num // 60
segundos = num % 60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos")
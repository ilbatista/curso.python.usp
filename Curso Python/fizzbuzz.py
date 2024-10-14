num = input("Informe um número inteiro: ")
if (int(num) % 3 == 0) and (int(num) % 5 == 0):
    print("FizzBuzz")
else:
    print(num)
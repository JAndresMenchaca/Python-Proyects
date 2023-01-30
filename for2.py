print('TABLA DE MULTIPLICAR:')
num_U = int(input("Ingrese un numero: "))
num = 0
print("Esta es la tabla del {}".format(num_U))
for num in range(10):
    num += 1
    if num % 2 == 0:
        print("{} x {} = {}".format(num_U, num, num_U * num))
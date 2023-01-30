print('Introduzca numeros.\n')
numeros = []
resp = None
while resp != "N":
    resp = int(input("Numero: "))
    num = int(resp)
    numeros.append(num)
    print('La lista de numeros es:\n', numeros)

    resp = input("Desea añadir mas numeros a la lista??? [S]/[N]\n")
    if resp == "N":
        print('\n')
        break
    else:
        pass
print('La lista de numeros es:\n', numeros)
print("El numero mas grande en la lista es: ", max(numeros))
print("El numero mas pequeño en la lista es: ", min(numeros))
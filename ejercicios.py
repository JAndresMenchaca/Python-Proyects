def ejercicio1(*args):
    for word in args:
        len(word)
    return max(args, key=len)


def ejercicio2(*nums):
    total = 0
    for num in nums:
        total += num
    return total


def ejercicio3(num):
    es_impar = True
    if num % 2 == 0:
        es_impar = False
    return es_impar


def ejercicio4(answer):
    resp = False
    if answer == 1:
        resp = True
    elif answer == 2:
        resp = False
    else:
        return "Tu respuesta no es valida"
    return resp


def ejercicio5(word):
    return word.swapcase()


def ejercicio6(resp):
    win = False
    while not win:
        numero = int(input("Introduzca un numero del 1 al 100\n"))
        if 0 <= numero <= 100:
            if numero == resp:
                win = True
                return print("Ganaste!!!")
            else:
                pass
        else:
            print("Las respuesta no es valida")


def ejercicio7(lista):
    band = False
    while not band:
        print("La lista de compras es:\n", lista)
        resp = int(input("Quieres añadir un producto???\n"
                         "1. Si\n"
                         "2. No\n"))
        if resp == 1:
            producto = input('Que producto quieres añadir???\n')
            if producto not in lista:
                lista.append(producto)
            else:
                print("Este producto ya esta en la lista")
        elif resp == 2:
            band = True
            return print(lista)
        else:
            print("Respuesta no valida")
            ejercicio7(lista)


def main():
    print('Ejercicio 1')
    print(ejercicio1("hola", 'como', 'estas'))

    print("Ejercicio 2")
    print(ejercicio2(1, 2, 3, 4, 5))

    print('Ejercicio 3')
    print(ejercicio3(24))

    print("Ejercicio 4")
    answer = int(input("Estas seguro??\n"
                   "1. Si\n"
                   "2. No\n"))

    print(ejercicio4(answer))

    print('Ejercicio 5')
    print(ejercicio5("hola"))

    print('Ejercicio 6')
    print("Advina el numero del 1 al 100")
    ejercicio6(50)

    print("Ejercicio 7")
    lista = ["leche", "tomate", "huevos"]
    ejercicio7(lista)


if __name__ == "__main__":
    main()



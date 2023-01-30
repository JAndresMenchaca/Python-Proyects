print('Lista de compra')
lista = []
resp = None
while resp != 'Q':
    print('Que deseas comprar???\n'
          'Ingresa [Q] para salir\n')
    resp = input("Quiero comprar: ")

    if resp == 'Q':

        print('La lista de compras es:', lista)

    if resp in lista:
        print('Este articulo ya esta en la lista')
    else:
        resp1 = input("Seguro que quieres añadirlo a la lista??? [S/N]\n")
        if resp1 == 'S':
            lista.append(resp)
            print(resp, "ya se agrego a la lista\n")
        else:
            print('Este articulo no se va a añadir')

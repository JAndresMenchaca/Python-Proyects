def txt(lista):
    a = open("compras.txt", "w")
    a.write("\n".join(lista))
    a.close()
    
    '''
    nombre_fichero = input("Como quieres que se llame el archivo???")
    with open(nombre_fichero + '.txt', 'w') as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))
    '''


def verificando(lista):
    lista_compras = []
    band = False
    while not band:
        resp = input("Ingrese un producto:")

        if resp == 'LISTA':
            print("Esta es la lista:\n", lista)

        elif resp not in lista_compras and resp in lista:
            lista_compras.append(resp)

        elif resp == "salir":
            band = True
            return lista_compras

        elif resp == "mostrar":
            print("Esta es la lista:\n", lista_compras)


def main():
    lista = ["pan", 'pollo', 'yogurt', 'carne', 'agua']
    txt(lista)
    verificando(lista)


if __name__ == "__main__":
    main()
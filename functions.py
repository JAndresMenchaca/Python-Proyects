def main():
    def potencia(numero):

        resultado = numero * numero
        return resultado

    numero = int(input("Introduzca un numero:\n"))
    print('El {} elevado a la 2 es: {}'.format(numero, potencia(numero)))


if __name__ == "__main__":
    main()
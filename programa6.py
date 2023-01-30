print('Vamos a elegir tu nuevo telefono')
print('Vamos a contestar algunas preguntas')
a = int(input('ANDROID o IOS ??\n'
               '1. ANDROID\n'
               '2. IOS\n'))
if a == 1:
    a = int(input('Tienes dinero??\n'
                   '1. Si\n'
                   '2. No\n'))
    if a == 2:
        print('Compra un ANDROID chino de 100$')
    elif a == 1:
        a = int(input('Te importa la camara del telefono???\n'
                              '1. Si\n'
                              '2. No\n'))
        if a == 1:
            print('Debes comprar el Google Pixel Super Camara')
        elif a == 2:
            print('Debes comprar el Android calidad-precio')
        else:
            print('Debes elegir una opcion valida')
    else:
        print('Debes elegir una opcion valida')
elif a == 2:
    a = int(input('Tienes dinero??\n'
                   '1. Si\n'
                   '2. No\n'))
    if a == 1:
        print('Compra el iPhone 14 Pro Max')
    elif a == 2:
        print('Compra un iPhone de segunda mano')
    else: print('Debes elegir una opcion valida')

else:
    print('Elija una opcion valida')


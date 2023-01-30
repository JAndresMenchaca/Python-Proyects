import random
print('\nBatman: La noche de la tragedia\n')
print('Es una noche caotica, hay muchos crimenes en la ciudad... de repente Batman recibe una llamada...\n'
      'ES EL JOKER\n')
print('JOKER: Hola Batman!!! Para esta noche prepare algo muy especial, te tengo un desafio.\n'
      'Te dare dos direcciones, en cada una hay un rehen que espera ser rescatado, pero solo podras rescatar a uno.\n\n'
      'EL primero esta en la vieja Panaderia de ciudad Gotica, si no vas alla en 7 mins, mis hombres acabaran con el.\n'
      'El segundo rehen esta cerca del Banco Nacional.\n'
      'Tu decides a quien salvar\n')

p = int(input('A quien salvara Batman???\n'
              '1. EL primer rehen\n'
              '2. Al segundo rehen\n'))
if p == 1:
    print('Batman decide ir a salvar al primer rehen, se dirige a la panaderia.\n'
          'Llega a la panadeira, pero antes de salir del Batimovil, no esta seguro de llevar sus Batarangs\n')
    p = int(input('Batman llevara sus Batarangs???\n'
                  '1. Si\n'
                  '2. No\n'))
    batarang = False
    if p == 1:
        print("Batman decide llevar sus Batarangs")
        batarang = True
    elif p == 2:
        print("Batman decide no llevar sus Batarangs")
        batarang = False

    else:
        print("Perdiste, aprende a leer las instrucciones :(\n"
              "Debes elegir entre 1 y 2, vuele a intentarlo")
        exit()

    print('Una vez adentro, los matones del Joker lo esperan, Batman puede con ellos, pero se le escapa uno.\n'
          'Ese ultimo maton va directamente hacia el Rehen decidido a matarlo')
    p = int(input('Que hara Batman???\n'
                  '1. Perseguirlo\n'
                  '2. Buscar otra manera de detener al maton\n'))

    if p == 1:
        print('Batman no alcanza al maton\n'
              'El rehen muere\n'
              'GAME OVER')
    elif p == 2:
        print("Batman busca sus Batarangs para lanzarlos al maton")
        if batarang == True:
            print("BATMAN TIENE SUS BATARANGS!!!!\n"
                  "El maton cae, Batman logra salvar a este rehen.")
        else:
            print("BATMAN NO TIENE SUS BATARANGS\n"
                  "EL rehen muere\n"
                  "GAME OVER")
    else:
        print("Perdiste, aprende a leer las instrucciones :(\n"         
              "Debes elegir entre 1 y 2, vuele a intentarlo")
elif p == 2:
    print('Batman decide ir a por el segundo Rehen\n'
          'Llega al Banco Nacional, pero no logra encontralo\n')
    p = int(input('Que hara Batman???\n'
                  '1. Seguir buscando al Rehen\n'
                  '2. Buscar Pistas\n'))
    if p == 1:
        print('Batman sigue buscando...\n'
              'Pero no lo encuentra, el Rehen es encontrado 1 hora despues.\n'
              'Esta muerto.\nGAME OVER')
    elif p == 2:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        exe = num1 * num2
        print("Batman busca pistas... y encuentra un telefono, con este mensaje")
        print('Ahi dice:\n'
              '----------------------------------------\n'
              '             Hola Batman\n'
              '     Quieres encontrar al rehen???\n'
              '  Resuelve esto: ',num1, " * ", num2, '.\n'
              '  Si lo resuelves... sabras donde buscar\n'
              '----------------------------------------\n')
        p = int(input('Cual es la respuesta???\n'))
        if p == exe:
            print("El telefono muestra las coordenadas del Rehen a Batman")
            print("Esta un poco lejos, y tiene que llegar en 2 mins")

            p = int(input('En que vehiculo ira Batman???\n'
                          '1. En el Batimovil\n'
                          '2. En el Batiavion\n'))
            if p == 1:
                print("Batman ira en el Batimovil\n"
                      "No llega a tiempo, el rehen muere\n"
                      "GAME OVER")
            elif p ==2:
                print("Batman se sube en el Batiavion\n"
                      "Logra llegar a tiempo\n"
                      "Batman salva a este Rehen")
            else:
                print("Perdiste, aprende a leer las instrucciones :(\n"
                      "Debes elegir entre 1 y 2, vuele a intentarlo")
                exit()
        else:
            print("Esa no es la respuesta correcta\n"
                  "El rehen muere\n"
                  "GAME OVER")
    else:
        print("Perdiste, aprende a leer las instrucciones :(\n"
              "Debes elegir entre 1 y 2, vuele a intentarlo")
        exit()
else:
    print("Perdiste, aprende a leer las instrucciones :(\n"
          "Debes elegir entre 1 y 2, vuele a intentarlo")
    exit()
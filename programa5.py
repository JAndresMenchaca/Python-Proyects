print("Bienvenido al Test de Juegos")
p = int(input('Cual es tu personaje favorito???\n'
               '1. Mario Bros\n'
               '2. Kratos\n'
               '3. Jefe Maestro\n'))
nintendo = 0
sony = 0
microsoft = 0

if p == 1:
    nintendo += 1
elif p == 2:
    sony += 1
elif p == 3:
    microsoft += 1
else:
    print('Tenias que poner 1, 2 o 3')

p = int(input('Cual es tu juego favorito???\n'
                  '1. Legends of Zelda BOTW\n'
                  '2. GOW 2018\n'
                  '3. Halo 5\n'))
if p == 1:
    nintendo += 1
elif p == 2:
    sony += 1
elif p == 3:
    microsoft += 1
else:
    print('Tenias que poner 1, 2 o 3')

p = int(input('Cual es tu consola favorita???\n'
                  '1. Nintendo Switch\n'
                  '2. PS5\n'
                  '3. XBOX SERIES X\n'))
if p == 1:
    nintendo += 1
elif p == 2:
    sony += 1
elif p == 3:
    microsoft += 1
else:
    print('Tenias que poner 1, 2 o 3')

resp = max(nintendo, sony, microsoft)


if nintendo == sony == microsoft or nintendo == sony or sony == microsoft or microsoft == nintendo:
    print('No eres fanantico de ninguna compañia')
elif resp == nintendo:
    print('Tu eres fan de Nintendo')
elif resp == sony:
    print('Tu eres fan de Play Station')
elif resp == microsoft:
    print('Tu eres fan de Microsoft')



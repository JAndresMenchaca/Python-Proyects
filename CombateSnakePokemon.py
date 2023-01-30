import msvcrt
import os
from random import randint


def combate(nombre_pokemon, vida_pokemon):
    os.system('cls')
    VIDA_INICIAL_PIKACHU = vida_pokemon
    VIDA_INICIAL_SQUIRTLE = 90
    TAMANIO_BARRA = 10
    vida_pikachu = VIDA_INICIAL_PIKACHU
    vida_squirtle = VIDA_INICIAL_SQUIRTLE

    print('\nComienza el combate')
    barra_pikachu = int(vida_pikachu * TAMANIO_BARRA / VIDA_INICIAL_PIKACHU)
    barra_squirtle = int(vida_squirtle * TAMANIO_BARRA / VIDA_INICIAL_SQUIRTLE)

    print(nombre_pokemon + ':  [{}{}] ({}/{})'.format('#' * barra_pikachu, " " * (TAMANIO_BARRA - barra_pikachu),
                                                      vida_pikachu, VIDA_INICIAL_PIKACHU))

    print('Squirtle: [{}{}] ({}/{})'.format('#' * barra_squirtle, " " * (TAMANIO_BARRA - barra_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    input('Enter para continuar...\n')

    os.system("cls")

    while vida_pikachu > 0 and vida_squirtle > 0:

        print('Turno de ' + nombre_pokemon)
        ataque_pikachu = randint(1, 2)
        if ataque_pikachu == 1:
            print(nombre_pokemon + ' ataca con Bola Voltio')
            vida_squirtle -= 10
        else:
            print(nombre_pokemon + ' ataca con Onda Trueno')
            vida_squirtle -= 11

        if vida_pikachu <= 0:
            vida_pikachu = 0
        if vida_squirtle <= 0:
            vida_squirtle = 0

        barra_pikachu = int(vida_pikachu * TAMANIO_BARRA / VIDA_INICIAL_PIKACHU)
        barra_squirtle = int(vida_squirtle * TAMANIO_BARRA / VIDA_INICIAL_SQUIRTLE)

        print(nombre_pokemon + ':  [{}{}] ({}/{})'.format('#' * barra_pikachu, " " * (TAMANIO_BARRA - barra_pikachu),
                                                          vida_pikachu, VIDA_INICIAL_PIKACHU))

        print('Squirtle: [{}{}] ({}/{})'.format('#' * barra_squirtle, " " * (TAMANIO_BARRA - barra_squirtle),
                                                vida_squirtle, VIDA_INICIAL_SQUIRTLE))
        input('Enter para continuar...\n')
        os.system('cls')

        print('Turno de Squirtle')
        ataque_squirtle = None
        while ataque_squirtle not in [1, 2, 3, 4]:
            ataque_squirtle = int(input('Que ataque deseas realizar???\n'
                                        '1. Placaje (10)\n'
                                        '2. Pistola de Agua (12)\n'
                                        '3. Burbuja (9)\n'
                                        '4. Quedarse quieto\n'))
            os.system('cls')
            if ataque_squirtle == 1:
                print('Squirtle ataca con Placaje')
                vida_pikachu -= 10
            elif ataque_squirtle == 2:
                print('Squirtle ataca con Pistola de Agua')
                vida_pikachu -= 12
            elif ataque_squirtle == 3:
                print('Squirtle ataca con Burnuja')
                vida_pikachu -= 9
            elif ataque_squirtle == 4:
                print("Te quedas quieto")

            if vida_pikachu <= 0:
                vida_pikachu = 0
            if vida_squirtle <= 0:
                vida_squirtle = 0

            barra_pikachu = int(vida_pikachu * TAMANIO_BARRA / VIDA_INICIAL_PIKACHU)
            barra_squirtle = int(vida_squirtle * TAMANIO_BARRA / VIDA_INICIAL_SQUIRTLE)

            print(
                nombre_pokemon + ':  [{}{}] ({}/{})'.format('#' * barra_pikachu, " " * (TAMANIO_BARRA - barra_pikachu),
                                                            vida_pikachu, VIDA_INICIAL_PIKACHU))

            print('Squirtle: [{}{}] ({}/{})'.format('#' * barra_squirtle, " " * (TAMANIO_BARRA - barra_squirtle),
                                                    vida_squirtle, VIDA_INICIAL_SQUIRTLE))
            input('Enter para continuar...\n')
            os.system('cls')

    if vida_pikachu > vida_squirtle:
        print(nombre_pokemon + ' gana!!!')
        print('No lo derotaste')
        input('Enter para continuar...\n')
    else:
        print("Squirtle gana!!!")
        input('Enter para continuar...\n')


# -----------------------------------------------------#
POS_X = 0
POS_Y = 1

my_position = [6, 1]

obs = '''\
###########################
####                        
######          #####   ####
#####################   ####
###########                                 
          ##########  ######
###      ########         ##
#######               ######
####  #######               
###        ##########    ###
##################         #
###################      ###
#################                     
###################     ####
############################\
'''
obs = [list(row) for row in obs.split('\n')]
MAP_WIDTH = len(obs[0])
MAP_HEIGHT = len(obs)
cont = 0
lista_pokemon = ['Pikachu', 'Mewtwo', 'Snorlax', 'Lucario']
lista_vida = [80, 100, 90, 110]
endgame = False
tail = []
objects = [[22, 4], [13, 4], [4, 5], [19, 12]]
tail_l = 0

while not endgame:
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print('|', end="")
        for coordinate_x in range(MAP_WIDTH):

            if my_position[POS_X] == MAP_WIDTH:
                my_position[POS_X] = 0

            elif my_position[POS_X] == -1:
                my_position[POS_X] = 19

            elif my_position[POS_Y] == -1:
                my_position[POS_Y] = 14

            elif my_position[POS_Y] == MAP_HEIGHT:
                my_position[POS_Y] = 0
            char = " "

            food = None

            for obj in objects:
                if obj[POS_X] == coordinate_x and obj[POS_Y] == coordinate_y:
                    food = obj
                    char = "*"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char = "@"
                if food:
                    objects.remove(food)
                    os.system('cls')
                    combate(lista_pokemon[cont], lista_vida[cont])
                    cont += 1

            if obs[coordinate_y][coordinate_x] == '#':
                char = '#'
            if cont == 4:
                endgame = True

            print(' {} '.format(char), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = msvcrt.getwch()
    print(direction)

    position = None

    if direction == 'w':
        position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == 'a':
        position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == 's':
        position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == 'd':
        position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == 'q':
        endgame = True
    os.system('cls')

    if position:
        if obs[position[POS_Y]][position[POS_X]] != '#':
            tail.insert(0, my_position.copy())
            tail = tail[:tail_l]
            my_position = position

if endgame:
    os.system('cls')
    print('Felicidades!!! Acabaste el juego!!! ')
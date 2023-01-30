import os
from random import randint

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
TAMANIO_BARRA = 10
vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE


print('Comienza el combate')
barra_pikachu = int(vida_pikachu * TAMANIO_BARRA / VIDA_INICIAL_PIKACHU)
barra_squirtle = int(vida_squirtle * TAMANIO_BARRA / VIDA_INICIAL_SQUIRTLE)

print('Pikachu:  [{}{}] ({}/{})'.format('#' * barra_pikachu, " " * (TAMANIO_BARRA - barra_pikachu),
                                       vida_pikachu, VIDA_INICIAL_PIKACHU))

print('Squirtle: [{}{}] ({}/{})'.format('#' * barra_squirtle, " " * (TAMANIO_BARRA - barra_squirtle),
                                       vida_squirtle, VIDA_INICIAL_SQUIRTLE))
input('Enter para continuar...\n')

os.system("cls")


while vida_pikachu > 0 and vida_squirtle > 0:

    print('Turno de Pikachu')
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print('Pikachu ataca con Bola Voltio')
        vida_squirtle -= 10
    else:
        print('Pikachu ataca con Onda Trueno')
        vida_squirtle -= 11

    if vida_pikachu <= 0:
        vida_pikachu = 0
    if vida_squirtle <= 0:
        vida_squirtle = 0

    barra_pikachu = int(vida_pikachu * TAMANIO_BARRA / VIDA_INICIAL_PIKACHU)
    barra_squirtle = int(vida_squirtle * TAMANIO_BARRA / VIDA_INICIAL_SQUIRTLE)

    print('Pikachu:  [{}{}] ({}/{})'.format('#' * barra_pikachu, " " * (TAMANIO_BARRA - barra_pikachu),
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

        print('Pikachu:  [{}{}] ({}/{})'.format('#' * barra_pikachu, " " * (TAMANIO_BARRA - barra_pikachu),
                                                vida_pikachu, VIDA_INICIAL_PIKACHU))

        print('Squirtle: [{}{}] ({}/{})'.format('#' * barra_squirtle, " " * (TAMANIO_BARRA - barra_squirtle),
                                                vida_squirtle, VIDA_INICIAL_SQUIRTLE))
        input('Enter para continuar...\n')
        os.system('cls')

if vida_pikachu > vida_squirtle:
    print('Pikachu gana!!!')
else:
    print("Squirtle gana!!!")



































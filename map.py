import msvcrt
import os
import random

POS_X = 0
POS_Y = 1
NUM_OBJECTS = 11
my_position = [6, 1]

obs = '''\
###########################
####                        
#####################   ####
#####################   ####
###########                                 
####################  ######
################         ##
#######               ######
#############                             
#####################    ###
##################         #
###################      ###
#################                     
###################     ####
############################\
'''
obs = [list(row) for row in obs.split('\n')]
MAP_WIDTH = len(obs[0])
MAP_HEIGHT = len(obs)


endgame = False
tail = []
objects = []
tail_l = 0
while len(objects) < NUM_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]

    if new_position not in objects and new_position != my_position and obs[new_position[POS_Y][position[POS_X]] != '#']:
        objects.append(new_position)

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

            for piece in tail:
                if piece[POS_X] == coordinate_x and piece[POS_Y] == coordinate_y:
                    char = '@'

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char = "@"
                if food:
                    objects.remove(food)

                    while len(objects) < NUM_OBJECTS:
                        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

                        if new_position not in objects and new_position != my_position:
                            objects.append(new_position)

                    tail_l += 1
                if my_position in tail:
                    endgame = True

            if obs[coordinate_y][coordinate_x] == '#':
                char = '#'

            print(' {} '.format(char), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("Puntos: {}".format(tail_l))

    direction = msvcrt.getwch()
    print(direction)

    position = None

    if direction == 'w':
        position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == 'a':
        position = [(my_position[POS_X]-1) % MAP_WIDTH, my_position[POS_Y]]

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
    print('Game Over')
    print('Total de puntos: {}'.format(tail_l))


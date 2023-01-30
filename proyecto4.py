import random
print('Tenemos un numero del 1 al 10, tienes que adivinar cual es')
numU = int(input('Ingresa tu numero: '))
numC = random.randint(1, 10)
if numU >= 1 and numU <= 10:
    if numC == numU:
        print('Felicidades!!! Ganaste!!!')
    else:
        print('Lo siento, perdiste')
        print('El numero era: ', numC)
else:
    print('Tenias que ingresar un numero valido del 1 al 10')

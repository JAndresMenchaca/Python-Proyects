frase = input("Ingresa tu frase:\n")

espacio = " "
coma = ','
punto = '.'

num_espacio = 0
num_coma = 0
num_punto = 0
for caracter in frase:
    if espacio == caracter:
        num_espacio += 1
    elif coma == caracter:
        num_coma += 1
    elif punto == caracter:
        num_punto +=1

print('Resultado:\n'
      'Numero de espacios: {}\n'
      'Numero de comas: {}\n'
      'Numero de puntos: {}'.format(num_espacio, num_coma, num_punto))

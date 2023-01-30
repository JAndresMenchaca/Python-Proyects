import os
import getpass
import re
from random import randrange
from time import sleep
import sqlite3
from pathlib import Path


def crear_nota(resultado):
    name_user = Path.home()  # "59162"  # os.getlogin()

    ruta = "{}/Desktop/".format(name_user)

    a = open(ruta + "READ ME.txt", "w")
    contenido = "Hola " + os.getlogin() + ", como estas??\n"
    a.write(contenido)

    for item in resultado[:10]:
        a.write("He visto que visitaste: {}\n".format(item[0]))

    '''
    with open(ruta+"READ ME.txt", "w") as a:
        a.write("hola")
    '''


def historial(name_user):
    band = False
    while not band:
        try:
            ruta = name_user + "/AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(ruta)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC LIMIT 10")
            # "SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC LIMIT 10"
            urls = cursor.fetchall()
            history = urls
            connection.close()
            print('Hecho')
            return history
            band = True
        except sqlite3.OperationalError:
            print("La base de datos esta bloqueada")
            sleep(3)


def twitter(resultado, name_user):
    visited = []
    for item in resultado:
        # https://pythex.org/
        # https://regexkit.com/python-regex
        mensaje = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if mensaje and mensaje[0] not in ['notifications', 'home']:
            visited.append(mensaje[0])

    with open(name_user + "/Desktop/" + "twitter.txt", "w") as a:
        a.write("Has visitado los perfiles de: {}".format(", ".join(visited)))


def youtube(resultado, name_user):
    visited = []
    for item in resultado:
        mensaje = re.findall("([A-Za-z0-9\sñ]+) - YouTube+$", item[0])
        if mensaje and mensaje[0] not in ['YouTube Premium', 'Premium']:
            visited.append(mensaje[0])

    with open(name_user + "/Desktop/" + "YouTube.txt", "w") as a:
        a.write("Has visitado los canales de: {}".format(", ".join(visited)))


def steam(name_user):
    ruta = "C:\\Program Files (x86)\\Steam\\steamapps\\common"
    games = os.listdir(ruta)
    real_games = []
    not_games = ['Steam Controller Configs', 'Steamworks Shared']
    for game in games:
        if game in not_games:
            pass
        else:
            real_games.append(game)
    with open(name_user + "/Desktop/" + "steam.txt", "w") as a:
        a.write("Hola! Estuviste jugando: {}".format(", ".join(real_games)))


def main():
    name_user = str(Path.home())

    # sleep(randrange(1, 4) * 60 * 60)

    resultado = historial(name_user)
    print(resultado)
    crear_nota(resultado)
    youtube(resultado, name_user)
    twitter(resultado, name_user)
    steam(name_user)


if __name__ == "__main__":
    main()

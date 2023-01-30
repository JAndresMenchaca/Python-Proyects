import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob


def get_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial bloqueado, reintentando en 3 segundos...")
            sleep(3)


def search_videos(history, user_path):
    visited = []
    url = []
    for item in history:
        mensaje = re.findall("([A-Za-z0-9\sñ()-]+) - YouTube+$", item[0])
        if mensaje and mensaje[0] not in ['YouTube Premium', 'Premium']:
            visited.append(mensaje[0])

    with open(user_path + "/Desktop/" + "YouTube.txt", "w") as a:
        a.write("Lista de videos y canales:\n{}".format("\n".join(visited)))


def main():
        user_path = str(Path.home())
        history = get_history(user_path)
        search_videos(history, user_path)


if __name__ == "__main__":
    main()
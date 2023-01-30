import pickle
import random
from requests_html import HTMLSession
from pprint import pprint


def main():
    pokemon_list = pokeload()
    player_profile = get_player_profile(pokemon_list)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
    print("Has perdido")


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]])


def get_pokemon_info(pokemon):
    return "{} | lvl {} | hp {}".format(pokemon["name"],
                                        pokemon["level"],
                                        pokemon["current_health"],
                                        pokemon["base_health"])


def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        print("Elige el POKEMON")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("[{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("A cual eliges???"))]
        except (ValueError, IndexError):
            print("Opcion invalida")


def fight(player_profile, enemy_pokemon):
    print("---NUEVO COMBATE---")
    player_pokemon = choose_pokemon(player_profile)
    print("Contrincantes: {} VS {}".format(get_pokemon_info(player_pokemon),
                                           get_pokemon_info(enemy_pokemon)))

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        player_attack(player_pokemon, enemy_pokemon)
        enemy_attack(enemy_pokemon, player_pokemon)


    print("---FIN DEL COMBATE---")
    input()


def get_player_profile(pokemon_list):
    profile = {
        "player_name": input("Cual es tu nombre???\n"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
                            # for a in range(3):
                            #   profile["pokemon_inventory"].append(random.randint(len(pokemon_list)))
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0

    }
    return profile


def pokeload():

    try:
        with open("pokefile.pkl", "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)

    except FileNotFoundError:
        pokemon_base = datos()
        all_pokemons = []

        for index in range(15):
            pokemon_page = url(index + 1)
            pokemon = get_pokemon(pokemon_base, pokemon_page)
            all_pokemons.append(pokemon)

        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)

    return all_pokemons


def datos():
    pokemon_base = {
        "name": "",
        "current_health": 100,
        "base_health": 100,
        "attacks": None,
        "level": 1,
        "type":None,
        "current_exp": 0
    }
    return pokemon_base


def url(num):
    url = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk={}".format(num)
    session = HTMLSession()
    pokemon_page = session.get(url)
    return pokemon_page


def get_pokemon(pokemon_base, pokemon_page):

    new_pokemon = pokemon_base.copy() # creamos un nuevo diccionario

    new_pokemon["name"] = pokemon_page.html.find('.mini', first=True).text.split('\n')[0] # agregamos un nombre

    new_pokemon["type"] = []
    pokemon_type = \
    pokemon_page.html.find('.pkmain', first=True).find(".bordeambos", first=True).find("img", first=True).attrs['alt']

    new_pokemon["type"].append(pokemon_type)

    new_pokemon["attacks"] = []
    for attack_item in  pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name": attack_item.find("td", first=True).find("a", first=True).text,
            "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
            "min_level": attack_item.find("th", first=True).text,
            "damage": int(attack_item.find("td")[3].text.replace("--", "0")),
        }
        new_pokemon["attacks"].append(attack)

    return new_pokemon


if __name__ == "__main__":
    main()
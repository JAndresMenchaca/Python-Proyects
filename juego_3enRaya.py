import PySimpleGUI as sg


def main():
    b_size, PLAYER_ONE, PLAYER_TWO, flag, current_player, game_end, deck, winner_plays = variantes()
    tablero(b_size)


def variantes():
    b_size = (7, 3)
    PLAYER_ONE = "X"
    PLAYER_TWO = "O"
    flag = False
    current_player = PLAYER_ONE
    game_end = False
    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

    winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    return b_size, PLAYER_ONE, PLAYER_TWO, flag, current_player, game_end, deck, winner_plays


def tablero(b_size):
    layout = [[sg.Button("", key="-0-", size=b_size),
               sg.Button("", key="-1-", size=b_size),
               sg.Button("", key="-2-", size=b_size)],

              [sg.Button("", key="-3-", size=b_size),
               sg.Button("", key="-4-", size=b_size),
               sg.Button("", key="-5-", size=b_size)],

              [sg.Button("", key="-6-", size=b_size),
               sg.Button("", key="-7-", size=b_size),
               sg.Button("", key="-8-", size=b_size)],

              [sg.Button("OK", key="-texto-")],
              [sg.Text("", key="-winner-")]]
    # sg.Text()
    # sg.Input()
    window = sg.Window("Demo", layout)


if __name__ == "__main__":
    main()
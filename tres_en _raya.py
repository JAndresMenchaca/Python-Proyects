import PySimpleGUI as sg

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

while True:
    event, value = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == "-texto-":
        break

    if window.Element(event).ButtonText == "" and game_end == False:
        index = int(event.replace("-", ""))
        deck[index] = current_player
        window.Element(event).Update(text=current_player)

        for winner_play in winner_plays:
            if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
                if deck[winner_play[0]] == PLAYER_ONE:
                    resp = "El jugador 1 ha ganado"
                    print(resp)
                    window.Element("-winner-").Update('{}'.format(resp))
                    game_end = True
                else:
                    resp = "El jugador 2 ha ganado"
                    print(resp)
                    window.Element("-winner-").Update('{}'.format(resp))
                    game_end = True

        if 0 not in deck:
            print("Juego terminado")
            break

        if current_player == PLAYER_ONE:
            current_player = PLAYER_TWO
        else:
            current_player = PLAYER_ONE



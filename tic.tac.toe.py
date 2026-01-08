players = ["x", "o"]
human_player = "x"
ai_player = "o"
player = human_player

game_btns = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]


def next_turn(row, col):
    global player

    if game_btns[row][col]['text'] == "" and check_winner() == False:
        game_btns[row][col]['text'] = player

        if check_winner() == False:
            player = ai_player

        else:
            end_game()


def check_winner():
    for i in range(3):
        if game_btns[i][0]['text'] == game_btns[i][1]['text'] == game_btns[i][2]['text'] != "":
            return True
        if game_btns[0][i]['text'] == game_btns[1][i]['text'] == game_btns[2][i]['text'] != "":
            return True

    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        return True
    if game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        return True

    for r in range(3):
        for c in range(3):
            if game_btns[r][c]['text'] == "":
                return False
    return 'tie'



from tkinter import *

players = ["x", "o"]
human_player = "x"
ai_player = "o"
player = human_player

window = Tk()
window.title("Tic Tac Toe")

game_btns = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]


def next_turn(row, col):
    global player

    if game_btns[row][col]['text'] == "" and check_winner() == False:
        game_btns[row][col]['text'] = player

        if check_winner() == False:
            player = ai_player
            label.config(text="AI turn")

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

def reset_game():
    global player, ai_turn_count
    ai_turn_count = 0
    player = human_player
    label.config(text="Your turn")
    for r in range(3):
        for c in range(3):
            game_btns[r][c].config(text="", bg="#F0F0F0")


label = Label(window, text="Your turn", font=("consolas", 30))
label.pack()

frame = Frame(window)
frame.pack()

for r in range(3):
    for c in range(3):
        game_btns[r][c] = Button(
            frame, text="", font=("consolas", 40),
            width=4, height=1,
            command=lambda r=r, c=c: next_turn(r, c)
        )
        game_btns[r][c].grid(row=r, column=c)


Button(window, text="Restart Round", font=("consolas", 20), command=reset_game).pack()

window.mainloop()

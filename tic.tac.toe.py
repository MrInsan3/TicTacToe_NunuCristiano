from tkinter import *
import random


players = ["x", "o"]
human_player = "x"
ai_player = "o"
player = human_player

window = Tk()
window.title("Tic Tac Toe")

difficulty = StringVar(window)
difficulty.set("random")

scores = {"x": 0, "o": 0, "draw": 0}

game_btns = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

ai_turn_count = 0

def next_turn(row, col):
    global player

    if game_btns[row][col]['text'] == "" and check_winner() == False:
        game_btns[row][col]['text'] = player

        if check_winner() == False:
            player = ai_player
            label.config(text="AI turn")
            window.after(300, ai_move)

        else:
            end_game()

def ai_move():
    global player, ai_turn_count
    ai_turn_count += 1

    if difficulty.get() == "random":
        move = ai_random_move()
    elif difficulty.get() == "best":
        move = ai_best_move()
    else:
        move = ai_best_move() if ai_turn_count % 2 == 0 else ai_random_move()

    if move:
        r, c = move
        game_btns[r][c]['text'] = ai_player

    end_game()

def end_game():
    global player
    result = check_winner()

    if result == False:
        player = human_player
        label.config(text="Your turn")
    else :
        if result == True:
            winner = "o" if player == ai_player else "x"
            scores[winner] += 1
            label.config(text=f"{winner.upper()} wins!")
        else:
            scores["draw"] += 1
            label.config(text="Tie!")

        update_score()

def update_score():
    score_label.config(
        text=f"X: {scores['x']}   O: {scores['o']}   Draws: {scores['draw']}"
    )

def ai_random_move():
    empty = []
    for r in range(3):
        for c in range(3):
            if game_btns[r][c]['text'] == "":
                empty.append((r, c))
    return random.choice(empty) if empty else None        

def check_winner(board=None):

    if board is None:
        board = game_btns

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

def ai_best_move():
    sim_board = [[game_btns[r][c]['text'] for c in range(3)] for r in range(3)]

    best_score = -float('inf')
    best_move = None

    for r in range(3):
        for c in range(3):
            if sim_board[r][c] == "":
                sim_board[r][c] = ai_player
                score = minimax(sim_board, False)
                sim_board[r][c] = ""
                if score > best_score:
                    best_score = score
                    best_move = (r, c)

    return best_move

def minimax(board, is_maximizing):
    result = evaluate_board(board)
    if result is not None:
        return result

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = ai_player
                    score = minimax(board, False)
                    board[r][c] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = human_player
                    score = minimax(board, True)
                    board[r][c] = ""
                    best_score = min(score, best_score)
        return best_score
    
def evaluate_board(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return 1 if board[i][0] == ai_player else -1
        if board[0][i] == board[1][i] == board[2][i] != "":
            return 1 if board[0][i] == ai_player else -1

    if board[0][0] == board[1][1] == board[2][2] != "":
        return 1 if board[0][0] == ai_player else -1
    if board[0][2] == board[1][1] == board[2][0] != "":
        return 1 if board[0][2] == ai_player else -1

    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                return None  
    return 0 
    
label = Label(window, text="Your turn", font=("consolas", 30))
label.pack()

score_label = Label(window, text="X: 0   O: 0   Draws: 0", font=("consolas", 20))
score_label.pack()

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

controls = Frame(window)
controls.pack()

Radiobutton(controls, text="Random", variable=difficulty, value="random").pack(side=LEFT)
Radiobutton(controls, text="Alternate", variable=difficulty, value="alternate").pack(side=LEFT)
Radiobutton(controls, text="Best", variable=difficulty, value="best").pack(side=LEFT)

Button(window, text="Restart Round", font=("consolas", 20), command=reset_game).pack()

window.mainloop()

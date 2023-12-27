import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext


def score_board():
    pass


def entry():
    pass


def player1_start():
    pass


def player2_start():
    pass


def enemy_bot():
    pass


# Using the random library to choose who's gonna start playing
def player_turn():
    coin = random.randint(1, 2)

    if coin == 1:
        player1_start()

    elif coin == 2:
        player2_start()
    else:
        messagebox.showwarning(None, "They're was an error, please restart the game.")


# Configuring window settings
root = tk.Tk()

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", font=('Arial', 20), width=5, height=2, command=lambda r=i, c=j: entry(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

start_button = tk.Button(root, text="START", font=('Arial', 9), width=10, height=2, command=player_turn)
start_button.grid(row=10, column=0)

multiplayer_button = tk.Button(root, text="MULTIPLAYER", font=('Arial', 9), width=11, height=2)
multiplayer_button.grid(row=10, column=1)

bot_button = tk.Button(root, text="BOT", font=('Arial', 9), width=10, height=2)
bot_button.grid(row=10, column=2)

root.title("TIC TAC TOE")
root.geometry("800x500")

# I have no clue what this does... so just leave it here :)
#  ttk.Label(root, text="logs", font=('Arial', 10), background='green', foreground='white').grid(column=10, rows=1)

score = 3
label = tk.Label(root, textvariable=score, font=('Arial', 10))
label.grid(column=4, pady=10, padx=10)
logs = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, font=('Arial', 10))

logs.grid(column=4, pady=10, padx=10)

root.mainloop()

import random
import time
from tkinter import *
from tkinter import messagebox


def start_game():
    start_time = time.time()

    def show_green_screen():
        root.configure(bg="green")
        root.bind("<Button-1>", lambda event, start_time=start_time: check_reaction_time(start_time))
    global randInt 
    randInt = random.randint(1000, 7000)
    root.after(randInt, show_green_screen)  # Random delay between 1 to 5 seconds

def check_reaction_time(start_time):
    end_time = time.time()
    reaction_time = ((end_time - start_time) * 1000) - randInt  # Convert to milliseconds
    messagebox.showinfo(title="Reaction Time", message=f"Your reaction time: {reaction_time:.3f} ms")
    root.configure(bg="black")
    root.unbind("<Button-1>")


def toggle_full_screen():
    if root.attributes("-fullscreen"):
        root.attributes("-fullscreen", True)
    else:
        root.attributes("-fullscreen", False)

def exit_program():
    root.destroy()

root = Tk()
root.title("ReactionTime")
root.geometry('800x600')
root.configure(bg="black")

startBtn = Button(root, text="Start", bg="white", fg="black", command=start_game)
startBtn.grid(column=2, row=2)

fullScreenBtn = Button(root, text="Toggle Fullscreen", bg="white", fg="black", command=toggle_full_screen)
fullScreenBtn.grid(column=4, row=2)

exitBtn = Button(root, text="Exit", bg="white", fg="black", command=exit_program)
exitBtn.grid(column=8, row=2) 

root.mainloop()

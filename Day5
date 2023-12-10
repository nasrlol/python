#Measuring reaction time

import random
from tkinter import *

def measuringTime():
    while True:
        time_interval = random.randint(1, 7) * 1000
        root.after(time_interval)
        greenScreen()

def greenScreen():
    root.configure(bg="green")
    time_interval = random.randint(1, 5) * 1000
    root.after(time_interval, lambda: root.configure(bg = "black"))
    measuringTime()


def fullScreen():
    root.attributes("-fullscreen", True)

def smallScreen():
    root.attributes("-fullscreen", False)
    
def exitPrgrm():
    exit()

root = Tk()
root.title("ReactionTime")
root.geometry('800x600')
root.configure(bg="black")

startBtn = Button(root, text="start", bg = "white", fg = "black", command = measuringTime)
startBtn.grid(column=2, row=2)

fullScreenBtn = Button(root, text="Fullscreen", bg = "white", fg = "black", command = fullScreen)
fullScreenBtn.grid(column=4, row=2)

smallScreenBtn = Button(root, text="Smallscreen", bg = "white", fg = "black", command = smallScreen)
smallScreenBtn.grid(column=6, row=2)

exitBtn = Button(root, text="exit", bg = "white", fg = "black", command = exitPrgrm)
exitBtn.grid(column=8, row=2) 

root.mainloop()


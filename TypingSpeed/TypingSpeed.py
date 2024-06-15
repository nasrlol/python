import pandas as pd
from tkinter import *

# assigning the images a variable
base_path = r'C:\Users\nasr\Documents\GitHub\python\TypingSpeed\\'

a_path = base_path + r'A.PNG'
b_path = base_path + r'B.PNG'
c_path = base_path + r'C.PNG'
d_path = base_path + r'D.PNG'
e_path = base_path + r'E.PNG'
f_path = base_path + r'F.PNG'
g_path = base_path + r'G.PNG'
h_path = base_path + r'H.PNG'
i_path = base_path + r'I.PNG'
j_path = base_path + r'J.PNG'
k_path = base_path + r'K.PNG'
l_path = base_path + r'L.PNG'
m_path = base_path + r'M.PNG'
n_path = base_path + r'N.PNG'
o_path = base_path + r'O.PNG'
p_path = base_path + r'P.PNG'
q_path = base_path + r'Q.PNG'
r_path = base_path + r'R.PNG'
s_path = base_path + r'S.PNG'
t_path = base_path + r'T.PNG'
u_path = base_path + r'U.PNG'
v_path = base_path + r'V.PNG'
w_path = base_path + r'W.PNG'
x_path = base_path + r'X.PNG'
y_path = base_path + r'Y.PNG'
z_path = base_path + r'Z.PNG'

# letter assignment 

lett_as = {
    "a": a_path,
    "b": b_path,
    "c": c_path,
    "d": d_path,
    "e": e_path,
    "f": f_path,
    "g": g_path,
    "h": h_path,
    "i": i_path,
    "j": j_path,
    "k": k_path,
    "l": l_path,
    "m": m_path,
    "n": n_path,
    "o": o_path,
    "p": p_path,
    "q": q_path,
    "r": r_path,
    "s": s_path,
    "t": t_path,
    "u": u_path,
    "v": v_path,
    "w": w_path,
    "x": x_path,
    "y": y_path,
    "z": z_path
              
}

# choosing the word from words(the word list) and extracting the letters
def select_word():
    list = pd.read_csv(r'C:\Users\nasr\Documents\GitHub\python\TypingSpeed\words.csv', encoding='utf8')
    word = list['Word']
    chosen_word = word.sample().iloc[0]

# configuring the window
root = Tk()

chosen_word = select_word()

canvas  = Canvas(root, width = 900, height = 600)
canvas.pack()


for letter in chosen_word:
        img_path = lett_as.get(letter.lower())
        if img_path:
            img = PhotoImage(file=img_path)
            canvas.create_image(20,20, anchor=NW, image=img)

root.mainloop()



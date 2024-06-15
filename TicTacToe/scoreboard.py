import tkinter as tk

class scoreboard:
   def __init__(self,score_player1,score_player2):

       self.score_player1 = score_player1
       self.score_player2 = score_player2
       
   def display_score(self,score): 
        return score
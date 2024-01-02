import random

def UserInput():
    return input().lower()

def game(userC, computerC):
    won = "Well played! You won..."
    lost = "Unlucky! You lost..."
    
    if (userC == "paper" and computerC == "rock") or \
       (userC == "scissors" and computerC == "paper") or \
       (userC == "rock" and computerC == "scissors"):
        print(computerC.upper())
        print(won)
    elif (userC == "rock" and computerC == "paper") or \
         (userC == "paper" and computerC == "scissors") or \
         (userC == "scissors" and computerC == "rock"):
        print(computerC.upper())
        print(lost)
    elif userC == computerC:
        print(computerC.upper())
        print("It's a tie! Let's go again")

# Welcoming User
print("Welcome to my rock paper scissors game!")
print("Choose between rock, paper, and scissors.")
print("If you want to exit, type 'done' or close the game by pressing the X button.")

while True:  # Loop indefinitely until a break condition is met
    userC = UserInput()  # Get user input
    
    if userC == "done":
        break  # Exit the loop if "done" is entered
    
    if userC not in {"rock", "paper", "scissors"}:
        print("Invalid input. Please choose between rock, paper, and scissors.")
        continue  # Go back to the start of the loop if input is invalid
    
    choice = {"rock", "paper", "scissors"}
    computerC = random.choice(list(choice))
    game(userC, computerC)

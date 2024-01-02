#dice game
import random

def user_input():
    global user_command
    user_command = input().lower()
    return user_command

def game():
    user_input()
    while user_command != "exit":
        if user_command == "roll":
            dice_roll = random.randint(1, 6)
            print(f"You rolled a {dice_roll}")
        elif user_command != "exit" or user_command != "roll":
            print("Invalid input!")
        user_input()
        
    else: exit()
    

print("Type 'roll' if you want to roll the dice!")
print("Type 'exit' if you want to exit")
game()





    

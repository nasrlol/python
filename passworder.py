import random

password = ""

print("How many signs do you need the password to be?")
password_size = input()

try:
    password_size = int(password_size)
except ValueError:
    print("Invalid input type")
    exit()

numbers = "1234567890"
letters = "azertyuiopqsdfghjklmwxcvbn"
signs_string = "&é(-è_çà=+°)@^`|[{#~¹}]"

print("press 1 if you want your password to only contain letters")
print("press 2 if you want your password to only contain signs")
print("press 3 if you want your password to only contain numbers")
print("press 4 if you want your password to only contain letters and numbers")
print("press 5 if you want your password to only contain letters and signs")
print("press 6 if you want your password to only contain numbers and signs")

combination = input()
new_password = password 

if combination == '1':
    for i in range(password_size):
        new_password += random.choice(letters)
elif combination == '2':
    for i in range(password_size):
        new_password += random.choice(signs_string)
elif combination == '3':
    for i in range(password_size):
        new_password += random.choice(numbers)
elif combination == '4':
    for i in range(password_size):
        new_password += random.choice(letters + numbers)
elif combination == '5':
    for i in range(password_size):
        new_password += random.choice(letters + signs_string)
elif combination == '6':
    for i in range(password_size):
        new_password += random.choice(numbers + signs_string)
else:
    print("Invalid combination choice")
    exit()

print("Generated password:", new_password)




import random
print("Welcome to the Rock-Paper-Scissors Game!")
user = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors\n"))
R = """   _______
---' ____)
     (_____)
     (_____)
     (____)
---.__(___)
"""
P = """   _______
---' ____)____
         ______)
         _______)
        _______)
---.__________)
"""
S = """   _______
---' ____)____
         ______)
      __________)
     (____)
---.__(___)
"""
game_menu = [R, P, S]

user_choice = game_menu[user]
print(user_choice)

computer_choice = game_menu[random.randint(0, 2)]
print(f"Computer choose:\n {computer_choice}")

if user_choice == computer_choice:
    result = "draw"
elif user_choice == P:
    if computer_choice == R:
        result = "win"
    else:
        result = "lose"
elif user == R:
    if computer_choice == P:
        result = "lose"
    else:
        result = "win"
else:
    if computer_choice == P:
        result = "win"
    else:
        result = "loose"
        
print(f"You {result}!")


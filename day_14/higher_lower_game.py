import random
from higher_lower_game_art import logo, vs
import os

from higher_lower_game_data import data


def fetch_individual():
    "Fetches individuals to be compared from the game_data"
    individual = random.choice(data)
    return individual
def check_answer(user_choice, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if user_choice == 'A' and a_followers > b_followers:
        return True
    elif user_choice == 'B' and b_followers > a_followers:
        return True
    else:
        return False
    
def clear():
    os.system('cls')

print(logo)
score = 0
game_should_continue = True

individual_a = fetch_individual()
individual_b = fetch_individual()

while game_should_continue == True:
    #print A and B
    print(f"Compare A: {individual_a['name']}, a {individual_a['description']}, from {individual_a['country']}.")
    print(vs)
    print(f"Against B: {individual_b['name']}, a {individual_b['description']}, from {individual_b['country']}.")   
    #Prompt the user to pick who has more followers
    user_choice = input("Who has more followers? 'A' or 'B': ")
    #Check the answer
    a_followers = individual_a['follower_count']
    b_followers = individual_b['follower_count']

    result = check_answer(user_choice, a_followers, b_followers)
    clear()

    if result:
        score += 1
        print(logo)
        print(f"You got it right! Current score: {score}.")
        individual_a = individual_b
        individual_b = fetch_individual()
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
    
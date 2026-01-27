import random
import os
from blackjack_art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare(user_score, computer_score):
    if computer_score == user_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You win"
    elif user_score == 0:
        return "You lose"
    elif user_score > 21:
        return "You lose"
    elif computer_score > 21:
        return "You win"
    elif user_score > computer_score:
        return "You win"
    elif computer_score > user_score:
        return "You lose"
    
def game_block():
    print(logo)
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_ends = False
    while game_ends == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_ends = True
        
        if game_ends == False:
            print(f"Your cards: {user_cards}, final score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == 'y':
                user_cards.append(deal_card())
                if computer_score < 17 and computer_score != 0:
                    computer_cards.append(deal_card())
            if draw_card == 'n':
                game_ends = True
        

        if game_ends == True:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            print(compare(user_score, computer_score))
        
        

restart_game = True
while restart_game == True:
    game_block()
    restart_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if restart_game == 'y':
        os.system('cls')
        restart_game = True
    else:
        restart_game = False
    
import os

from art import logo

print(logo)
print("Welcome to the Auction Bid App")

winner = ""
isUser = True
highestBid = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bid_process():
    global individuals
    name = input("What's your name?: ")
    bid = int(input("What's your bid price? $ "))
    individuals = {
        name: bid
    }
    

while isUser == True:
    bid_process()
    user = input("Is there any other users who want to bid? 'yes' or 'no' ")
    if user == "yes":
        isUser = True
        clear()
    elif user == "no":
        for individual in individuals:
            if individuals[individual] > highestBid:
                winner = individual
                highestBid = individuals[individual]
                print(f"The winner is {winner} with a bid of ${highestBid}")
        isUser = False

import random
from guess_number_art import logo
print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(number)
difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5

for i in range(0, attempt):
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempt -= 1
    if guess > number:
        print("Too high.\nGuess again.")
    elif attempt == 0:
        print("You've run out of guesses. You lose")
        break
    elif guess < number:
        print("Too low.\nGuess again.")
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        break
    
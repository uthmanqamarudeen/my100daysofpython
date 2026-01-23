import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"The chosen word is {chosen_word}")

# chosen_word_split = list(chosen_word)
#Not necessary to convert it to list
display = []
for letter in chosen_word:
    display += "_"
print (display)

check = ""


while not check:
    guess = input("Guess a letter:").lower()
    display_char = -1
    for letter in chosen_word:
        display_char += 1
        if guess == letter:
            display[display_char] = guess
    if all(letter in chosen_word for letter in display):
        check = True
        print(display)
        print("You win")
        break
        
    
    print(display)
    
#if check == True:
 #   print("You win!")


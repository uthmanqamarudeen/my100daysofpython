print("Welcome to the Love Calculator!")
name1 = input("What's your name? \n")
name2 = input("What's their name? \n")
name1_as_lower = name1.lower()
name2_as_lower = name2.lower()
name_together = f"{name1_as_lower}{name2_as_lower}"
first_digit =  name_together.count("t") + name_together.count("r") + name_together.count("u") +name_together.count("e")
last_digit =  name_together.count("l") + name_together.count("o") + name_together.count("v") +name_together.count("e")
score = int(f"{first_digit}{last_digit}")
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50 :
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
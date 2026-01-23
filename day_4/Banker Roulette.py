import random
names_string = input("Give me everybody's names, separated by a comma.\n")

names = names_string.split(", ")
names_count = names_string.count(",")
print(names[random.randint(0,names_count)], "is going to pay the bill today!")
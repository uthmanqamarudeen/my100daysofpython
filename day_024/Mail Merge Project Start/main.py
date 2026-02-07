with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    correspondents = invited_names.readlines()

for correspondent in correspondents:
    correct_correspondent = correspondent.strip()
    correct_letter = letter.replace("[name]", correct_correspondent)
    with open(f"./Output/ReadyToSend/letter_for_{correct_correspondent}.txt", mode="w") as invitation_letter:
        invitation_letter.write(correct_letter)

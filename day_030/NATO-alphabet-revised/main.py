import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}

def answer():
    word = input("What's the word: ").upper()
    try:
        result = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please!")
        answer()
    else:
        print(result)


answer()



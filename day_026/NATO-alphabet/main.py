import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}

word = input("What's the word: ").upper()

result = [alphabet_dict[letter] for letter in word]

print(result)
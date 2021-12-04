import pandas

nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')

# 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
alphabet = {row.letter:row.code for (index, row) in nato_df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
valid_word = False
while not valid_word:
    try:
        word = input("Enter a word: ")
        coded_word = [alphabet[letter.upper()] for letter in word]
        valid_word = True
        print(coded_word)
    except KeyError:
        print("Sorry, only letters of the English alphabet please.")

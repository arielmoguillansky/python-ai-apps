import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
def word_to_nato(word):
    upper_word = word.upper()
    return [nato_dict[letter] for letter in upper_word if letter.upper() in nato_dict]

txt_input = input('Enter a word: ')
print(word_to_nato(txt_input))
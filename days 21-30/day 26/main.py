
#TODO 1. Create a dictionary in this format:

import pandas
nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_word_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_code = input('Write it down: ')
print([nato_word_dict[letter] for letter in input_code.upper()])

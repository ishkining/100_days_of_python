# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.


random_index = random.randint(0, len(word_list) - 1)
chosen_word = word_list[random_index]

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input('Try to guess:\n').lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for character in chosen_word:
    if guess == character:
        print('True')
    else:
        print('False')

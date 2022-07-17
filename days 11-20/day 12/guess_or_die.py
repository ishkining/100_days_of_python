# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from library import choose_difficulty
import random

print(logo)
print('Welcome to the game Guess or Die!')
print('I\'m thinking of a number between 1 and 100')
accessible_attempts = choose_difficulty()
answer = random.randint(1, 100)
is_game_on = True
while is_game_on:
    print(f'You have attempts {accessible_attempts}')
    our_guess = int(input('Type a guess: \n'))
    accessible_attempts -= 1
    if our_guess == answer:
        print('You win')
        is_game_on = False
    elif accessible_attempts == 0:
        print('You lose')
        is_game_on = False
    elif our_guess > answer:
        print('Too high')
        print('Guess again.')
    elif our_guess < answer:
        print('Too low')
        print('Guess again.')

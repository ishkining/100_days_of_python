from art import logo, vs
from game_data import data
import random

score = 0
is_game_on = True

while is_game_on:
    print(logo)

    choice_A = random.choice(data)
    print(
        f'Compare A: {choice_A["name"]}, a {choice_A["description"]}, from {choice_A["country"]}')

    print(vs)

    choice_B = random.choice(data)
    print(
        f'Compare B: {choice_B["name"]}, a {choice_B["description"]}, from {choice_B["country"]}')

    your_choice = input('Who has more followers? Type A or B:\n')

    if (your_choice == 'A' and choice_A["follower_count"] > choice_B["follower_count"]) or (your_choice == 'B' and choice_B["follower_count"] > choice_A["follower_count"]):
        print("Nice")
        score += 1
    else:
        is_game_on = False
        print(f'Your score is {score}')

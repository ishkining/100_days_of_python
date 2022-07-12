import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

my_choice = int(
    input('What do u choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

opponent_choice = random.randint(0, 2)

if my_choice == opponent_choice:
    print('Draw')
elif (my_choice == 0 and opponent_choice == 2) or (my_choice == 1 and opponent_choice == 0) or (my_choice == 2 and opponent_choice == 1):
    print('Win')
else:
    print('Lose')

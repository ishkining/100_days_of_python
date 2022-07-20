from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make ur bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for iterator in range(len(colors)):
    turtles.append(Turtle())
    turtles[iterator].shape('turtle')
    turtles[iterator].color(colors[iterator])
    turtles[iterator].up()
    turtles[iterator].goto(-230, -80 + (iterator * 30))

are_none_reached = True
list_of_turtles_gone = [0 for _ in range(len(turtles))]
while are_none_reached:
    for iterator in range(len(turtles)):
        random_move = random.randint(0, 5)
        list_of_turtles_gone[iterator] += random_move
        turtles[iterator].forward(random_move)
        if list_of_turtles_gone[iterator] >= 475:
            are_none_reached = False
            if colors[iterator] == user_bet:
                print(f'You were right with {colors[iterator]}')
            else:
                print(f'You were wrong, the winner is {colors[iterator]}')
            break

screen.exitonclick()
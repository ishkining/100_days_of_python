def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    else:
        turn_left()
    while front_is_clear() and wall_on_right():
        move()

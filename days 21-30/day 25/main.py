import turtle
import pandas

screen = turtle.Screen()
screen.title('US STATES GAME')
screen.addshape('blank_states_img.gif')
screen.setup(width=700, height=500)
turtle.shape('blank_states_img.gif')

us_states_data = pandas.read_csv('50_states.csv')

text_drawer_of_states = turtle.Turtle()
text_drawer_of_states.up()
text_drawer_of_states.hideturtle()

is_game_on = True
score = 0
# TODO: 5: Track correct guesses
guessed_states = []

# TODO: 4: Use loop for keep answering
while is_game_on:

    if score == len(us_states_data.state):
        is_game_on = False

    # TODO: 1: Convert guess to title case
    answer_state = screen.textinput(title=f'{score}/{len(us_states_data.state)} correct states'
                                    , prompt='Whats another state\'s name?')
    if answer_state == 'exit':
        missed_states = [state for state in us_states_data.state.to_list() if state not in guessed_states]
        pandas.DataFrame(missed_states).to_csv('missed_states.csv')
        break
    # TODO: 2: Check if the guess is among 50 states
    if not us_states_data[us_states_data.state == answer_state.title()].empty \
            and answer_state.title() not in guessed_states:
        # TODO: 3: Write correct state in map
        x = int(us_states_data[us_states_data.state == answer_state.title()].x)
        y = int(us_states_data[us_states_data.state == answer_state.title()].y)
        text_drawer_of_states.goto(x, y)
        text_drawer_of_states.write(answer_state.title())
        guessed_states.append(answer_state.title())
        # TODO: 6: Track score
        score += 1






screen.exitonclick()
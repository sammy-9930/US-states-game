import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
guessed_state = []
data = pandas.read_csv('50_states.csv')

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 States correct',
                                    prompt="What's another state name").title()

    all_states = data.state.to_list()

    if answer_state == "Exit":
        # save the states that user has not guessed into a csv file
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


# for state in data.state:
#     if state == answer_state:
#         new_turtle = turtle.Turtle()
#         new_turtle.color('red')
#         new_turtle.hideturtle()
#         x_pos = int(data[data['state'] == answer_state].x)
#         y_pos = int(data[data['state'] == answer_state].y)
#         new_turtle.penup()
#         new_turtle.goto(x_pos, y_pos)
#         new_turtle.write(answer_state, align='center')






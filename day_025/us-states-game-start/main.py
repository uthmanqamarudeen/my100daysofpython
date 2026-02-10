import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

prompt_title = "Guess the state"
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(prompt_title, "What's another state's name?").title()

    if answer_state == "Exit":
        states_to_learn = []
        for state in states_list:
            if state not in correct_guesses:
                states_to_learn.append(state)
        states_to_learn_file = pandas.DataFrame(states_to_learn)
        states_to_learn_file.to_csv("states_to_learn.csv")
        break

    elif answer_state in states_list and answer_state not in correct_guesses:
        answer_state_row = data[data.state == answer_state]
        x_cor = answer_state_row.x.item()
        y_cor = answer_state_row.y.item()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x_cor, y_cor)
        turtle.write(answer_state, align="center")
        correct_guesses.append(answer_state)
        prompt_title = f"{len(correct_guesses)}/50 States Correct"





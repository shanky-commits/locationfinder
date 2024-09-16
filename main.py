import turtle
from turtle import Screen
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states=data.state.to_list()

# def get_mouse_click_coor(x,y):
#     print(x,y)
# for finding coardinates
Guessed_states = []

while len(Guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(Guessed_states)}/ 50 States Correct",
                                    prompt="what's the another state's name").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in Guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")

        break
    if answer_state in all_states:
        Guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)




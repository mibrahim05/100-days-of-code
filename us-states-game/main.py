import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")


image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
all_states = data["state"].tolist()
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",prompt="What's the another state's name").title()


    if answer_state == "Exit".title():
        missing_state = [state for state in all_states if state not in guessed_state]
    #     missing_state =[]
    #     for state in all_states:
    #         if state not in guessed_state:
    #             missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data["state"] == answer_state]
        tim.goto(state_data.x.item(),state_data.y.item())
        tim.write(answer_state)



# guessed_state = pd.DataFrame
# guessed_state.to_csv("states_to_learn.csv")


# if answer_state ==
# print(answer_state)




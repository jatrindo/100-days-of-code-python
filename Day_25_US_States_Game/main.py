import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Set up turtle that will write the states' names
t = turtle.Turtle()
t.penup()
t.hideturtle()

# Read in the states data
state_df = pandas.read_csv('50_states.csv')
states = state_df.state.to_list()

# 5. Record the correct guesses in a list
guessed_states = []

# 4. Use a loop to allow the user to keep guessing (user can end the game by
#   clicking 'Cancel')
title = "Guess the state"
while len(guessed_states) < len(state_df):
    # 1. Convert the guess to Title case
    response = screen.textinput(title=title, prompt="What's another state's name?")

    if response is None or response == "Exit":
        break

    response = response.title()

    # 2. Check if the guess is among the 50 states
    if response not in guessed_states and response in states:
        state_row = state_df[state_df['state'] == response]

        # 3. Write correct guesses onto the map
        x = int(state_row.x)
        y = int(state_row.y)
        t.goto(x, y)
        t.write(response, align='center')

        guessed_states.append(response)

    # 6. Keep track of the score (which are the number of states guessed)
    title = f"{len(guessed_states)}/{len(state_df)} States Correct"

# Write out states missed for further review
if len(guessed_states) < len(states):
    states_to_learn = [state for state in states if (state not in guessed_states)]

    df = pandas.DataFrame({
        'states': states_to_learn
    })

    df.to_csv('states_to_learn.csv')

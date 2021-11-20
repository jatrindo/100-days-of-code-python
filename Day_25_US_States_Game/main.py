import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)

# TODO: 1. Convert the guess to Title case
# TODO: 2. Check if the guess is among the 50 states
# TODO: 3. Write correct guesses onto the map
# TODO: 4. Use a loop to allow the user to keep guessing
# TODO: 5. Record the correct guesses in a list
# TODO: 6. Keep track of the score

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Keep track of the score
score = 0
guess_list = []
# Use a loop to allow the user to keep guessing
while score < 50:
    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="What's another state's name?")
    # Convert the guess to Title case
    answer_state = answer_state.title()
    List = pandas.read_csv("50_states.csv")
    # Check if the guess is among the 50 states
    row = List.loc[List['state'] == answer_state]
    if answer_state not in guess_list:
        # Write correct guesses onto the map
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        if not row.empty:
            marker.goto(row.at[row.index[0], 'x'], row.at[row.index[0], 'y'])
            marker.write(f"{answer_state}", move=False, align='center', font=('Arial', 7, 'normal'))
            # Record the correct guesses in a list
            guess_list.append(answer_state)
            score += 1
        else:
            print("Try again!")

print(f"Your guesses were {guess_list}")
turtle.mainloop()

screen.exitonclick()

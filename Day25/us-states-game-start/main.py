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
    if answer_state == "Exit":
        break
    if answer_state not in guess_list:
        # Write correct guesses onto the map
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        if not row.empty:
            marker.goto(row.at[row.index[0], 'x'], row.at[row.index[0], 'y'])
            marker.write(f"{answer_state}", move=False, align='left', font=('Arial', 5, 'normal'))
            # Record the correct guesses in a list
            guess_list.append(answer_state)
            score += 1
        else:
            print("Try again!")

# Generate CSV file containing missing states from guesses
if score < 50:
    print(f"Your guesses were {guess_list}. Check missing_states.csv to see the states that you missed out on")
    missing_states = [state for state in List['state'] if state not in guess_list]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv('missing_states.csv', index=False, sep=',', mode='w')
else:
    print("Congratulations! You correctly guessed all 50 states!")

import turtle
import pandas
import time

# game screen
screen = turtle.Screen()
screen.title("Romania County Game")
# map image
image = "Romania-districts_map.gif"
screen.addshape(image)
turtle.shape(image)
# turtle for the timer
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
# turtle for displaying the high score
high_score_turtle = turtle.Turtle()
high_score_turtle.hideturtle()
high_score_turtle.penup()
# turtle for writing district names
district_turtle = turtle.Turtle()
district_turtle.hideturtle()
district_turtle.penup()
district_turtle.color("blue")
district_turtle.fontsize = 15

start_time = time.time()
game_active = True  # game is running
guessed_states = []  # store correctly guessed districts

# read previous best times from the file
try:
    with open("lowest_times.txt", "r") as file:
        times = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    times = []

# display the high score if previous times exist
if times:
    lowest_time = min(times)
    high_score_turtle.goto(50, screen.window_height() / 2 - 30)
    high_score_turtle.write(f"High Score: {lowest_time}", align="right", font=("Arial", 16, "normal"))


def update_timer():
    """Updates the timer every second while the game is active."""
    if not game_active:
        return  # stop at game end

    # calculate elapsed time
    time_passed = int(time.time() - start_time)
    minutes_passed = time_passed // 60
    seconds_passed = time_passed % 60

    # format the time as MM:SS
    time_format = f"{minutes_passed}:{seconds_passed:02d}"

    # display the updated time
    timer_turtle.clear()
    timer_turtle.goto(screen.window_width() / 2 - 30, screen.window_height() / 2 - 30)
    timer_turtle.write(f"Time: {time_format}", align="right", font=("Arial", 16, "normal"))

    # schedule the next timer update (only if the game is still running)
    if game_active:
        screen.ontimer(update_timer, 1000)


def exit_game():
    global game_active
    game_active = False

    # Calculate final time before closing
    stop_time = time.time()
    count_time = stop_time - start_time
    min_passed = int(count_time // 60)
    sec_passed = int(count_time % 60)
    f_time = f"{min_passed}:{sec_passed:02d}"

    # Display final time
    timer_turtle.clear()
    timer_turtle.goto(screen.window_width() / 2 - 30, screen.window_height() / 2 - 30)
    timer_turtle.write(f"Final Time: {f_time}", align="right", font=("Arial", 16, "normal"))

    # Close the window
    screen.bye()


update_timer()

# load data from CSV
data = pandas.read_csv("counties.csv")
all_states = data.state.to_list()

# keep asking for district names until 41 are guessed or user exits
while len(guessed_states) < 41 and game_active:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/41 Districts",
                                    prompt="What's the District name?")

    if answer_state is None:
        exit_game()
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        exit_game()
        break

    # check if the answer is correct and not previously guessed
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # get the x, y coordinates for the district
        state_data = data[data.state == answer_state]
        x_coord, y_coord = int(state_data.x.iloc[0]), int(state_data.y.iloc[0])

        # move the turtle to the district and write its name
        district_turtle.goto(x_coord, y_coord)
        district_turtle.write(answer_state, align="center", font=("Arial", district_turtle.fontsize, "normal"))

# save the best times only if all districts were guessed
if len(guessed_states) == 41:
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    formatted_time = f"{minutes}:{seconds:02d}"

    with open("lowest_times.txt", "a") as file:
        file.write(formatted_time + "\n")

# only call mainloop if the game is still active
if game_active:
    turtle.mainloop()

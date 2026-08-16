# TURTLE RACE

# import what we need
import random
import os
from turtle import Screen
import turtle as t

# create new screen object
screen = Screen()

# set initial screen size
    # DONT include the other two fields
    # start_x and start_y or else screen won't open up in center of your screen
screen.setup(width=900, height=800)
screen.title("Welcome to the Turtle Race!")

# ask user who will win the race
who_will_win = screen.textinput("Place Your Best!", "Who will win the race? Enter a color of kayla, david, eric, josh, steven, ming)")

while who_will_win not in ("kayla", "david", "eric", "josh", "steven", "ming"):
    who_will_win = screen.textinput("Incorrect Section", "Who will win the race? Enter a color of kayla, david, eric, josh, steven, ming)")

# 1. Store the colors in a list
colors = ["kayla", "david", "eric", "josh", "steven", "ming"]
# 2. Store speeds in a list
speeds = [1, 3, 5, 7, 9, 0]
# 3. Save turtle racers for later
turtle_racers = []
# 4. set x,y  positions
start_x = -425
start_y = -125
# 5. movement forward amounts
forward_movement = [5, 10, 15, 20, 25, 30]
# 6. wait for count to equal len(colors) and start race
count = 0

# 7. face images to use for each racer, matched up with the colors list above
    # each color gets its own face image
    # these .gif files need to live in the same folder as this script
image_dir = os.path.dirname(os.path.abspath(__file__))
face_images = {
    "kayla": "kayla.gif",
    "david": "david.gif",
    "eric": "eric.gif",
    "josh": "josh.gif",
    "steven": "steven.gif",
    "ming": "ming.gif",
}

# register every face image as a turtle shape before it's used
for color, filename in face_images.items():
    image_path = os.path.join(image_dir, filename)
    screen.register_shape(image_path)

for index in range(len(colors)):

    # create new turtle object
    new_turtle = t.Turtle()
    # setting shape, colors, speed, NO PEN
    new_turtle.penup()

    # use the registered face image as this turtle's shape instead of the default turtle shape
    face_shape = os.path.join(image_dir, face_images[colors[index]])
    new_turtle.shape(face_shape)

    # now that .color() is no longer set to a color name, we can't rely on
    # turtle.color()[0] to tell racers apart anymore. Instead, tag each
    # turtle with its own custom .racer_name attribute we can check later.
    new_turtle.racer_name = colors[index]

    new_turtle.speed(3)

    # setting position of turtles on x axis one above the other by 50 paces
    new_turtle.setposition(start_x, start_y + (index * 50))

    # increment count each time a turtle makes it to the starting line
    count = count + 1

    # add turtles that are ready to race to their own list
    turtle_racers.append(new_turtle)

# ready to start race when
    # count of turtles at starting line match all turtles that are expected to race
if count == len(colors):

    # start racing
    racing = True

    while racing:

        for turtle in turtle_racers:
            turtle.speed(random.choice(speeds))  # give each turtle a random speed
            turtle.forward(random.choice(forward_movement))  # give each turtle a random forward amount

            # find the finish line
                # grab the x coordinate of position and
                # check if the turtle reaches x coordinate finish line
                    # pos()[0] or pos()[1] gives x or y coordinate
                    # xcor() gives x coordinate
                    # ycor() gives y coordinate
            if turtle.xcor() > 430:
                winning_turtle = turtle.racer_name  # grab name of winning turtle
                print(f"As they come down the home stretch the winning turtle is {winning_turtle}")
                racing = False  # stop racing as we have a winner

                # print out the winning or lose message based on who_will_win input above
                if who_will_win == winning_turtle:
                    print(f"Your Turtle WON! The winning turtle was {who_will_win}")
                else:
                    print(f"Your Turtle LOST! You bet the {who_will_win} turtle would win "
                          f"but the {winning_turtle} turtle won")

                break  # stop racing

# exit screen when clicked
screen.exitonclick()
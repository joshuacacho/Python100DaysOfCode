# TURTLE RACE

# import what we need
import random
from turtle import Screen
import turtle as t

#create new screen object
screen = Screen()

# set initial screen size
    # DONT include the other two fields
    # start_x and start_y or else screen won't open up in center of your screen
screen.setup (width=500, height=400)
screen.title("Welcome to the Turtle Race!")

# ask user who will win the
who_will_win =  screen.textinput("Place Your Best!", "Who will win the race? Enter a color of red, blue, green, black, brown or coral")

while who_will_win not in ("red","blue","green","black","brown","coral"):
    who_will_win = screen.textinput("Incorrect Section", "Who will win the race? Enter a color of red, blue, green, black, brown or coral")

# 1. Store the colors in a list
colors = ["red","blue","green","black","brown","coral"]
# 2. Store speeds in a list
speeds = [1,3,5,7,9,0]
# 3. Save turtle racers for later
turtle_racers = []
# 4. set x,y  positions
start_x = -225
start_y = -125
# 5. movement forward amounts
forward_movement = [5,10,15,20,25,30]
# 6. wait for count to equal len(colors) and start race
count = 0

for index in range(len(colors)):

    #create new turtle object
    new_turtle = t.Turtle()
    # setting shape, colors, speed, NO PEN
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[index])
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
            turtle.speed(random.choice(speeds)) # give each turtle a random speed
            turtle.forward(random.choice(forward_movement)) # give each turtle a random forward amount

            # find the finish line
                # grab the x coordinate of position and
                # check if the turtle reaches x coordinate finish line
                    # pos()[0] or pos()[1] gives x or y coordinate
                    # xcor() gives x coordinate
                    # ycor() gives y coordinate
            if turtle.xcor() > 225:
                winning_turtle = turtle.color()[0] # grab color of winning turtle
                print(f"As they come down the home stretch the winning turtle is {winning_turtle}")
                racing = False # stop racing as we have a winner

                # print out the winning or lose message based on who_will_win input above
                if who_will_win == winning_turtle:
                    print(f"Your Turtle WON! The winning turtle was {who_will_win}")
                else:
                    print(f"Your Turtle LOST! You bet the {who_will_win} turtle would win "
                          f"but the {winning_turtle} turtle won")

                break # stop racing

else:
    print("ALL USERS DIDNT MAKE IT TO THE STARTING LINE")

# exit screen when clicked
screen.exitonclick()
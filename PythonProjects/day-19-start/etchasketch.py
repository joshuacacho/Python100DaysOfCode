# ETCH A SKETCH GAME
import turtle
# import what we need
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

# Requirements are as follows
    # W to move forwards
    # S to move backwards
    # A to move counter-clockwise
    # D to move clockwise
    # C to clear drawing and start at position 0,0

# get the screen to listen to key strokes
screen.listen()

# move forward
def move_forwards():
    t.forward(10)

# move backwards
def move_backwards():
    t.back(10)

# move counter-clockwise or left
def turn_left():
    t.left(10)

# move clockwise or right
def turn_right():
    t.right(10)

# clear screen
def clear_screen():
    t.reset()
    t.setposition(0,0)

# keyboard strokes
screen.onkey(fun=move_forwards, key = "w")
screen.onkey(fun=move_backwards, key = "s")
screen.onkey(fun=turn_left, key = "a")
screen.onkey(fun=turn_right, key = "d")
screen.onkey(fun=clear_screen, key = "c")


# exit screen
screen.exitonclick()
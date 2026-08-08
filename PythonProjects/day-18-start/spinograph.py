# Creat a spirograph

from turtle import Turtle, Screen # packaged with python standard library
import random
import turtle

timmy_the_turtle = Turtle()

# changes the color mode of the Turtle library to accept RGB values ranging from 0 to 255
# instead of percentages between 0.0 and 1.0
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    my_tuple = [r,g,b]
    return my_tuple

# Figure out how to draw a circle
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(0)

def draw_spirograph(spirograph, title_increment, tilt_heading):
    heading = 0
    for _ in range(spirograph):
        heading = heading + tilt_heading
        timmy_the_turtle.tilt(title_increment)
        timmy_the_turtle.tiltangle()
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(title_increment)
        timmy_the_turtle.setheading(heading + tilt_heading)

draw_spirograph(360, 180,70)

# This is the last thing we will do to close the screen
screen = Screen()
screen.exitonclick()
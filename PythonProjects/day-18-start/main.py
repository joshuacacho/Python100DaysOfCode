from time import time
from turtle import Turtle, Screen # packaged with python standard library
import random
import turtle

timmy_the_turtle = Turtle()

# 1. This line fixes the error!
turtle.colormode(255)

# using rgb colors and then assigning the value to a tuple
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    my_tuple = [r,g,b]
    return my_tuple


# Using the documentation we can do many things
    # Always refer to the documentation

# Set turtle shape to shape with given name or, if name is not given, return name of current shape.
# Shape with name must exist in the TurtleScreen’s shape dictionary.
# Initially there are the following polygon shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(0)


# Drawing the turtle walking schema
track_colors = ["red", "orange","yellow","blue","pink","purple","black","green","coral2","wheat"]
directions = [0,90,180,270]
pen_thickness = [5,10]
forward_movement = [20,30,40]

for _ in range(250):
    timmy_the_turtle.forward(random.choice(forward_movement))
    # using the tuple below instead
    # timmy_the_turtle.color(random.choice(track_colors))
    # using tuple created
    print(random_color())
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.pensize(random.choice(pen_thickness))
    timmy_the_turtle.setheading(random.choice(directions))



# Set turtle color
# https://docs.python.org/3/library/turtle.html#color-control
timmy_the_turtle.color("coral2")


# Move the turtle (current direction and change direction)
# https://docs.python.org/3/library/turtle.html#turtle-motion
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

# Draw a square (continuing from above)
for i in range(3):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

timmy_the_turtle.clear()
# Draw a
# dashed line for 10 paces and
# then a gap of 10 paces and - https://docs.python.org/3/library/turtle.html#turtle.penup
# then a solid line for 10 paces until it does it 50 times - https://docs.python.org/3/library/turtle.html#turtle.pendown
for i in range(10):
    # move forward 10 with solid line
    timmy_the_turtle.forward(10)
    # create the dash where we move forward 10 without drawing
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    # put the pen back down and make a solid  line and move forward 10 with solid line
    timmy_the_turtle.pendown() # put pen back down
    timmy_the_turtle.forward(10)



# Drawing a triangle
    # 360 / 3 sides = 120
timmy_the_turtle.clear()
for _ in range(3):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(120)
    timmy_the_turtle.forward(100)


# Drawing a square
    # 360 / 4 sides = 90
timmy_the_turtle.clear()
for _ in range(2):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


# Drawing a pentagon
    # 360 / 5 sides = 72
timmy_the_turtle.clear()
for _ in range(2):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(72)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(72)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(72)


# Drawing a pentagon
    # 360 / 6 sides = 60
timmy_the_turtle.clear()
for _ in range(2):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(60)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(60)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(60)
    timmy_the_turtle.forward(100)


# Drawing a heptagon
    # 360 / 7 sides = 52
timmy_the_turtle.clear()
for _ in range(2):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(52)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(52)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(52)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(52)

# Drawing a octagon
    # 360 / 8 sides = 45
timmy_the_turtle.clear()
for _ in range(2):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(45)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(45)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(45)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(45)
    timmy_the_turtle.forward(100)

# Drawing a nonagon
    # 360 / 9 sides = 40
timmy_the_turtle.clear()
for _ in range(2):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(40)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(40)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(40)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(40)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(40)

# Drawing a decagon
    # 360 / 10 sides = 36
timmy_the_turtle.clear()
for _ in range(2):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(36)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(36)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(36)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(36)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(36)
    timmy_the_turtle.forward(100)


# now that we know the pattern above we can draw it out
timmy_the_turtle.clear()

colors = ["red", "orange","yellow","blue","pink","purple","black","green","coral2","wheat"]

# draw_shape function that calculates number of sides and tells turtle to move
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(angle)

# for loop to create each shape from 3 (triangle 10 (11 is not inclusive for decagon))
for shape_side_n in range (3,11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)


# This is the last thing we will do to close the screen
screen = Screen()
screen.exitonclick()
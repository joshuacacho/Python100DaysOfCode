# import what we need
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

# getting the screen ready to start listening
screen.listen()

# turtle.onkey(fun, key)
# turtle.onkeyrelease(fun, key)
# Parameters:
    # fun – a function with no arguments or None
    # key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
def move_forwards():
    t.forward(10)

screen.onkey(fun=move_forwards, key="space") #move_forwards is object, NOT move_forwards()

# exit screen on click
screen.exitonclick()
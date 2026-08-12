from turtle import Turtle, Screen
import time

# screen setup
screen = Screen()
screen.tracer(0) # turn tracer off and we will update manually the screen when we want
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")

# turtle setup
snake = Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.shapesize(1,-2)

# consistent forward movement of snake
MOVEMENT = 20

# use keys to be able to move the turtle up, down, left and right
    # in snake we cant allow the snake to trigger either one of the below and RUN INTO ITSELF
        # go backwards once its moved forward
        # go backwards once its moved forward
        # go left once its moved right
        # go right once its moved

def go_up():
    if snake.heading() != 270: # down on y-axis
        snake.setheading(90) # go up on y-axis

def go_down():
    if snake.heading() != 90: # up on y-axis
        snake.setheading(270) # go down on y-axis

def go_left():
    if snake.heading() != 0: # right on x-axis
        snake.setheading(180) # go left on x-axis

def go_right():
    if snake.heading() != 180: # left on x-axis
        snake.setheading(0) # go right on x-axis


# create key pairing for up,down,left and right
screen.listen() # create screen listener for key
screen.onkey(fun=go_up, key="Up")
screen.onkey(fun=go_down, key="Down")
screen.onkey(fun=go_left, key="Left")
screen.onkey(fun=go_right, key="Right")

# start game
game_running = True

while game_running:
    snake.forward(MOVEMENT)
    time.sleep(0.1) #using this to control the speed of the game
    screen.update() # update the screen while the game is running

screen.exitonclick()
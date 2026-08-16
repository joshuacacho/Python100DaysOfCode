from turtle import Turtle, Screen


class Snake:

    def __init__(self, turtle_width, turtle_length):
        self.turtle = Turtle()
        self.screen = Screen()
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.shapesize(turtle_width, turtle_length)
        self.movement = 20

    def snake_default_movement(self):
        """This function moves the snake at game start at intervals of 20 on x-axis"""
        self.turtle.forward(self.movement)

    def go_up(self):
        """This function moves the snake up"""
        if self.turtle.heading() != 270: # down on y-axis
            self.turtle.setheading(90) # go up on y-axis

    def go_down(self):
        """This function moves the snake down"""
        if self.turtle.heading() != 90:  # up on y-axis
            self.turtle.setheading(270)  # go down on y-axis

    def go_left(self):
        """This function moves the snake left"""
        if self.turtle.heading() != 0:  # right on x-axis
            self.turtle.setheading(180)  # go left on x-axis

    def go_right(self):
        """This function moves the snake right"""
        if self.turtle.heading() != 180:  # left on x-axis
            self.turtle.setheading(0)  # go right on x-axis

    def event_listener(self):
        self.screen.listen()

    def key_movement(self):
        # create key pairing for up,down,left and right
        self.screen.onkey(fun=self.go_up, key="Up")
        self.screen.onkey(fun=self.go_down, key="Down")
        self.screen.onkey(fun=self.go_left, key="Left")
        self.screen.onkey(fun=self.go_right, key="Right")




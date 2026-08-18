# The food class for our snake

from turtle import Turtle
import random


# Challenge 1
    # Make the Food class inherit from the Turtle Class
class Food(Turtle):

    def __init__(self):
        super().__init__() # super class is the Turtle class

        # creating our food shape using the Turtle Super Class
        self.shape("circle") # we are using the shape method from Turtle Class
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid= .5) # 10 x 10 circle
        self.speed("fastest")
        self.food_random_position()

    def food_random_position(self):
        """This method updates the location of the food each time
            the snake collides with it """
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)

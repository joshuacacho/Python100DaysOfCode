# the Scoreboard class to update the score each time food is found

# using turtle to create out score board
from turtle import Turtle

# Create variables for self.write
SCORE = "Score: "
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        # creating the necessary scoreboard parameters utilizing the Turtle Class Methods
        self.hideturtle() # hide the arrow
        self.penup()
        self.color("white")
        self.goto(0,280) # location to place the scoreboard
        self.score = 0

        # because have the below in two place it means we need to create something to make this re-useable
        # self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 12, 'normal'))
        self.update_scoreboard()


    def update_scoreboard(self):
        """This method clears current scoreboard and creates initial scoreboard"""
        self.clear()
        self.write(f"{SCORE} {self.score}", move=False, align=ALIGNMENT, font=FONT)

    # increment score each time food is found
    def increment_score(self):
        """This method updates the score, clears previous scoreboard and updates the scoreboard with new score"""
        self.score += 1

        # because have the below in two place it means we need to create something to make this re-useable
        # self.clear()
        # self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 12, 'normal'))

        self.update_scoreboard() # since the score is shared across the entire class it will update
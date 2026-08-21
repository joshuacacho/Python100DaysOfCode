from turtle import Screen, Turtle

class Setup:

    def __init__(self, title):
        self.turtle = Turtle()
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title(title)
        self.screen.tracer(0)


    def update_screen(self):
        """This function updates the screen for rendering since default tracer is disabled"""
        self.screen.update()

    def exit_on_click(self):
        """This function will exit the screen on click"""
        self.screen.exitonclick()





# utilizing Screen class for setup
from screenOOP import Setup
# utilizing Turtle class from
from snakeOOP import Snake
# import time class to use as control speed of game
import time

# create default setup and new turtle
screen = Setup("Snake Game")
snake = Snake(1, -2)

# creating the controls of the game
snake.event_listener()
snake.key_movement()

# start game
game_running = True

while game_running:
    snake.snake_default_movement()
    time.sleep(0.1) #using this to control the speed of the game
    screen.update_screen() # update the screen while the game is running


# exit game on click
screen.exit_on_click()





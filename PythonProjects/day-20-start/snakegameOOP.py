# utilizing Screen class for setup
from screenOOP import Setup
# utilizing Turtle class
from snakeOOP import Snake
# utilizing Turtle Class
from snakefoodOOP import Food
# utilizing Turtle Class
from snakescoreOOP import Scoreboard
# import time class to use as control speed of game
import time

# create default setup and new turtle
screen = Setup("Snake Game")
snake = Snake(1, -2)
food = Food()
score = Scoreboard()


# creating the controls of the game
snake.event_listener()
snake.key_movement()

# start game
game_running = True

while game_running:
    snake.snake_default_movement()
    time.sleep(0.1) #using this to control the speed of the game
    screen.update_screen() # update the screen while the game is running

    # detect collision with food
        # using Turtle method distance is < 15
    if snake.turtle.distance(food) < 15:
        print("collided")

        # update the score

        # Once we collide we want the
            # score to update
                # we will update the score
            # next piece of food to new location
                # we will create new method for this
        score.increment_score()
        food.food_random_position()

# exit game on click
screen.exit_on_click()





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
snake = Snake()
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

    # detect collision with food comparing two turtles movements
        # using Turtle method distance is < 15
    if snake.head.distance(food) < 15: # was snake.turtle.distance(food)
        print("collided")

        # Once we collide we want the
            # score to update
                # we will update the score
            # NEW - extend the snake size anytime we get the food
            # next piece of food to new location
                # we will create new method for this
        score.increment_score()
        snake.extend_snake_size()
        food.food_random_position()

    # detect collision with food comparing two turtles movements
        # if this returns false we will exit the while look
    out_of_bounds = snake.is_out_of_bounds()

    # detect collision with wall
        # is the head of the snake collides with any segment with the rest of our body
    body_collision= snake.snake_body_collision()

    # if out of bounds or body collisions then game over
        # if not true
    if not out_of_bounds or not body_collision:
        game_running = False


# dont end the game until we click otherwise it will close on its own because the while loop will end
screen.screen.exitonclick()

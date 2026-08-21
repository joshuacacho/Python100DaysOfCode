# from turtle import Turtle, Screen
#
# ALIGNMENT = "center"
# FONT = ('Arial', 12, 'normal')
#
# class Snake:
#
#     def __init__(self):
#         self.turtle = Turtle()
#         self.screen = Screen()
#         self.turtle.shape("square")
#         self.turtle.color("white")
#         self.turtle.penup()
#         self.turtle_width = 1
#         self.turtle_length = -2
#         self.turtle.shapesize(self.turtle_width, self.turtle_length)
#         self.movement = 20
#
#     def snake_default_movement(self):
#         """This method moves the snake at game start at intervals of 20 on x-axis"""
#         self.turtle.forward(self.movement)
#
#     def extend_snake_size(self):
#         """This method extends the length of the snake e"""
#         self.turtle_length += -1
#         self.turtle.shapesize(self.turtle_width, self.turtle_length)
#
#
#     def snake_body_collision(self):
#
#         game_running = True
#
#         turtle_head = self.turtle_width # will be 1 always
#         turtle_segment = self.turtle_length # will extend
#
#         if self.turtle.distance(turtle_head, turtle_segment) < 10:
#             print("Tail Collision")
#             game_running = False
#
#         return game_running
#
#     def go_up(self):
#         """This method moves the snake up"""
#         if self.turtle.heading() != 270: # down on y-axis
#             self.turtle.setheading(90) # go up on y-axis
#
#     def go_down(self):
#         """This method moves the snake down"""
#         if self.turtle.heading() != 90:  # up on y-axis
#             self.turtle.setheading(270)  # go down on y-axis
#
#     def go_left(self):
#         """This method moves the snake left"""
#         if self.turtle.heading() != 0:  # right on x-axis
#             self.turtle.setheading(180)  # go left on x-axis
#
#     def go_right(self):
#         """This method moves the snake right"""
#         if self.turtle.heading() != 180:  # left on x-axis
#             self.turtle.setheading(0)  # go right on x-axis
#
#     def event_listener(self):
#         self.screen.listen()
#
#     def key_movement(self):
#         # create key pairing for up,down,left and right
#         self.screen.onkey(fun=self.go_up, key="Up")
#         self.screen.onkey(fun=self.go_down, key="Down")
#         self.screen.onkey(fun=self.go_left, key="Left")
#         self.screen.onkey(fun=self.go_right, key="Right")
#
#     # def screen_width(self):
#     #     self.width = self.screen.window_width()
#     #     return self.width
#     #
#     # def screen_height(self):
#     #     self.height = self.screen.window_height()
#     #     return self.height
#
#     # turtle starts at 0,0 so the full width of the screen is 600
#         # WE COULD DO - so need to do half distance which is (300,0) or / 2
#         # So abs() just means "how far from center, regardless of direction" —
#             # it basically just strips the - from the number so abs(-5) = 5 and abs(5) = 5
#             # without absolute we would need to check BOTH directions separately for -x, x and -y,y
#             # which is exactly what you care about for a boundary check.
#     def is_out_of_bounds(self):
#         """This method checks if the snake reaches out of bounds"""
#         game_running = True
#
#         # x coordinates and y coordinate for turtle position and oob (out of bounds)
#         x_pos = self.turtle.xcor()
#         y_pos = self.turtle.ycor()
#         oob_x = 260
#         oob_y = 260
#
#         if (abs(x_pos) > oob_x or
#                 abs(y_pos) > oob_y):
#
#             # write the game over text at center of the screen
#             self.turtle.pendown()
#             self.turtle.home() # go to 0,0
#             self.turtle.color("white")
#             self.turtle.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
#
#             game_running = False
#
#         return game_running
#
#


from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # head + 2 starting body segments
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.screen = Screen()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Builds the initial snake from STARTING_POSITIONS"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Creates one new square segment at the given (x, y) position"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake_size(self):
        """Adds a new segment at the position of the current last segment
        (it'll catch up visually on the next move cycle)"""
        self.add_segment(self.segments[-1].position())

    def snake_default_movement(self):

#
# Let's connect it piece by piece to the kids example.

# Say you have 4 kids in line: 🧒1 🧒2 🧒3 🧒4

# In code, they live in a list called self.segments,
    # and each kid has a position number (index) starting from 0:

# The lineup, again:
# self.segments[0] = Kid 1 (the leader/head)
# self.segments[1] = Kid 2
# self.segments[2] = Kid 3
# self.segments[3] = Kid 4 (the very last kid)

# THE FOR LOOP#

    # Let's connect it piece by piece to the kids example.
    #
    # Say you have 4 kids in line: 🧒1 🧒2 🧒3 🧒4
    #
    # In code, they live in a list called self.segments, and each kid has a position number (index) starting from 0:
    #
    # self.segments[0] = Kid 1 (the leader/head)
    # self.segments[1] = Kid 2
    # self.segments[2] = Kid 3
    # self.segments[3] = Kid 4 (the very last kid)

    # THE len(self.segments -1, 0, 1) #

    # So len(self.segments) = 4 (there are 4 kids total).
    #
    # Now let's break down range(len(self.segments) - 1, 0, -1) — range(start, stop, step):
    #
    # len(self.segments) - 1 → 4 - 1 → 3. This is the start: index 3, which is Kid 4, the very last kid. We start with the last kid, just like the story said.
    # 0 → this is the stop. Important: range() stops before it reaches this number, so it never actually includes 0. That's on purpose — index 0 is Kid 1, the leader, and the leader doesn't copy anyone, so we skip them entirely.
    # -1 → this is the step, meaning "count backwards, one at a time" instead of forwards.
    #
    # So range(3, 0, -1) produces: 3, 2, 1
    #
    # Which in kid terms means the loop visits, in this order:
    #
    # seg_num = 3 → Kid 4 (last kid) — walks to where Kid 3 was
    # seg_num = 2 → Kid 3 — walks to where Kid 2 was
    # seg_num = 1 → Kid 2 — walks to where Kid 1 (leader) was
    #
    # And then it stops — because Kid 1 (index 0) never gets included in this loop. That matches the story:
        # the leader doesn't follow anyone,
    # #


    # THE SEGMENT X,Y COORDINATES #

    # Now, what does each kid actually do on their turn? That's the body of the loop:
    # python
    # new_x = self.segments[seg_num - 1].xcor()
    # new_y = self.segments[seg_num - 1].ycor()
    # self.segments[seg_num].goto(new_x, new_y)

    # Think of seg_num as "me, the kid whose turn it is." And seg_num - 1 is "the kid standing right in front of me."
    # So in plain words, every kid's turn looks like this:
    # new_x, new_y = ...xcor(), ...ycor() → "Peek at exactly where the kid in front of me is currently standing."
    # self.segments[seg_num].goto(new_x, new_y) → "Now walk to that exact spot."

    # Let's trace it turn by turn:
    # Turn 1 (seg_num = 3, Kid 4's turn): Kid 4 peeks at Kid 3's spot (seg_num - 1 = index 2 = Kid 3),
        # then walks there.
    # Turn 2 (seg_num = 2, Kid 3's turn): Kid 3 peeks at Kid 2's spot, then walks there.
    # Turn 3 (seg_num = 1, Kid 2's turn): Kid 2 peeks at Kid 1's (the leader's) spot, then walks there.
    # And that's the end of the loop — three kids have each taken one step, always into the spot the kid ahead of
        # them just vacated.

# OUTSIDE THE LOOP #
# Finally, outside the loop:
# python
# self.head.forward(MOVE_DISTANCE)
# This is Kid 1, the leader, who never copies anybody. After all the other kids have shuffled forward into
    # each other's old spots, the leader finally takes a real, brand-new step forward — into ground nobody's stood
    # on before.
# So the whole thing, top to bottom, is really just: "Starting from the back, each kid copies the spot of the kid
    # ahead of them — and once everyone's shuffled forward, the leader takes the one real new step."

        """Moves the snake: each segment moves to where the one in front of it was,
        and the head moves forward in its current heading"""
        # move body segments from tail to head (backwards through the list)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # move the head forward
        self.head.forward(MOVE_DISTANCE)

    def snake_body_collision(self):
        """Checks if the head has collided with any body segment"""
        game_running = True

        # slicing and only looking at everything that is NOT the head
        for segment in self.segments[1:]:  # skip the head itself
            if self.head.distance(segment) < 10:
                print("Tail Collision")
                game_running = False
                break

        return game_running

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def event_listener(self):
        self.screen.listen()

    def key_movement(self):
        self.screen.onkey(fun=self.go_up, key="Up")
        self.screen.onkey(fun=self.go_down, key="Down")
        self.screen.onkey(fun=self.go_left, key="Left")
        self.screen.onkey(fun=self.go_right, key="Right")

    def is_out_of_bounds(self):
        """Checks if the snake's head reaches out of bounds"""
        game_running = True

        x_pos = self.head.xcor()
        y_pos = self.head.ycor()
        oob_x = 260
        oob_y = 260

        # So abs() just means "how far from center, regardless of direction" —
        #             # it basically just strips the - from the number so abs(-5) = 5 and abs(5) = 5
        #             # without absolute we would need to check BOTH directions separately for -x, x and -y,y
        #             # which is exactly what you care about for a boundary check.
        #     def is_out_of_bounds(self):
        #         """This method checks if the snake reaches out of bounds"""
        #         game_running = True
        #
        #         # x coordinates and y coordinate for turtle position and oob (out of bounds)

        if abs(x_pos) > oob_x or abs(y_pos) > oob_y:
            self.head.pendown()
            self.head.home()
            self.head.color("white")
            self.head.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
            game_running = False

        return game_running





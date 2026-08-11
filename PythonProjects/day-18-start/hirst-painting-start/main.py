###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

import colorgram, random
from turtle import Turtle, Screen
import turtle


t = Turtle()
t.speed(0)

#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)

# Creating our own spot painting like David Hurst
rgb_colors_turtle = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r,g,b)
    rgb_colors_turtle.append(new_color)

print(rgb_colors_turtle)
print(len(rgb_colors_turtle))

# needed for colormode
turtle.colormode(255)
t.hideturtle()
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.penup()
t.setposition(-200,-200)

for row in range(1, 101):
    t.dot(20, random.choice(color_list))  # Draw dot first starting at 0,0
    t.forward(50)  # Move forward to the next dot space

    if row % 10 == 0:
        t.setheading(90)  # face up
        t.forward(50) # move 50 up
        t.setheading(180) # face left
        t.forward(500) # move back to first dot dran above at location 0,50
        t.setheading(0) # go easy, doing 360 would also work


#
# # Set starting position for the bottom-left corner
# start_x = -200
# start_y = -200
#
# # Outer loop controls the 10 rows
# for row in range(10):
#
#     #pen up so dont draw
#     t.penup()
#     # Move turtle to the start of the current row (shifting up by 50 pixels per row)
#         # start_y + (row * 50): Automatically calculates the height of the next row.
#         # The first row sits at -200,  -200 + (0*50) = -200
#         # the second row shifts up to -150, -200 + (1*50) = -150
#         # the third to -100, and so on. -200 + (2*50) = -100
#     t.setposition(start_x, start_y + (row * 50))
#
#     # Inner loop controls the 10 dots in each row
#     for col in range(10):
#         t.dot(20, random.choice(color_list))  # Draw dot first
#         t.forward(50)  # Move forward to the next dot space


# This is the last thing we will do to close the screen
screen = Screen()
screen.exitonclick()

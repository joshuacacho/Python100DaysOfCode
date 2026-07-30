# Blueprint for a turtle where we can tell the turtle to
    # pick different colors,
    # brush sizes and color on the screen
    # has image of a turtle with tooth brush

#
# import another_module # from the another_module.py
#
# # use the variable another_module = 12 and print it our from the another_module.py file
# print(another_module.another_module_value) # prints 12
#
# # THIS TURTLE blueprint already comes within Python installed
# import turtle
# from turtle import Turtle, Screen # can also just take what you need
#
# # using values from the turtle module
#     # fetches the class from the turtle module and initialized it using () from the blueprint and
#     # saved into an object called timmy_the_turtle
# timmy_the_turtle = Turtle()
# print(timmy_the_turtle) #different than a string
#
# # objecct.attribute
# my_screen = Screen()
# print(my_screen.canvheight)
#
# # object methods
#     # allows us to close our screen when we click on the screen
#
# # changes the shape of the arrow to a turtle when it appears on our screen below
# timmy_the_turtle.shape("turtle")
# # change the color of the turtle
# timmy_the_turtle.color("red")
# # move the turtle 100 paces
# timmy_the_turtle.forward(100)
# # exit screen on click
# my_screen.exitonclick()
#

# using the added package prettytable create a table using the documentation
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.add_column("Food Supply", ["20", "40", "60"])
table.align = 'l'
print(table)
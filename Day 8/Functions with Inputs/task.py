#Function with NO input param

# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello There")
    print("We hope you are doing well")
    print("Welcome to the class")

#call the name of the function
greet()



#Function WITH input param

#my function to add two numbers together
def add(a,b):
    return a + b # you may not want to print it and use the return value so not including print statement

print(add(5,4))


# Life in Weeks
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#
# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
#
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
#
# **Warning** The function must be called life_in_weeks for the tests to pass. Also the output must have the same punctuation and spelling as the example. Including the full stop!
# Example Input
# 56
# Example Output
# You have 1768 weeks left.

#tbis function assumes we live until 90
def life_in_weeks(current_age):
    years_left_to_live = 90 - current_age
    weeks_left_to_live = years_left_to_live * 52 #52 weeks per year
    print(f"You have {weeks_left_to_live} weeks left")

life_in_weeks(20)